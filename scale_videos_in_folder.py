import os
import subprocess


def scale():
    dir = "Z:\\Dropbox\\elo-world\\video-crystal\\blender\\textures\\monitor_videos"

    files = [f for f in os.listdir(dir) if f.endswith("cal.avi")]
    files.sort()

    for file in files:
        output_movie = f"{dir}/{file} - scaled.mov"

        subprocess.call(["ffmpeg",
                         "-i", f"{dir}/{file}",
                         "-vf", "scale=1600x1440",
                         "-sws_flags", "neighbor",
                         "-c:v", "libx264",
                         "-crf", "23",
                         # "-threads", "1",
                         output_movie])


def prores():
    dir = "Z:/Dropbox/elo-world/elo_world_pokemon_crystal/manim/media/videos/2160p60"
    files = [f for f in os.listdir(dir) if f.endswith(".mov")]
    files.sort()

    for file in files:
        output_movie = f"{dir}/{file} - prores.mov"

        subprocess.call(["ffmpeg",
                            "-i", f"{dir}/{file}",
                            "-c:v", "prores_ks",
                            "-pix_fmt", "yuva444p10le",
                            "-profile:v", "4444",
                            "-q:v", "20",
                            output_movie])

def apngs_to_png_sequences():
    dir = "Z:\\Dropbox\\elo-world\\video-crystal\\blender\\textures\\pokemon\\red"

    files = [f for f in os.listdir(dir) if f.endswith(".png")]
    files.sort()

    for file in files:
        output_folder = f"{dir}/{file[:-4]}"
        os.makedirs(output_folder, exist_ok=True)

        subprocess.call(["ffmpeg",
                            "-i", f"{dir}/{file}",
                         "-r", "60",
                            f"{output_folder}/%05d.png"])

if __name__ == '__main__':
    # scale()
    # prores()
    apngs_to_png_sequences()
