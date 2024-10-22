from manim import *
from math import *

class FuncaoExponencial(ThreeDScene):
    def construct(self):
        axes = Axes(
            x_range=[-2, 5],
            y_range=[-2, 19.2],
            axis_config={"color": BLACK,
                         "include_ticks": False, 
                        "include_numbers": False }  
        )
        plano_de_fundo = ImageMobject("fundo.png")
        
        # Ajusta o tamanho para cobrir toda a cena
        #plano_de_fundo.scale_to_fit_width(config.frame_width)
        #plano_de_fundo.scale_to_fit_height(config.frame_height)
        
        # Envia a imagem para o fundo
        plano_de_fundo.z_index = -1

        # Adiciona o plano de fundo à cena
        self.add(plano_de_fundo)
        
        # Criando a curva da função f(x) = x^2
        curva = axes.plot(lambda x: exp(x), color=RED, x_range=[0, 3], stroke_width=5)
        
        # Agrupando eixos e gráfico para redimensionar juntos
        grafico_completo = VGroup(axes, curva)
        axes.move_to([0.52,-1.9,0])
        curva.move_to([0.52,-1,0])
        # Reduzir o tamanho do gráfico para 70% do original
        grafico_completo.scale(0.7)
        self.wait()
        self.play(Create(axes), run_time=2)
        self.play(Create(curva), run_time=2, linear=True)
        self.wait(2)
        self.play(FadeOut(plano_de_fundo, run_time=3), axes.x_axis.animate.set_color(WHITE),
                axes.y_axis.animate.set_color(WHITE))
        self.play(grafico_completo.animate.move_to([0,0,0]))
        self.wait(3)

class Revolucao(ThreeDScene):
        def construct(self):
            axes = Axes(
            x_range=[-2, 5],
            y_range=[-2, 19.2],
            axis_config={"color": WHITE,
                         "include_ticks": False, 
                        "include_numbers": False }
            
        )
            curva = axes.plot(lambda x: exp(x), color=RED, x_range=[0, 3], stroke_width=5)
        
            # Agrupando eixos e gráfico para redimensionar juntos
            grafico_completo = VGroup(axes, curva)
            axes.move_to([0.52,-1.9,0])
            curva.move_to([0.52,-1,0])
            # Reduzir o tamanho do gráfico para 70% do original
            grafico_completo.scale(0.7)
            
            grafico_completo.move_to([0,0,0])

            axes3D = ThreeDAxes(
                x_range=[-2, 5],
                y_range=[-2, 19.2],
                z_range = [-10, 10, 2],
                axis_config = {"color": WHITE,
                            "include_ticks": False, 
                            "include_numbers": False }
                            )
            grafico_3d = axes3D.plot(lambda x: exp(x), color=RED, x_range=[0, 3], stroke_width=5)
            
            axes3D.move_to(axes.get_center())
            grafico_3d.move_to(curva.get_center())
            
            self.add(grafico_completo)
            self.wait(3)
            self.move_camera(zoom=0.5)
            # Animando a transição suave de 2D para 3D
            self.play(ReplacementTransform(grafico_completo, VGroup(axes3D, grafico_3d)))
            self.move_camera(
                phi= -15 * DEGREES, #Eixo X
                theta= -90 * DEGREES, #Mesma coisa que o gamma
                gamma= 0 * DEGREES, #Eixo Z
                #zoom=2,
                run_time=2  # Tempo da animação
            )
        
            self.wait(2)
        

