#Este programa é bem longo, ele irá verificar qual é o maior número entre aqueles que o usúario inserir e mostrar aquele que é o maior número:

#Nâo tem muito ue se falar dessa função, apenas um monte de condicionais com "return" dentro:
def maximo(a, b, c):
    if a == b and a == c:
        return(a)
    else:
        if a == b and a > c:
            return(a)
        else:
            if b == c and b > a:
                return(b)
            else:
                if c == a and c > b:
                    return(c)
                else:
                    if a == b and a < c:
                        return(c)
                    else:
                        if b == c and b < a:
                            return(a)
                        else:
                            if c == a and c < b:
                                return(b)
                            else:   
                                if a > b and a > c:
                                    return(a)
                                else:
                                    if b > a and b > c:
                                        return(b)
                                    else:
                                        if c > b and c > a:
                                            return(c)

#Fim-se :D