# Crear un programa que solicite 5 notas a ingresar, dichas notas deberan agregarse en una lista
# El programa debe validar el ingreso de únicamente números, validando que en caso un dato numérico
# arroje un mensaje solicitando el ingreso de el dato correcto
# Una vez ingresadas las 5 notas el sistema arrojará en pantalla el promedio de todas las notas, la nota mayor y la nota menor
#=============================================================================================================================

lista = []
cant_notas = int(input("Ingrese cantidad de notas a registrar: "))

for i in range(cant_notas):
    while True:
        try:
            nota = float(input(f"Ingrese nota {i+1}: "))
            if (nota >= 0 and nota <=20):
                lista.append(nota)
                break  
            else:
                if nota > 0:
                    print("Solo puede ingresar notas de 0 a 20")
                else:
                    print("No puede digitar notas negativas, Intente nuevamente...")
        except Exception:
            print("Error...!! Intente nuevamente...")
        
#Resultado 
print("\n\t .:: Notas Registradas ::.")
print("===========================================")
print(lista)
print("\n\t .:: Promedio de Notas ::.")
print("===========================================")
print(sum(lista)/len(lista))
print("\n\t .:: Nota Mayor ::.")
print("===================================")
print(max(lista))
print("\n\t .:: Nota Menor ::.")
print("===================================")
print(min(lista))
