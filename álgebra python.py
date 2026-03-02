'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
from datetime import datetime

def calcular_metro():
    print("--- CALCULADORA DE OBRA: METRO DE BOGOTÁ ---")
    
    fecha_inicio = datetime(2021, 3, 15)
    
    fecha_entrega = datetime(2028, 3, 31)
    
    hoy = datetime.now()

    pasado = hoy - fecha_inicio
    faltante = fecha_entrega - hoy

    print(f"Fecha de hoy: {hoy.strftime('%d/%m/%Y')}")
    print("-" * 40)
    print(f"Días desde que inició la obra: {pasado.days} días")
    print(f"Días que faltan para la entrega: {faltante.days} días")
    
    total_dias = (fecha_entrega - fecha_inicio).days
    progreso = (pasado.days / total_dias) * 100
    print(f"Progreso temporal de la obra: {progreso:.2f}%")

if __name__ == "__main__":
    try:
        calcular_metro()
    except Exception as e:
        print(f"Hubo un error: {e}")