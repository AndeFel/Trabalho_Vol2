import random

def rolar_d20():
    resultado = random.randint(1, 20)
    
    if resultado == 20:
        mensagem = "Acerto crítico!"
    elif resultado == 1:
        mensagem = "Falha crítica."
    elif resultado >= 15:
        mensagem = "Um bom resultado da pra fazer alguma coisa talvez."
    elif resultado >= 10:
        mensagem = "Você conseguiu um resultado ok."
    else:
        mensagem = "Poderia ser melhor..."
    
    print(f"Você rolou um d20 e tirou: {resultado}. {mensagem}")
    
    jogar_novamente = input("Quer rolar o dado novamente? (s/n): ").strip().lower()
    if jogar_novamente == 's':
        rolar_d20()
    else:
        print("Vlw, tenha um bom dia.")

rolar_d20()
