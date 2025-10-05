"""
Objetivo: Crear un menú interactivo con un bucle while para manipular una lista
de tareas de varias maneras.

Instrucciones:
Este es un administrador de tareas. Podrás ver tus tareas,
añadir nuevas, y marcar las que ya hiciste.

¡El programa no se detendrá hasta que elijas la opción de salir!
1. Añadir tarea
2. Ver tareas
3. Seleccionar tarea al azar
4. Marcar tarea como hecha
5. Tareas no hechas
6. Salir

El usuario usa el número de la opción como input
"""

import random


def main():
    tareas = []
    while True:
        opcion = int(input("Opción: "))
        if opcion == 6:
            break

        if opcion == 1:
            task_name = input("Tarea: ")
            task_tuple = (task_name, False)
            tareas.append(task_tuple)
        elif opcion == 2:
            print(tareas)
        elif opcion == 3:
            random_task = random.randint(0, len(tareas) - 1)
            print(tareas[random_task])
        elif opcion == 4:
            index_of_taks_to_remove = int(input("Tarea a remover: "))
            if index_of_taks_to_remove >= len(tareas):
                print("El indice no es valido")
                continue

            original_tuple = tareas[index_of_taks_to_remove]
            tareas[index_of_taks_to_remove] = (original_tuple[0], not original_tuple[1])
        elif opcion == 5:
            # not_done = []
            # for task in tareas:
            # task_name = task[0]
            # done = task[1]
            #    task_name, done = task
            #    if not done:
            #        not_done.append(task_name)
            # print(not_done)
            print([item[0] for item in tareas if item[1] == False])
        else:
            continue


main()
