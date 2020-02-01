try:
    y=1/0
except ArithmeticError:
        print("Problema aritmetico")
except ZeroDivisionError:
    print("zero division")
print("the end")

### funcion divertida
def badFun(n):
    try:

        return 1/n
    except ArithmeticError:
        print("Problema aritmetico")
    return None
badFun(2)
print("the end")

######### laboratorio
def validarNumero(prompt, min, max):
    while (True):
        try:
            x = int(input(prompt))
            assert x >= min and x <= max
            return x
            break
        except ValueError:
            print("Ingresar solo numeros")
        except:
            print("El valor debe estar dentro del RANGO --> (-10..10) <--")
    
v = validarNumero("Ingrese un valor desde -10 a 10:", -10, 10)

print("El número es:", v)