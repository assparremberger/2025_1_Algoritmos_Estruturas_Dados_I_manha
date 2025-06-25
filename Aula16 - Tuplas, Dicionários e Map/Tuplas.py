carros = "Twingo" , "Del Rey", "Corolla"

print( carros[-1:] )

def calcular(x, y):
    return x+y , x-y , x*y , x/y

resultado = calcular( 10 , 5 )
print(resultado)

for r in resultado:
    print( r )

a, b, c, d = resultado
print( "Soma: " , a)
print( "Subtração: " , b)
print( "Multiplicação: " , c)
print( "Divisão: " , d)





