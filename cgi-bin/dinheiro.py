#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cgi
import cgitb

import funcoes
import functions

import sys
import codecs
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

cgitb.enable()

funcoes.conv()

print('<div id="principal">')
print("""
<div id="principal">
    <div id="postagens">

        <div class="postagem">
                <h2><span class="titulo">Dinheiro em REAIS para DOLAR:</span></h2>
                <form action="" method="post">
                    <div>
                        <label>Quantia em reais*:</label>
                        <input type="text" name="r" placeholder="1.99">
                    </div>
                    <input type="submit" value="Converter">
                </form>
        </div>


""")
#
form = cgi.FieldStorage()
br = form.getvalue("r")
if br:
    print(f"""
                <br>
                <h2><span class="titulo">Resultado:</span></h2>
                {functions.monetario(float(br))}
    """)

print("""
    <span class="data-postagem">*Pela alta variação do dólar, usamos como arredondamento que 1 dolar = 5 reais.*</span>
    </div>
</div>
""")

funcoes.lateral()
print('</div>')

funcoes.footer()
