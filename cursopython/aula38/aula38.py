# Listas 

secreto = 'Perfume'
digitadas = []
chances = 3

while True:
    letra = input('Digite uma letra: ')
    
    if len(letra) > 1:
        print('Ahhhh isso nao vale, digite apenas  uma letra.')
        continue
    
    digitadas.append(letra)  # Adiciona um novo elemento na lista
    
    if letra in secreto:
        print(f'UHUUUL, a letra "{letra}" existe na palavra secreta.')
    else:
        print(f'AFFFZZZ a letra {letra} nao existe na palavra secreta.')
        digitadas.pop()  # Remover o ultimo elemento da lista
        chances -= 1
        print(f'Voce tem {chances} restantes')

    secreto_temporario = ''    
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '*'
    
    if secreto_temporario == secreto:
        print(f'Que legal, voce ganhou!!!! A palavra era {secreto_temporario} ')
        break
    else:
        print(f'A palavra secreta esta assim: {secreto_temporario}')
    
    if chances == 0:
        print('Acabaram as suas chances')
        break

        
    
