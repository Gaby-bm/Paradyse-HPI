import time

# Define la función
def bienvenida():
    print("Bienvenido al Asistente Educativo de Votación.")
    print("Este programa te ayudará a informarte sobre temas importantes relacionados con las elecciones.")
    print("A continuación, responderás algunas preguntas informativas para reflexionar sobre el proceso de votación.")
    print("Este test no limita tu derecho a votar; su objetivo es educativo.")
    print("¡Comencemos!\n")

# Preguntas educativas sobre el proceso electoral
def cuestionario():
    preguntas = [
        {
            "pregunta": "¿Por qué es importante participar en las elecciones?",
            "opciones": ["a) Porque todos los votos cuentan", "b) Porque votar es un derecho y un deber", "c) Porque el voto influye en decisiones futuras", "d) Todas las anteriores"],
            "respuesta": "d"
        },
        {
            "pregunta": "¿Qué significa votar de forma informada?",
            "opciones": ["a) Conocer las propuestas de cada candidato", "b) Investigar los antecedentes de cada candidato", "c) Entender cómo las políticas propuestas afectarán a la comunidad", "d) Todas las anteriores"],
            "respuesta": "d"
        },
        {
            "pregunta": "¿Es correcto votar basándote en información no verificada o rumores?",
            "opciones": ["a) Sí", "b) No"],
            "respuesta": "b"
        },
        {
            "pregunta": "¿Es tu voto anónimo y protegido por ley en las elecciones democráticas?",
            "opciones": ["a) Sí", "b) No"],
            "respuesta": "a"
        }
    ]
    
    correctas = 0
    
    for i, pregunta in enumerate(preguntas):
        print(f"\nPregunta {i + 1}: {pregunta['pregunta']}")
        for opcion in pregunta["opciones"]:
            print(opcion)
        respuesta = input("Escribe la letra de tu respuesta: ").strip().lower()
        
        if respuesta == pregunta["respuesta"]:
            print("¡Correcto!")
            correctas += 1
        else:
            print("Incorrecto. La respuesta correcta es:", pregunta["respuesta"].upper())
        time.sleep(1)

    print(f"\nHas respondido correctamente {correctas} de {len(preguntas)} preguntas.")
    print("Recuerda que la información es poder. Investiga y vota de forma informada.")

# Función principal
def main():
    bienvenida()
    cuestionario()
    print("\nGracias por utilizar el Asistente Educativo de Votación. ¡Tu voto informado es valioso!")

# Ejecución del programa
if __name__ == "__main__":
    main()