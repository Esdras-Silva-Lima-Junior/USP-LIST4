# Aqui neste programa criei duas funções principais responsaveis por checar se o número inserido é primo ou não que é a função éPrimo e depois verificar qual é o número primo mais proximo do número digitado (ele só vai exibir o número primo anterior ao número digitado).

#Função usada para verificar se é primo:
def éPrimo(n):
    cont = 2
    cond = True
    while cond:
        if n == cont:
            cond = False
        else:
            if n < 2:
                cond = False
            else:
                if (n % cont == 0):
                    cond = False
                    return(False)
                else:
                    cont = cont + 1
    return True

#Função usada pora verificar qual é o número primo mais proximo:
def maior_primo(n):
    cond = True
    if n <= 2:
        return(2)
    else:
        while cond:
            if éPrimo(n) == True:
                x = n
                cond = False
            else:
                n = n - 1
    return(x)

#Abaixo os testes para verificar se o programa realmente está fazendo aquilo que desejo:
def test_primo_Big():
    assert maior_primo(957) == 953
    
def test_primo_negativo():
    assert maior_primo(-97) == 2
    
def test_primo_zero():
    assert maior_primo(0) == 2
    
def test_primo_minimo_igual():
    assert maior_primo(2) == 2

#Fim-se :D