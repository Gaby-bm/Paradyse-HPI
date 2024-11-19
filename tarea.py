import time
import random #importamos los módulos

# Función de bienvenida
def bienvenida():
    print("Bienvenido al Asistente Educativo de Votación.")
    print("Este programa evaluará tus conocimientos sobre el proceso electoral.")
    print("Si obtienes un puntaje suficiente, podrás votar. Si no, recibirás recomendaciones para mejorar.")
    print("¡Comencemos!\n")#en sí la bienvenida es modificable
    time.sleep(2)#hace que el programa se detenga dos segundos antes de continuar

# Función para mostrar una barra de progreso simulada
def barra_progreso(progreso, total):
    porcentaje = (progreso / total) * 100
    barra = f"[{'#' * int(porcentaje // 5)}{'-' * (20 - int(porcentaje // 5))}]"
    print(f"\rProgreso: {barra} {int(porcentaje)}%", end="", flush=True)
    
#' * int(porcentaje // 5):
#El porcentaje se divide por 5 (porque la barra tiene 20 posiciones fijas, y 100/20 = 5).
#El resultado entero (int) indica cuántos # llenar en la barra.
#Por ejemplo, si el progreso es del 50%, porcentaje // 5 será 10, y se imprimirán 10 #.
#'-' * (20 - int(porcentaje // 5)):

#Calcula el número restante de espacios en la barra (los que no están llenos de #).
#Si la barra tiene 20 posiciones y se llenaron 10 con #, se imprimirán 10 -.
#Resultado de barra:

#La barra completa tiene un formato como este: [#####----------].
#La cantidad de # y - cambia según el porcentaje calculado

# Función del cuestionario
def cuestionario():#modificar preguntasy respuestas
    preguntas = [
        {
            "pregunta": "¿Por qué es importante participar en las elecciones?",
            "opciones": ["a) Porque todos los votos cuentan", "b) Porque votar es un derecho y un deber", "c) Porque el voto influye en decisiones futuras", "d) Todas las anteriores"],
            "respuesta": "d",
            "ponderacion": 2  # Respuesta correcta vale 2 puntos
        },
        {
            "pregunta": "¿Qué significa votar de forma informada?",
            "opciones": ["a) Conocer las propuestas de cada candidato", "b) Investigar los antecedentes de cada candidato", "c) Entender cómo las políticas propuestas afectarán a la comunidad", "d) Todas las anteriores"],
            "respuesta": "d",
            "ponderacion": 2
        },
        {
            "pregunta": "¿Es correcto votar basándote en información no verificada o rumores?",
            "opciones": ["a) Sí", "b) No"],
            "respuesta": "b",
            "ponderacion": 1
        },
        {
            "pregunta": "¿Es tu voto anónimo y protegido por ley en las elecciones democráticas?",
            "opciones": ["a) Sí", "b) No"],
            "respuesta": "a",
            "ponderacion": 1
        },
        {
            "pregunta": "Selecciona un beneficio de la democracia:",
            "opciones": ["a) Libertad de expresión", "b) Igualdad ante la ley", "c) Oportunidad de elegir a los líderes", "d) Todas las anteriores"],
            "respuesta": "d",
            "ponderacion": 3
        },
        {
            "pregunta": "Completa: En una democracia, el poder reside en ____.",
            "opciones": ["a) el gobierno", "b) los ciudadanos", "c) los medios de comunicación", "d) los partidos políticos"],
            "respuesta": "b",
            "ponderacion": 2
        }
    ]

    # Contadores de desempeño
    correctas = 0
    puntaje_total = 0
    puntaje_obtenido = 0

    print("El cuestionario consta de 6 preguntas. Lee cuidadosamente y responde.")
    time.sleep(2)
    
    for i, pregunta in enumerate(preguntas):
        print(f"\nPregunta {i + 1}: {pregunta['pregunta']}")
        for opcion in pregunta["opciones"]:
            print(opcion)
        
#f"\nPregunta {i + 1}": Muestra el número de la pregunta sumando 1 a i (porque los índices empiezan desde 0).
#pregunta['pregunta']: Accede al texto de la pregunta desde el diccionario.
#for opcion in pregunta["opciones"]: Recorre y muestra cada opción de respuesta contenida en la lista pregunta["opciones"].

        inicio_respuesta = time.time()  # Captura el inicio de la respuesta
        respuesta = input("Escribe la letra de tu respuesta: ").strip().lower()
        tiempo_respuesta = time.time() - inicio_respuesta  # Tiempo que tardó en responder
        
        if respuesta == pregunta["respuesta"]:
            print(f"¡Correcto! (+{pregunta['ponderacion']} puntos)")
            correctas += 1
            puntaje_obtenido += pregunta["ponderacion"]
        else:
            print(f"Incorrecto. La respuesta correcta era: {pregunta['respuesta'].upper()}. (+0 puntos)")

        print(f"Tiempo tomado: {tiempo_respuesta:.2f} segundos.")
        puntaje_total += pregunta["ponderacion"]
        time.sleep(1)
        
        # Muestra la barra de progreso
        barra_progreso(i + 1, len(preguntas))

    print("\n\nEvaluación completada.")
    time.sleep(1)

    #Itera sobre las preguntas y captura la interacción del usuario.
    #Evalúa las respuestas, registra puntajes y tiempos.
    #Proporciona retroalimentación inmediata (correcto/incorrecto).
    #Muestra el progreso del cuestionario.

    print(f"Respuestas correctas: {correctas}/{len(preguntas)}")
    print(f"Puntaje obtenido: {puntaje_obtenido}/{puntaje_total}")
    
    # Feedback basado en el desempeño
    if puntaje_obtenido >= (0.7 * puntaje_total):  # 70% o más para aprobar
        print("\n¡Felicidades! Tienes los conocimientos necesarios para votar.")
    else:
        print("\nNo alcanzaste el puntaje necesario para votar.")
        print("Recomendamos revisar información sobre el proceso electoral y la importancia del voto informado.")
        print("Visita sitios web confiables o consulta con especialistas en educación cívica.")

# Función para cerrar el programa
def despedida():
    print("\nGracias por usar el Asistente Educativo de Votación.")
    print("Recuerda que un voto informado es un voto poderoso.")
    print("¡Hasta la próxima!")
    time.sleep(2)

# Función principal
def main():
    bienvenida()
    cuestionario()
    despedida()

# Ejecución del programa
if __name__ == "__main__":
    main()
