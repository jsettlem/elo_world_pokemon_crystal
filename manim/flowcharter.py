import os

from manim import *

class Flowchart(Scene):

    def __init__(self, svg_path, **kwargs):
        self.svg_path = svg_path
        super().__init__(**kwargs)

    def construct(self):
        svg = SVGMobject(self.svg_path, svg_default={
            "color": None, "fill_color": None, "opacity": None, "fill_opacity": None, "stroke_color": None,
            "stroke_opacity": None, "stroke_width": 1
        }).scale_to_fit_height(7)

        self.wait(0.25)

        self.play(Write(svg, ), run_time=1)
        self.wait(1)

        self.wait(1)

        self.wait(3)

        self.play(Unwrite(svg, reverse=False), run_time=0.5)
        self.wait(0.5)

        self.wait(0.25)


class AiRoutine(Scene):

    def __init__(self, svg_path, **kwargs):
        self.svg_path = svg_path
        super().__init__(**kwargs)

    def construct(self):
        svg = SVGMobject(self.svg_path, svg_default={
            "color": None, "fill_color": None, "opacity": None, "fill_opacity": None, "stroke_color": None,
            "stroke_opacity": None, "stroke_width": 1
        }).scale_to_fit_width(4)

        self.play(Write(svg, ), run_time=1)
        self.wait(1)
        # move to top left corner and scale down
        self.play(svg.animate.shift(3 * UP + 3 * LEFT).scale(0.25), run_time=1)
        self.play(Unwrite(svg, reverse=False), run_time=1)


def main():
    config.background_opacity = 0
    config.transparent = True
    # config.background_color = WHITE
    config.quality = "fourk_quality"
    path = "Z:/Dropbox/elo-world/video-crystal/flowcharts/Crystal AI Diagrams (layered)/"
    # path = "Z:/Dropbox/elo-world/video-crystal/flowcharts/"

    files = [file for file in os.listdir(path) if (file.endswith(".svg") and "None" not in file and file == "AI_Smart_Snore.svg")]
    for file in files:
        config.output_file = file.replace(".svg", "")
        scene = Flowchart(path + file)
        scene.render()

def routines():
    config.background_opacity = 0
    config.transparent = True
    # config.background_color = WHITE
    config.quality = "fourk_quality"
    path = "Z:/Dropbox/elo-world/video-crystal/powerpoint/exports/routines/"
    # path = "Z:/Dropbox/elo-world/video-crystal/flowcharts/"

    files = [file for file in os.listdir(path) if file.endswith(".svg")]
    for file in files:
        config.output_file = file.replace(".svg", "")
        scene = AiRoutine(path + file)
        scene.render()

if __name__ == '__main__':
    main()
    # routines()
