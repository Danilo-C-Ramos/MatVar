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
        axes = ThreeDAxes(x_range=[-30, 30],
                y_range=[-30, 30],
                z_range = [-30, 30],
                axis_config = {"color": WHITE,
                            "include_ticks": False, 
                            "include_numbers": False }
                            )
        
        self.set_camera_orientation(phi = 0 * DEGREES, theta = -90 * DEGREES)
        grafico_3d = axes.plot(lambda x: exp(x), color=RED, x_range=[1, 3], stroke_width=5)
        self.move_camera(zoom=0.7)

        def superficie(u, v):
            r_u = log(u)  # Exemplo: Função parábola
            x = r_u * np.cos(v)
            y = u
            z = r_u * np.sin(v)
            return np.array([x, y, z])

        surface = Surface(
            lambda u, v: superficie(u, v),
            u_range=[1, 3], v_range=[0, TAU],
            resolution=(10, 10),
        )
        
        surface.set_style(fill_opacity=0.7, fill_color=BLUE)
        
        # Adicionar os eixos e os rótulos à cena
        self.add(axes)
        self.play(Create(grafico_3d))
        self.wait(2)
        self.move_camera(phi= 70 * DEGREES, theta= 70 * DEGREES, run_time=3)
        self.wait()
        self.play(Create(surface, run_time=1))
        self.wait()
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(3)


class JuntandoCenas(ThreeDScene):
    def construct(self):
        axes3D = ThreeDAxes(
                x_range=[-2, 5],
                y_range=[-2, 19.2],
                z_range = [-10, 10, 2],
                axis_config = {"color": WHITE,
                            "include_ticks": False, 
                            "include_numbers": False }
                            )
        grafico_3d = axes3D.plot(lambda x: exp(x), color=RED, x_range=[0, 3], stroke_width=5)
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

        def superficie(u, v):
            r_u = log(u)  # Exemplo: Função parábola
            x = r_u * np.cos(v)
            y = r_u * np.sin(v)
            z = u
            return np.array([x, y, z])

        surface = Surface(
            lambda u, v: superficie(u, v),
            u_range=[1, 3], v_range=[0, TAU],
            resolution=(10, 10),
        )
        
        surface.set_style(fill_opacity=0.7, fill_color=BLUE)
        
        self.add(axes3D)
        self.play(Create(surface, run_time=3))
        self.wait()

