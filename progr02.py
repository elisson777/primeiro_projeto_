nome= input("Qual o seu nome mano:")
print(f"ola {nome} seja bem vindo ao programa!`")
#primeiro
idade01= input(f"prazer em te conhecer {nome},me fale a sua idade")
print (f"parabens por sua idade {idade01}")
#segundo
local= input("vc mora aonda aliado?")
print(f"massa ainda bem ne que vc mora{local}")
 #3
preso= input(f"vc ja foi preso")
print("oloko meu")
#
saber1= input(f"mano e como la")
print(f"foda vey")
#
saber2=input(f"me passa sua idade estou achando que e mentira sua")

ano_nasc = int( input(f"prazer em te conhecer {nome}!, \n digite o ano de nascimento mano "))

idade = 2026 - ano_nasc
print(f"parabens por seus {idade} anos")

if idade > 18:
    print("Maior de idade")
elif idade < 18:
    print("maior de idade")
else:
    print("18 anos")
