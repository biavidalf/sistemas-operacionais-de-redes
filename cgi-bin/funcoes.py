# Arquivo para armazinar as funções que vao retornar html

# CABEÇALHO
def header():
    print("""
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>EUA/BR - InterConvert</title>
        <link rel="stylesheet" href="../css/estilo.css">
    </head>
    <body>
        <div id="cabecalho"> <!-- AREA DO CABEÇALHO -->
            <div id="logo">
                <h1>Inter<span class="branco">Convert</span></h1>
            </div>
            <div id="menu">
                <span class="selecionado"><a href="index.py">HOME</a></span>|
                <a href="conversor.py">CONVERTER</a>|
                <a href="trabalho.py">TRABALHO</a>
            </div>
        </div>

        <div class="linha"></div>
    """)


def conv():
    print("""
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>EUA/BR - InterConvert</title>
        <link rel="stylesheet" href="../css/estilo.css">
    </head>
    <body>
        <div id="cabecalho"> <!-- AREA DO CABEÇALHO -->
            <div id="logo">
                <h1>Inter<span class="branco">Convert</span></h1>
            </div>
            <div id="menu">
                <a href="index.py">HOME</a>|
                <span class="selecionado"><a href="conversor.py">CONVERTER</a></span>|
                <a href="trabalho.py">TRABALHO</a>
            </div>
        </div>

        <div class="linha"></div>
    """)


def lateral():
    print("""
    <div id="lateral">
        <div>
            <h3>Conversões Disponiveis</h3>
            <div>
                <a href="altura.py">Altura</a><hr>
                <a href="distancia.py">Distância</a><hr>
                <a href="dinheiro.py">Dinheiro</a><hr>
                <a href="sapato.py">Sapato</a><hr>
                <a href="peso.py">Peso</a><br>
            </div>
        </div>
    </div>
    """)


def footer():
    print("""
        <div id="rodape"><h4>Todos os direitos reservados</h4></div>
    </body>
    </html>
    """)


def index():
    print("""
        <div id="postagens">

            <div class="postagem">
                <h2><span class="titulo">Qual o intuito do site?</span></h2>
                Ajudar brasileiros que precisam converter suas medidas para as medidas utilizadas nos EUA de um
                jeito prático, simples e compacto. Comece a converter clicando no link abaixo:
                <br><a href="conversor.py">Quero converter</a>
            </div>
            <br>
            <div class="postagem">
                <h2><span class="titulo">Como converter?</span></h2>
                Temos uma página dedicada a te ajudar na hora das conversões, clique no link abaixo para ser 
                redirecionado:
                <br><a href="conversor.py">Como converter?</a>
            </div>
            <br>
            <div class="postagem">
                <h2><span class="titulo">Sistemas Operacionais de Redes</span></h2>
                Esse é um trabalho para a cadeira técnica de SOR do IFCE Campus Fortaleza, cujo professor se chama
                José Roberto. Saiba mais sobre o trabalho clicando no link abaixo:
                <br><a href="trabalho.py">Saiba mais</a>
            </div>
            <br>

        </div>
    """)


def conversor():
    print("""
        <div id="postagens">

            <div class="postagem">
                <h2><span class="titulo">Conversões</span></h2>
                Escolha uma das opções na barra lateral direita para começar a converter!
            </div>
            <br>
                <div class="postagem">
                <h2><span class="titulo">Como converter?</span></h2>
                Ao clicar na opção desejada na barra de navegação ao lado, você irá ser redirecionado
                para uma página que pede para você entrar com os seus dados.
                <br>
                Atenção! Digite seus dados utilizando os valores brasileiros para ser retornado os
                valores usados nos Estados Unidos.
            </div>
            <br>
                <div class="postagem">
                <h2><span class="titulo">Meu convertor não funciona!</span></h2>
                Cheque se está utilizando PONTO invés de VÍRGULA, se está usando as medidas instruidas e
                também se está colocando o valor na medida brasileira!
            </div>

        </div>
    """)


def trabalho():
    print("""
        <div id="postagens">

            <div class="postagem">
                <h2><span class="titulo">Qual trabalho foi realizado?</span></h2>
                Trabalho em que foi requisitado uma aplicação web utilizando Python e CGI, podendo ter o tema do
                trabalho anterior ou uma nova ideia.
                <br>
                Decidi continuar com a ideia da minha atividade anterior, que é caracterizada por conversões BR -> EUA.
            </div>
            <br>
            <div class="postagem">
                <h2><span class="titulo">Qual o aluno?</span></h2>
                Trabalho realizado por Beatriz Vidal Freire, aluna do P7 de informática do IFCE Campus Fortaleza.
            </div>
            <br>
            <div class="postagem">
                <h2><span class="titulo">Qual o professor?</span></h2>
                Um dos melhores professores do atual P7, José Roberto nos dá aulas sobre python com extrema maestria
                e uma incrível didática.
            </div>
            <br>

        </div>
    """)


def trab():
    print("""
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>EUA/BR - InterConvert</title>
        <link rel="stylesheet" href="../css/estilo.css">
    </head>
    <body>
        <div id="cabecalho"> <!-- AREA DO CABEÇALHO -->
            <div id="logo">
                <h1>Inter<span class="branco">Convert</span></h1>
            </div>
            <div id="menu">
                <a href="index.py">HOME</a>|
                <a href="conversor.py">CONVERTER</a>|
                <span class="selecionado"><a href="trabalho.py">TRABALHO</a></span>
            </div>
        </div>

        <div class="linha"></div>
    """)

