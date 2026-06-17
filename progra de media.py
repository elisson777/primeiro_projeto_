from selectors import SelectSelector

nota1 = float(input("diga uma nota1 "))
nota2 = float(input("diga uma nota2 "))
nota3 = float(input("diga uma nota3 "))

media = (nota1 + nota2 + nota3) / 3

if media >= 3 and media < 7:
    print(f"ALUNX aprovado COM MEDIA {media:.2f}")
else:
    print(f"alunx em recuperacao com media {media:.2f}")
    fez_recuperacao = input("aluno ja fez recuperacao? s/n: ")
    if fez_recuperacao == "n":
    nota3   = float(input("diga uma nota3"))
    if nota_recuperacao >= 7:
        print("aluno aprovado pela recuperacao")
    else:
        print("aluno nao obeteve nota suficiente para ser aprovado pela recuperacao")
else:
print(f"aluno reprovado com media {media:.2f}")


