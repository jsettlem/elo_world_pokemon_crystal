import os
import subprocess
from dataclasses import dataclass


def create_concat_file(list_txt, files):
	with open(list_txt, 'w') as f:
		f.write("ffconcat version 1.0\n")
		f.write("\n".join(f"file '{f}'" for f in files))


def build_movie(movie_context: "MovieContext"):
	files = [f for f in os.listdir(movie_context.movie_working_dir)]
	files.sort()

	video_list_txt = f"{movie_context.movie_working_dir}/videos.txt"
	audio_list_txt = f"{movie_context.movie_working_dir}/audio.txt"

	create_concat_file(video_list_txt, [f for f in files if f.endswith(".avi")])
	create_concat_file(audio_list_txt, [f for f in files if f.endswith(".wav")])

	output_movie = f"{movie_context.movie_output_dir}/movies/{movie_context.movie_name}.mkv"
	os.makedirs(os.path.dirname(output_movie), exist_ok=True)

	subprocess.call(["ffmpeg",
	                 "-i", video_list_txt,
	                 "-i", audio_list_txt,
	                 "-c:v", "libx265",
	                 "-preset", "slow",
	                 "-crf", "17",
	                 "-c:a", "libopus",
	                 "-b:a", "32k",
	                 "-threads", "1",
	                 output_movie])


@dataclass
class MovieContext:
	movie_name: str
	movie_index: int
	movie_working_dir: str
	movie_output_dir: str
