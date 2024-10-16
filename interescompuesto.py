def CalcularIntereses(p,r,t,n) :
    A = p*(1+r/n) **(n*t)
    return A
p = float(input("capital inicial"))
r = float(input("interés anual en porcentaje"))
t = float(input("número de año"))
n = float(input("n° de periodo por año") )
capitalfinal = CalcularIntereses(p,r,t,n)
print(f"la cantidad final después de 1 de años será {capitalfinal}")