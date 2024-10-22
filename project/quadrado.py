from manim import *

class QuadradoTeste(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        func = axes.plot(lambda x: x**2,
            color=BLUE, x_range=[0, 4],
        )
        self.set_camera_orientation(phi=0 * DEGREES, theta=90 * DEGREES)
        self.add(axes)
        self.play(Create(func))
        self.wait(2)
        camera.capture_mobjects(func)
        self.begin_3dillusion_camera_rotation(rate=1)
        self.wait(PI)
        self.stop_3dillusion_camera_rotation()
