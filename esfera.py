from manim import *

class ExampleSphere(ThreeDScene):
    def construct(self):
        # Configuração da câmera
        self.set_camera_orientation(phi= 75 * DEGREES, theta= 70 * DEGREES)
        
        # Criar a esfera inicial
        sphere1 = Sphere(
            center=(0, 0, 0),
            radius=1,
            resolution=(10, 10),
            u_range=[0.001, PI - 0.001],
            v_range=[0, TAU]  # Começar com a esfera invisível
        )
        
        # Criar e adicionar os eixos
        axes = ThreeDAxes(
            axis_config = {"color": WHITE, "include_ticks": False, "include_numbers": False })
        self.add(axes)

        # Definir a cor da esfera
        sphere1.set_color(BLUE)
        self.add(sphere1)

        # Função de atualização para animar a esfera
        def update(mob, alpha):
            # Alterar o v_range para expandir a esfera conforme o tempo passa
            angle = alpha * TAU
            sphere1 = Sphere(
            center=(0, 0, 0),
            radius=2,
            resolution=(10, 10),
            u_range=[0.001, (PI - 0.001) * alpha],
            v_range=[0, TAU]  # Começar com a esfera invisível
        )
            mob.become(sphere1)

        self.play(Create(sphere1))
        # Animação: Atualizar a esfera ao longo do tempo
        #self.play(UpdateFromAlphaFunc(sphere1, update), run_time=1, rate_func=linear)
        self.wait(1)

class SphereFormation(ThreeDScene):
    def construct(self):
        # Configuração da câmera
        self.set_camera_orientation(phi=PI / 3, theta=PI / 4)
        
        # Criar o semicirculo
        semicircle = ParametricFunction(
            lambda t: np.array([
                np.cos(t),  # x = cos(t)
                np.sin(t),  # y = sin(t)
                0             # z = 0
            ]),
            t_range=[0, PI],  # Semicirculo de 0 a π
            color=BLUE
        )
        
        # Superfície da esfera gerada pela revolução do semicirculo
        sphere_surface = Surface(
            lambda u, v: np.array([
                np.cos(v) * np.sin(u),  # x
                np.sin(v) * np.sin(u),  # y
                np.cos(u)                # z
            ]),
            u_range=[0, PI],  # De 0 a π (semicirculo)
            v_range=[0, TAU],  # Revolução completa
            resolution=(20, 20)
        )

        # Adicionar eixos para referência
        axes = ThreeDAxes(x_range=[-2, 2],
                y_range=[-2, 2],
                z_range = [-2, 2],
                axis_config = {"color": WHITE,
                            "include_ticks": False, 
                            "include_numbers": False }
                            )
        self.add(axes)

        # Adicionar o semicirculo
        self.add(semicircle)

        # Animação da rotação do semicirculo
        self.play(Create(semicircle), run_time=1)
        self.wait(1)

        # Esconder o semicirculo e mostrar a superfície da esfera
        self.play(FadeOut(semicircle))
        self.play(Create(sphere_surface), run_time=1)
        self.wait(2)

class SphereFormationLateral(ThreeDScene):
    def construct(self):
        # Configuração da câmera
        self.set_camera_orientation(phi=PI / 4, theta=PI / 4)
        
        # Criar a superfície da esfera gerada pela revolução de um semicirculo
        sphere_surface = Surface(
            lambda u, v: np.array([
                np.cos(v) * np.sin(u),  # x
                np.sin(v) * np.sin(u),  # y
                np.cos(u)                # z
            ]),
            u_range=[0, PI],  # De 0 a π (semicirculo)
            v_range=[0, TAU],  # Revolução completa
            resolution=(20, 20)
        )

        # Adicionar eixos para referência
        axes = ThreeDAxes()
        self.add(axes)

        # Esconder a superfície da esfera inicialmente
        sphere_surface.set_fill(BLUE, opacity=0.8)
        sphere_surface.set_stroke(WHITE, width=0.5)
        
        # Adicionar a esfera à cena, mas escondida
        self.add(sphere_surface)
        sphere_surface.set_fill_opacity(0)  # Começa invisível

        # Função de atualização para criar a esfera lateralmente
        def update(mob, alpha):
            # Altera o v_range para expandir a esfera lateralmente
            mob.set_v_range([0, alpha * TAU])  # Crescer a esfera lateralmente (0 a 360 graus)
            mob.set_fill_opacity(0.8)  # Torna a esfera visível gradualmente

        # Animação: Atualizar a esfera ao longo do tempo
        self.play(UpdateFromAlphaFunc(sphere_surface, update), run_time=3, rate_func=linear)
        self.wait(1)

        # Girar a câmera para visualizar a esfera
        self.move_camera(phi=PI/6, theta=PI/6, run_time=2)
        self.begin_ambient_camera_rotation(rate=0.5)
        self.wait(3)
        self.stop_ambient_camera_rotation()
