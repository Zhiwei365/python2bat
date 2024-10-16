def CalcularNotaAcceso(notaBachillerato, notaFaseGeneral):
    notaAcceso = 0.6*notaBachillerato + 0.4*notaFaseGeneral
    return notaAcceso

def CalcularNotaAdmisión(notaAcceso, m1, m2, a, b):
    notaAdmisión = notaAcceso + m1*a + m2*b
    return notaAdmisión

notaBachillerato = float(input("nota bachillarato"))
notaFaseGeneral = float(input("nota fase general"))

notaAcceso = CalcularNotaAcceso(notaBachillerato, notaFaseGeneral)
print(f"Tu nota de acceso es {notaAcceso}")
m1 = float(input("nota materia especifica 1"))
m2 = float(input("nota materia especifica 2"))
a = float(input("coeficiente ponderación materia 1"))
b = float(input("coeficiente ponderación materia 2"))

notaAdmisión = CalcularNotaAdmisión(notaAcceso, m1, m2, a, b)

print(f"tu nota de admisión es {notaAdmisión}")