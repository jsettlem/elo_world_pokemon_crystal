import itertools
import os
import subprocess
import uuid
from pprint import pprint
import random


def main():
    movies = []
    input_directory = "W:\\elo_world_output\\crystal-red"
    for directory in os.walk(input_directory):
        for file in directory[2]:
            if file.endswith(".mov"):
                movies.append(directory[0] + "\\" + file)

        input_directory = "W:\\elo_world_output\\crystal-red-2"

    for directory in os.walk(input_directory):
        for file in directory[2]:
            if file.endswith(".mov"):
                movies.append(directory[0] + "\\" + file)
    random.shuffle(movies)
    # pprint(movies)

    width = 12
    height = 5
    duration = 60 + 50
    video_count = width * height

    for mosaic_index in range(len(movies) // video_count):
        example_movies = movies[mosaic_index * video_count:mosaic_index * video_count + video_count]


        movie_path = f"mosaic_red/fullres_small/long_mosaic_{str(uuid.uuid4())}"
        os.makedirs(movie_path, exist_ok=True)

        scale_filter = "scale=160:144:flags=neighbor"
        complex_filters = [*(f"[{i}:v] {scale_filter} [v{i}];" for i in range(video_count)),
                           "".join(f"[v{i}]" for i in range(video_count)) + f"xstack=grid={width}x{height}[vout];",
                           ]

        with open(f"{movie_path}-filters.txt", "w") as f:
            f.write("".join(complex_filters))

        call = ["Z:\\Downloads\\ffmpeg-2023-05-04-git-4006c71d19-full_build\\ffmpeg-2023-05-04-git-4006c71d19-full_build\\bin\\ffmpeg.exe",

                *[o for i in zip(
                    itertools.repeat("-stream_loop"),
                    itertools.repeat("-1"),
                    itertools.repeat("-i"),
                    (movie for movie in example_movies)
                ) for o in i],
                # "-filter_complex",
                # "".join(complex_filters),
                "-filter_complex_script",
                f"{movie_path}-filters.txt",
                # f"amix=inputs={width * height}[aout]",
                "-map", "[vout]",
                # "-map", "[aout]",
                # "-c:v", "libx264",
                # "-s",  f"{width * 160}x{height * 144}",
                # "-sws_flags", "neighbor",
                # "-ac", "2",
                "-t", "00:01:50",
                f"{movie_path}/%05d.png"
                ]

        pprint(call)
        subprocess.run(call)

def combine_mosaics():
    movies = []
    input_directory = "Z:/Dropbox/elo-world/elo_world_pokemon_crystal/mosaic_red/fullres_small"

    for directory in os.listdir(input_directory):
        if os.path.isdir(input_directory + "/" + directory):
            movies.append(directory)

    random.shuffle(movies)

    width = 2
    height = 3
    number_of_movies = width * height
    for mosaic_index in range(len(movies) // number_of_movies):

        movie_path = f"mosaic_red/fullres/combined_mosaic_{str(uuid.uuid4())}"
        os.makedirs(movie_path, exist_ok=True)

        input_movies = movies[mosaic_index * number_of_movies:mosaic_index * number_of_movies + number_of_movies]
        input_movies = [f"{input_directory}/{movie}/%05d.png" for movie in input_movies]

        complex_filter = f"xstack=grid={width}x{height}"

        call = ["Z:\\Downloads\\ffmpeg-2023-05-04-git-4006c71d19-full_build\\ffmpeg-2023-05-04-git-4006c71d19-full_build\\bin\\ffmpeg.exe",
            *[o for i in zip(
                itertools.repeat("-i"),
                (movie for movie in input_movies)
            ) for o in i],
            "-filter_complex",
            complex_filter,
            "-s", "3840x2160",
            f"{movie_path}/%05d.png"
        ]

        pprint(call)
        subprocess.run(call)


if __name__ == '__main__':
    # main()
    # main()
    # main()

    combine_mosaics()
