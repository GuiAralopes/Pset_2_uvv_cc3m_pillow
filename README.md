# Pset_2

## Ciência da Computação UVV
**Aluno:** Guilherme Araujo Lopes 

**Professor:** [Abrantes Araújo Silva Filho](https://github.com/abrantesasf)

**Disciplina:** Linguagem de Programação

**Turma:** CC3M

# PILLOW: 
## Python Imaging Library (abreviado para PIL) é uma biblioteca da linguagem de programação Python que adiciona suporte à abertura e gravação de muitos formatos de imagem diferentes.

## Questões e Imagens de Teste:

todas as imagens estão disponíveis na pasta [meu_teste](https://github.com/GuiAralopes/Pset_2_uvv_cc3m_pillow/tree/main/test_images/meu_teste)

### QUESTÃO 01:

Se você passar essa imagem pelo filtro de inversão, qual seria o output esperado? Justifique sua resposta.

Espera-se que o filtro de inversão relita os pixels e que as cores deles se invertam, tendo áreas mais pretas ficando brancas e brancas se tornando pretas

![mushroom](https://github.com/GuiAralopes/Pset_2_uvv_cc3m_pillow/blob/main/test_images/meu_teste/mushroom.png)
![inverted_mushroom](https://github.com/GuiAralopes/Pset_2_uvv_cc3m_pillow/blob/main/test_images/meu_teste/inverter_cogumelo.png)

## QUESTÃO 02:

Faça a depuração e, quando terminar, seu código deve conseguir passar em todos os testes do grupo de teste TestInvertido (incluindo especificamente o que você acabou de criar). Execute seu filtro de inversão na imagem imagens_teste/peixe.png, salve o resultado como uma imagem PNG e salve a imagem em seu repositório GitHub.

![fish](https://github.com/GuiAralopes/Pset_2_uvv_cc3m_pillow/blob/main/test_images/meu_teste/bluegill.png)
![inverted_fish](https://github.com/GuiAralopes/Pset_2_uvv_cc3m_pillow/blob/main/test_images/meu_teste/inverter_fish.png)

## QUESTÃO 03:

considere uma etapa de correlacionar uma imagem com o seguinte kernel:
| 0.00|-0.07| 0.00|
|-|-|-|
|-0.45|1.20| -0.25|
|0.00|-0.12| 0.00|


### Qual será o valor do pixel na imagem de saída no local indicado pelo destaque vermelho? Observe que neste ponto ainda não arredondamos ou recortamos o valor, informe exatamente como você calculou. Observação: demonstre passo a passo os cálculos realizados.
![imagem_Q3](https://github.com/GuiAralopes/Pset_2_uvv_cc3m_pillow/blob/main/test_images/meu_teste/Captura%20de%20tela%202022-09-05%20163733.jpg)


### O cálculo se baseia em somar os valores de associação dos pixels
O(x,y) = (0.00 * 80) + (-0.07 * 53) + (0.00 * 99) + (-0.45 * 129) + (1.20 * 127) + (-0.25 * 148) + (0.00 * 175) + (-0.12 * 174) + (0.00 * 193)

O(x,y) = 0 + (-3.71) + 0 + (-58.05) + 152.4 + (-37) + 0 + 0 + (-20.88) + 0

O(x,y) = 32.76
## QUESTÃO 04:

quando você tiver implementado seu código, tente executá-lo em imagens_teste/porco.png com o seguinte kernel 9 × 9:
|0 |0 |0 |0 |0 |0 |0 |0 |0|
|-|-|-|-|-|-|-|-|-|
|0 |0 |0 |0 |0 |0 |0 |0 |0|
|1 |0 |0 |0 |0 |0 |0 |0 |0|
|0 |0 |0 |0 |0 |0 |0 |0 |0|
|0 |0 |0 |0 |0 |0 |0 |0 |0|
|0 |0 |0 |0 |0 |0 |0 |0 |0|
|0 |0 |0 |0 |0 |0 |0 |0 |0|
|0 |0 |0 |0 |0 |0 |0 |0 |0|
|0 |0 |0 |0 |0 |0 |0 |0 |0|

![pigbird](https://github.com/GuiAralopes/Pset_2_uvv_cc3m_pillow/blob/main/test_images/meu_teste/pig.png)
![correlated_pigbirg](https://github.com/GuiAralopes/Pset_2_uvv_cc3m_pillow/blob/main/test_images/meu_teste/pig_correlate.png)

### Quando você terminar e seu código passar em todos os testes relacionados ao desfoque, execute seu filtro na imagem imagens_teste/gato.png com um kernel de desfoque de caixa de tamanho 5, salve o resultado como uma imagem PNG e faça o upload para seu repositório GitHub.

![blurred_cat](https://github.com/GuiAralopes/Pset_2_uvv_cc3m_pillow/blob/main/test_images/meu_teste/cat_borrado.png)

## QUESTÃO 05:

se quisermos usar uma versão desfocada B que foi feita com um kernel de desfoque de caixa de 3 × 3, que kernel k poderíamos usar para calcular toda a imagem nítida com uma única correlação? Justifique sua resposta mostrando os cálculos.

         k1 = [[0, 0, 0],       k2 = [[1/9, 1/9, 1/9],          k_result = [[-1/9,-1/9, -1/9],
               [0, 2, 0],     -       [1/9, 1/9, 1/9],     =                [-1/9, 17/9,-1/9], 
               [0, 0, 0]]             [1/9, 1/9, 1/9]]                      [-1/9, -1/9,-1/9]

### Quando terminar e seu código passar nos testes relacionados à nitidez, execute seu filtro de nitidez na imagem imagens_teste/python.png usando um kernel de tamanho 11, salve o resultado como uma imagem PNG e faça o upload no seu repositório GitHub.

![sharpened_snake](https://github.com/GuiAralopes/Pset_2_uvv_cc3m_pillow/blob/main/test_images/meu_teste/python_sharpened.png)


## QUESTÃO 06:

explique o que cada um dos kernels acima, por si só, está fazendo. Tente executar mostrar nos resultados dessas correlações intermediárias para ter uma noção do que está acontecendo aqui.
Detecta as bordas no eixo X (Horizontal) da imagem
       
        kx = [[-1, 0, 1],
              [-2, 0, 2],
              [-1, 0, 1]]
Detecta as bordas no eixo Y (Vertical) da imagem         
     
       ky = [[-1, -2, -1],
             [ 0,  0,  0],
             [ 1,  2,  1]]
![construct](https://github.com/GuiAralopes/Pset_2_uvv_cc3m_pillow/blob/main/test_images/meu_teste/construct.png)
![construct_edges](https://github.com/GuiAralopes/Pset_2_uvv_cc3m_pillow/blob/main/test_images/meu_teste/construct_edge.png)

## As imagens de obra em cada eixo estão na pasta [meu_teste](https://github.com/GuiAralopes/Pset_2_uvv_cc3m_pillow/tree/main/test_images/meu_teste)

### [Eixo x](https://github.com/GuiAralopes/Pset_2_uvv_cc3m_pillow/blob/main/test_images/meu_teste/edge_axis_x.png) 
### [Eixo y](https://github.com/GuiAralopes/Pset_2_uvv_cc3m_pillow/blob/main/test_images/meu_teste/edge_axis_y.png) 
