def somar( valores ):
    soma = 0
    for x in valores:
        soma += x
    return soma

values = [10, 20, 30]   , ( 5, 15, 25, 35) , [ 1 , 5]

result = map( somar  ,  values  )
print( list(result) )