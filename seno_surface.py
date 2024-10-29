from manim import *
from math import *

class ParaSurface(ThreeDScene):
    def func(self, u, v):
        return np.array([u, np.cos(u) * np.cos(v),  np.cos(u) * np.sin(v)])
    
    def construct(self):
        axes = ThreeDAxes(x_range=[-4,4], x_length=8)
        surface = Surface(
            lambda u, v: axes.c2p(*self.func(u, v)),
            u_range=[-PI, PI],
            v_range=[0, TAU],
            resolution=8,
            fill_opacity=0.4,
            stroke_color=BLUE
        )
        curva = axes.plot(lambda x: cos(x), color=BLUE, x_range=[-4, 4])
        
        self.set_camera_orientation(theta=70 * DEGREES, phi=75 * DEGREES)
        self.play(Create(axes))
        self.play(Create(curva, run_time=2))
        self.wait()
    
        self.play(Create(surface, run_time=3))
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(3)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=75 * DEGREES, theta=30 * DEGREES)
        self.wait()


class SuperficieRevolucao(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        def superficie(u, v):
            r_u = np.exp(abs(u))  # Exemplo: Função parábola
            x = r_u * np.cos(v)
            y = r_u * np.sin(v)
            z = u
            return np.array([x, y, z])

        surface = Surface(
            lambda u, v: superficie(u, v),
            u_range=[0, 2], v_range=[0, TAU],
            resolution=(10, 10),
        )
        
        surface.set_style(fill_opacity=0.7, fill_color=BLUE)

        self.add(axes, surface)
        self.wait()


