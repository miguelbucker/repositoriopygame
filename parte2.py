import pygame

# Definindo as constantes de cores com o sistema RGB
# Letras maiúsculas são constantes que não se alteram
PRETO = (0,0,0)
BRANCO = (255,255,255)
VERMELHO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)

# Definindo consta com valor de PI (Utilizado para o cálculo na criação das figuras)
PI = 3.1416

# Inicializando os módulos do Pygame
pygame.init()

# Criando a najela de tamanho 800x600 e com título "Figuras e Texto"
janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Figuras e texto")

# Utilizando método fill() para aplicar cor a superfície 
janela.fill(PRETO)

# A mudança de cor da superfície acima somente será aplicada quando rodar o código abaixo
pygame.display.update()

# Trabalhando com texto
fonte = pygame.font.Font(None,48)

# são dois parametros = nome da fonte e tamanho, ao colocar NONE ele usa a fonte padrão do sistema

# Utilizando o método render() para renderizar o texto a apresentar
font_path = "EduAUVICWANTHand-VariableFont_wght.ttf"
fonte = pygame.font.Font(font_path,40)
texto = fonte.render("Olá, mundo!", True, BRANCO, AZUL)
janela.blit(texto, [30,150])

# Utilizando o método line() para desenhar uma linha na tela
pygame.draw.line(janela, VERDE, [60,260], [420,260], 4)

# Utilizando o método polygon() para desenhar um polígono na tela
pygame.draw.polygon(janela, BRANCO, ([191,206], [236,277], [156,277]),0 )

# Utilizando o método CIRCLE() para desenhar um círculo na tela
pygame.draw.circle(janela, AZUL, (300,500), 20, 0 )

# Utilizando o método elipse() para desenhar um círculo na tela
pygame.draw.ellipse(janela, VERMELHO, (300,500,40,80) , 1)

# Utilizando o método react() para desenhar um retângulo na tela
pygame.draw.rect(janela, VERDE , (20,20,60,40) , 0)

# Utilizando o método arc() para desenhar um arco na tela
pygame.draw.arc(janela, VERMELHO , (250,75,150,125),  PI/2 , 3*PI, 2)
pygame.draw.arc(janela, BRANCO , (250,75,150,125), -PI/2 , PI/2 , 2)

pygame.display.update()

deve_continuar = True

while deve_continuar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            deve_continuar=False

# Fechar os módulos de pygame
pygame.quit()