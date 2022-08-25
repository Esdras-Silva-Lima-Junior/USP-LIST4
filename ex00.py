#Este programa  vai exibir qual é o maior número entre aqueles que o usuário digitar

#Função usada para tal tarefa:
def maximo(x, y):
    if x > y:
        return(x)
    else:
        return(y)
#Programa acaba aqui porem abaixo tem as funções que irão fazer os testes.        

def test_maximo_negativo():
    assert maximo(-1, -2) == -1
    
def test_maximo_zero():
    assert maximo(0, 0) == 0

def test_maximo():
    assert maximo(999, 999) == 999

#Fim-se :D