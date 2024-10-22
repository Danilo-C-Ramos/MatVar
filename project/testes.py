from manim import *

class SolidoDeRevolucao(ThreeDScene):
    def construct(self):

        # Criando os eixos 3D
        axes = ThreeDAxes(
            x_range=[-4, 4, 1],
            y_range=[0, 5, 1], 
            z_range=[-4, 4, 1]
        )

        # Criando a curva da função f(x) = x^2
        curva = axes.plot(lambda x: x**2, color=RED, x_range=[0, 2], stroke_width=7)

        # Definir a orientação da câmera com uma leve inclinação
        self.set_camera_orientation(phi=-15 * DEGREES, theta=-90 * DEGREES)
        self.camera.frame_width = 12  # Aumenta a largura do frame, "afastando" a câmera

        # Adicionando a curva e animando a sua criação
        self.add(axes)
        self.play(Create(curva), run_time=2)

        # Criando a superfície inicial com ângulo zero
        surface = Surface(
            lambda u, v: axes.c2p(np.cos(v) * u, u**2, np.sin(v) * u),
            u_range=[0, 2], v_range=[0, 0],  # Inicialmente sem rotação
            checkerboard_colors=[BLUE, BLUE_B],
            resolution=(20, 20)
        )

        self.add(surface)

        # Atualizar a superfície com base no ângulo de rotação
        def update_surface(mob, alpha):
            angle = alpha * TAU  # Atualizar o ângulo de 0 a 2π
            surface = Surface(
                lambda u, v: axes.c2p(np.cos(v) * u, u**2, np.sin(v) * u),
                u_range=[0, 2], v_range=[0, angle],
                checkerboard_colors=[BLUE, BLUE_B],
                resolution=(20, 20)
            )
            mob.become(surface)
            self.add(axes)  # Re-adiciona os eixos para garantir que fiquem visíveis por cima da superfície

        # Animar a rotação gradual para formar o sólido
        self.play(UpdateFromAlphaFunc(surface, update_surface), run_time=3, rate_func=linear)

        self.wait(1)
