#Quiz 3
#E: numero
#S: lista con los numeros pero separados por una coma donde hay 0s
#R: -

def partir(num):
    if not isinstance(num,int):
        return "Error"
    else:
        return partir_aux(abs(num), 0, 0, [])

def partir_aux(num, temp, exp, result):
    if num == 0:
        if temp != 0:
            return [temp] + result
        else:
            return result
    elif num%10==0:
        if temp != 0:
            return partir_aux(num // 10, 0, 0, [temp] + result)
        else:
            return partir_aux(num // 10, 0, 0, result)            
    else:
        return partir_aux(num // 10, temp + ((num % 10) * (10 ** exp)), exp +1, result)

print("Quiz 3:")
print("partir(123029201034)  Correcto: [123,292,1,34] Retorna: ",partir(123029201034))
print("partir(89762931)      Correcto: [89762931]     Retorna: ",partir(89762931))
print("partir(120)           Correcto: [12]           Retorna: ",partir(120))
print("partir(120000)        Correcto: [12]           Retorna: ",partir(120000))
print("partir(1200045)       Correcto: [12, 45]       Retorna: ",partir(1200045))
print("partir(0)             Correcto: []             Retorna: ",partir(0))
