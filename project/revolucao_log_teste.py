from manim import *
import numpy as np
from math import *

class SuperficieRevolucao(ThreeDScene):
    def construct(self):
        # Configurando eixos 3D
        axes3D = ThreeDAxes(
            x_range=[-1, 5],
            y_range=[-1, 20],
            z_range=[-5, 5],
            axis_config={"color": WHITE}
        )

        # Função f(x) = e^x
        curva = axes3D.plot(
            lambda x: exp(x), 
            color=RED, 
            x_range=[0, 3], 
            stroke_width=5
        )

        # Movemos a curva para o local correto, alinhada com o eixo Y
        curva.shift(LEFT * 3)  # Alinha curva para que a revolução seja ao redor do eixo Y
        self.add(axes3D, curva)

        # Configuração da câmera para melhor visualização
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES, zoom=0.8)

        # Função paramétrica para a superfície de revolução
        def superficie(u, v):
            x = u * np.cos(v)
            z = u * np.sin(v)
            y = exp(u)  # Altura é f(u) = e^u
            return np.array([x, y, z])

        # Superfície inicial (v_range começando em 0)
        surface = Surface(
            lambda u, v: superficie(u, v),
            u_range=[0, 3], v_range=[0, 0],
            resolution=(10, 10),
            fill_opacity=0.7,
            fill_color=BLUE,
        )
        surface.shift(LEFT * 3)  # Alinha a superfície com a curva
        self.add(surface)

        # Função para atualizar a superfície gradualmente
        def atualizar_superficie(mob, alpha):
            """Atualiza a superfície até completar 2π."""
            v_max = TAU * alpha  # Aumenta o ângulo progressivamente
            mob.become(
                Surface(
                    lambda u, v: superficie(u, v),
                    u_range=[0, 3], v_range=[0, v_max],
                    resolution=(30, 30),
                    fill_opacity=0.7,
                    fill_color=BLUE,
                ).shift(LEFT * 3)  # Mantém a superfície alinhada
            )

        # Animação: Rotação da curva e criação da superfície
        self.play(
            Rotate(curva, angle=TAU, axis=Y_AXIS, about_point=ORIGIN, run_time=5),
            UpdateFromAlphaFunc(surface, atualizar_superficie),
            run_time=2
        )

        # Espera para observar o resultado final
        self.wait(2)
