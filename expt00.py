#Essa é uma varição de um execicio já feito anterior mente em outra lista de exercicios porem feito com uma função aqui.

#Aqui apenas criei uma função para fazer oque antes era mais complicado:
def fizzbuzz(n1):
    re1 = n1 % 3
    re2 = n1 % 5
    
    if re1 % 3 == 0 and re2 % 5 == 0:
        return("FizzBuzz")
    else:
        if re1 % 3 == 0:
            return("Fizz")
        else:
            if re2 % 5 == 0:
                return("Buzz")
            else:
                return(n1)
        
#Fim-se :D