from manim import *

class SolidoDeRevolucao(ThreeDScene):
    def construct(self):
        # Criando os eixos 3D
        axes = ThreeDAxes(x_range=[-3, 3, 1], y_range=[-1, 9, 1], z_range=[-1, 9, 1])

        # Criando a curva da função f(x) = x^2
        curva = axes.plot(lambda x: x**2, color=BLUE, x_range=[-2, 2])

        # Criando a superfície de revolução rotacionando a curva em torno do eixo x
        superficie = Surface(
            lambda u, v: axes.c2p(u, np.cos(v) * (u**2), np.sin(v) * (u**2)),  # Definindo como rotacionar a curva
            u_range=[-2, 2], v_range=[0, TAU],  # Rotacionar a curva de 0 a 2π
            checkerboard_colors=[BLUE, BLUE_B],  # Cor da superfície
        )

        # Definindo a posição da câmera para visualizar o sólido 3D
        self.set_camera_orientation(phi=75 * DEGREES, theta=45 * DEGREES)

        # Adicionando os objetos à cena
        self.add(axes, curva)

        # Animando a criação da superfície de revolução
        self.play(ReplacementTransform(curva, superficie), run_time=4)
        self.begin_ambient_camera_rotation(rate=0.1)  # Movimentando a câmera ao redor do sólido
        self.wait(2)
        self.stop_ambient_camera_rotation()
        self.wait()