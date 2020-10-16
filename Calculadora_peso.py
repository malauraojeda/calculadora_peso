#Primero se piden la información necesaria para realizar la formula
def usuario():
    edad = int(input('Cual es su edad: '))
    genero = input('Cual es su genero (hombre o mujer): ')
    peso = int(input('Cuanto en pesa en kg: '))
    altura = int(input('Cual es su altura en cm: '))

    if genero == 'hombre':
        n1 = 66.5
        p = 13.75 * peso
        at = 5.003 * altura
        e = 6.77 * edad
    elif genero == 'mujer':
        n1 = 655.1
        p = 9.56 * peso
        at = 1.85 * altura
        e = 4.68 * edad

    #GEB mujer= 665 + (9.56 x p) + (1.85 x cm) – (4.7 x anios)
    #GEB hombre = 66 + (13.75 x p) + (5.003 x cm) - (6.77 x anios)
    GEB_resultado = n1 + at + p - e
    return(int(GEB_resultado))

def calcular_actividad(GEB_resultado): 
    actividad_nivel = input('Cual es su actividad normalmente (liviano, moderado, pesado, o extremo): ')

    if actividad_nivel == 'liviano':
        actividad_nivel = (30 * GEB_resultado /100) + GEB_resultado
    elif actividad_nivel == 'moderado':
        actividad_nivel = (50 * GEB_resultado /100) + GEB_resultado
    elif actividad_nivel == 'pesado':
        actividad_nivel = (75 * GEB_resultado /100) + GEB_resultado
    elif actividad_nivel == 'extremo':
        actividad_nivel = (100 * GEB_resultado /100) + GEB_resultado

    return(int(actividad_nivel))


def ganar_o_perder(actividad_nivel):
    meta = input('Quiere perder, mantener, o ganar peso: ')

    if meta == 'perder':
        kcal = actividad_nivel - 500
    elif meta == 'mantener':
        kcal = actividad_nivel
    elif meta == 'ganar':
        ganar_peso = int(input('''Ganar 500 gr o 1 kg por semana?/n
Si elige 500 gr escriba 1 
Si elige 1 kg escriba 2 '''))
        if ganar_peso == 1: 
            kcal = actividad_nivel + 500
        elif ganar_peso == 2:
            kcal = actividad_nivel + 1000

    print('en orden de ', meta, 'peso, su consumo diario de calorias deberia ser de', int(kcal), '!')


ganar_o_perder(calcular_actividad(usuario()))