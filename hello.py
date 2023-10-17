#!/usr/bin/env python3

# Abaixo o comentário de documentação dentro do bloco de aspas
# duplas.

"""Hello World Multi Linguas

Dependendo da línguagem do ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável LANG devidamente configurada. ex:

    export LANG=pt_BR
    
Execução:

    python3 hello.py
    ou
    ./hello.py
"""

__version__ = "0.0.1"
__autor__= "Rodrigo Lima Cavalcante"
__license__= "Unlicense"

# Dunder

# Este programa imprime Hello world

# padrão PascalCase - CurrentLanguage

# padrão snake_case - minusculas separadas por underline


current_language = "pt_BR"

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, mundo!"
elif current_language == "it_IT":    
    msg = "Ciao, Mondo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"
    
print(msg) # test-ignore - trecho ignorado pós-bloco 

