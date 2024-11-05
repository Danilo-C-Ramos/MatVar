from manim import *

class ExampleSphere(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=PI / 6, theta=PI / 6)
        sphere1 = Sphere(
            center=(0, 0, 0),
            radius=1,
            resolution=(20, 20),
            u_range=[0.001, PI - 0.001],
            v_range=[0, TAU]
        )
        axes = ThreeDAxes()
        def update(mob, alpha):
            angle = alpha * TAU
            sphere1 = Sphere(
            center=(3, 0, 0),
            radius=1,
            resolution=(20, 20),
            u_range=[0.001, PI - 0.001],
            v_range=[0, angle]
        )
        self.add(axes)

        sphere1.set_color(BLUE)
        self.add(sphere1)
        self.play(UpdateFromAlphaFunc(sphere1, update), run_time=1, rate_func=linear)
        