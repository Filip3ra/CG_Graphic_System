# TP1 - Display File e Transformada de Viewport 

<b>Alunos</b>:  André Vinícius e Filipi Maciel

<b>Disciplina</b>: Computação Gráfica

O objetivo desse trabalho é desenvolver um programa que seja capaz de ler um arquivo contendo informações a respeito dos objetos a serem desenhados, da <i>window</i> e da <i>viewport</i>, e gerar um arquivo de saída contendo os objetos no sistema de coordenadas de <i>viewport</i>.

## Pré-requisitos

Inicialmente, é necessário que haja a instalação do Python em sua máquina, a instalação pode ser feita pelo seguinte comando: ''sudo apt-get install python''. Após isso, sugerimos que seja criado um ambiente virtual com conda ou python para que ao fim desse trabalho os pacotes e bibliotecas utilizados, possam ser apagados mais facilmente. O ambiente virtual pode ser criado atraves do conda, ou pelo próprio python. Nesse <a href='https://docs.conda.io/projects/conda/en/latest/user-guide/install/linux.html'>link</a> tem o tutorial do processo de instalação do conda. O comando para criar o ambiente conda (opcional) é o seguinte:

``conda create --name <nome_ambiente>``

Criado o ambiente, é necessário ativá-lo.

``conda activate <nome_ambiente>``

E por último, precisamos instalar o PySide, biblioteca responsável pela interface gráfica do nosso programa.

``pip install pyside6``

## Como executar

Para executar o trabalho, é preciso ir para pasta ``src`` e depois executar o arquivo ``main.py``.

``cd src``
``python3 main.py <arquivo_xml>``


