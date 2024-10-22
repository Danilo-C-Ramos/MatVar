from manim import *

class ExampleFunctionGraph(Scene):
    def construct(self):
        cos_func = FunctionGraph(lambda t: np.cos(t) + 0.5 * np.cos(7 * t) + (1 / 7) * np.cos(14 * t),
            color=RED,  
        )
        axes = Axes()
        sin_func_1 = axes.plot(lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t))

        sin_func_2 = FunctionGraph(
            lambda t: np.sin(t) + 0.5 * np.sin(7 * t) + (1 / 7) * np.sin(14 * t),
            x_range=[-4, 4],
            color=GREEN,
        ).move_to([0, 1, 0])

        
        self.add(cos_func)
        self.play(Transform(cos_func,sin_func_1))