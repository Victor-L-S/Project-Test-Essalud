import calendar
from datetime import datetime

print('Registrate')
print("--------------------------------------------------------------------")

def telnumber():
    numcorrectos = False
    while(not numcorrectos):
        tel = input("Ingrese tu Número Telefónico: ")
        if tel.isnumeric():
            if len(tel) == 9:
                numcorrectos = True
            else:
                print("------------------------------------------------------------------")
                print("El Telefono debe contener 9 dígitos")
                print("------------------------------------------------------------------")
        else:
            print("------------------------------------------------------------------")
            print("Debe ingresar solo Números")
            print("------------------------------------------------------------------")

def dnicard():
    numcorrectos1 = False
    while(not numcorrectos1):
        dni = input("Ingrese su DNI: ")
        if dni.isnumeric():
            if len(dni) == 8:
                numcorrectos1 = True
            else:
                print("------------------------------------------------------------------")
                print("El DNI debe contener 8 dígitos")
                print("------------------------------------------------------------------")
        else:
            print("------------------------------------------------------------------")
            print("Debe ingresar solo Números")
            print("------------------------------------------------------------------")

def Registro():
    nombre = str(input("Ingrese su Nombre: "))
    apellido = str(input("Ingrese Apellidos completos: "))
    telnumber()
    dnicard()
    contra = str(input("Ingrese su Contraseña: "))
    conf_contra = str(input("Confirme su Contraseña: "))

    while contra != conf_contra:
        print("")
        print("La contraseña que ingreso no es válida, vuelva a intentarlo")
        print("")
        contra = str(input("Ingrese su Contraseña: "))
        conf_contra = str(input("Confirme su Contraseña: "))
    if contra == conf_contra:
        print("------------------------------------------------------------------")
        print("¡Se registró Correctamente!")
        print("------------------------------------------------------------------")

        def again():
            home = [
                "1 -Cita Virtual",
                "2 -Información Médica",
                "3 -Calendario",
            ]
            print("MENU: ")

            print("\n".join(map(str, home)))

            opcion = int(input("\nIngrese la opcion a elegir: \n"))

            if opcion == 1:
                print("Has seleccionado Cita virtual")
                print("")
                
                h_ahora = datetime.now()
                h_actual = datetime.strftime(h_ahora, '%d %b')
                Hora = str(input("Ingrese la hora: "))
                Fecha = str(input("Ingrese la fecha: "))

                print("")
                print("Los médicos disponibles son: ")

                Med_dispo = [
                    "Doc.Ana Perez",
                    "Doc.Pepe Aguilar",
                    "Doc.Benito Anastasio",
                    "Doc.Florencia Villalobos",
                    "Doc.Susana Horia",
                    "Doc.Carolina Herrera",
                    "Doc.Victor Prada",
                    "Doc.Cristina Cueva",
                ]

                print("\n".join(map(str,Med_dispo)))
                print()
                Medico = int(input("Ingrese la opcion del Doctor: "))

                if Medico == 1:
                    print(f'Has programado una cita el día: {h_actual} | para el: {Fecha} | a las: {Hora} con el {Med_dispo[0]}\n')
                if Medico == 2:
                    print(f'Has programado una cita el día: {h_actual} | para el: {Fecha} | a las: {Hora} con el {Med_dispo[1]}\n')
                if Medico == 3:
                    print(f'Has programado una cita el día: {h_actual} | para el: {Fecha} | a las: {Hora} con el {Med_dispo[2]}\n')
                if Medico == 4:
                    print(f'Has programado una cita el día: {h_actual} | para el: {Fecha} | a las: {Hora} con el {Med_dispo[3]}\n')
                if Medico == 5:
                    print(f'Has programado una cita el día: {h_actual} | para el: {Fecha} | a las: {Hora} con el {Med_dispo[4]}\n')
                if Medico == 6:
                    print(f'Has programado una cita el día: {h_actual} | para el: {Fecha} | a las: {Hora} con el {Med_dispo[5]}\n')
                if Medico == 7:
                    print(f'Has programado una cita el día: {h_actual} | para el: {Fecha} | a las: {Hora} con el {Med_dispo[6]}\n')
                if Medico == 8:
                    print(f'Has programado una cita el día: {h_actual} | para el: {Fecha} | a las: {Hora} con el {Med_dispo[7]}\n')
                elif Medico > 8 and Medico < 0:
                    print("Ingrese un Número Válido")
                again()

            if opcion == 2:
                print("\nHas seleccionado información sobre doctores")
                print("")
                medico= [
                        "1- Doc.Juan Perez",
                        "2- Doc.Pepe Aguilar",
                        "3- Doc.Rafael Anastasio",
                        "4- Doc. Eduardo Pampañaupa",
                        "5- Doc.Susana Horia",
                        "6- Doc.Alma Marcela",
                        "7- Doc. Carolina Herrera",
                        "8- Doc. Cristina Cueva",
                ]
                print("\n".join(map(str,medico)))
                opcion2 = int(input(("\nIngrese la opción: \n")))

                if opcion2 == 1:
                    print("\nDoctor.Juan Perez:\n47 años\nMedico general\nSe graduo en Maranguita,Piura(2010)\n22 años de experiencia\n")
                if opcion2 == 2:
                    print("\nDoc Pepe Aguilar:\n30 años\nMedico Cirujano\nSe graduo en la UNP(2015)\n7 años de experiencia\n")
                if opcion2 == 3:
                    print("\nDoc Rafael Anastasio:\n23 años\nPediatra\nSe graduo en Cesar Vallejo (2017)\n5 años de experiencia\n")
                if opcion2 == 4:
                    print("\nDoc.Eduardo Pampañaupa:\n50 años\nDermatologo\nSe graduo en la UNP(1992)\n20 años de experiencia\n")
                if opcion2 == 5:
                    print("\nDoc.Susana Horia:\n48 años\nNefrologo\nSe graduo en la UPAL(2020)\n2 años de experiencia\n")
                if opcion2 == 6:
                    print("\nDoc.Alma Marcela:\n50 años\nMedico General\nSe graduo en la UNP(2017)\n5 años de experiencia\n")
                if opcion2 == 7:
                    print("\nDoc.Carolina Herrera:\n50 años\nMedico General\nSe graduo en la UNP(2017)\n5 años de experiencia\n")
                if opcion2 == 8:
                    print("\nDoc.Cristina Cueva:\n50 años\nMedico General\nSe graduo en la UNP(2017)\n5 años de experiencia\n")
                elif opcion2 > 8 and opcion2 < 0:
                    print("Ingrese una opción válida")
                again()

            if opcion == 3:
                # print("\nHas seleccionado calendario")
                # print("")
                # citaA = datetime.now()
                # citaB = datetime.strftime(citaA, '%Y')
                # citaC = datetime.strftime(citaA, '%m')

                # a = int(citaB)
                # b = int(citaC)

                # print(calendar.month(a, b))
                calendario = calendar.TextCalendar(calendar.SUNDAY)
                print(calendario.formatyear(2022, 2, 1, 2, 3))
            again()

    else:
        print("------------------------------------------------------------------")
        print("Debe ingresar solo Números")
        print("------------------------------------------------------------------")

    again()
Registro()
