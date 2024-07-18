# Recordmendation_DataEngineering

Recordmendation es una aplicación de IA generativa que permite a los usuarios descubrir nuevas canciones basadas en sus preferencias musicales. El nombre combina "record" (disco musical) y "recommendation" (recomendación), reflejando su funcionalidad principal: recomendar música a los usuarios.


## Descripción del Proyecto
Este proyecto utiliza un modelo de lenguaje avanzado para generar recomendaciones musicales personalizadas. Los usuarios interactúan con la aplicación proporcionando el nombre de una canción y su intérprete, y a cambio reciben una lista de 5 canciones recomendadas que podrían gustarles, basadas en el input inicial.


## Estructura
    • app_record.py: código para la aplicación, guardando los datos de entrada y la respuesta en AWS

    • app.py: código para la aplicación, sin guardar datos

    • BasedeDatos.ipynb: notebook para creación de base de datos en AWS y para poder revisar ingesta de datos

    • dockerfile: archivo docker para correr la app en Docker

    • requirements.txt : requerimientos para uso de la app

    • index.hmtl: archivo de estructura de página web

    • test_app.py: código para probar la app

    • static: carpeta para imágenes utilizadas en el proyecto y en el README


## Instalación a través de Docker
  1. Descarga la imagen desde Docker Hub: 
       docker pull nataliojpg/recordmendation
     
  2. Ejecuta el contenedor:
       docker run -p 4000:4000 nataliojpg/recordmendation


## Uso
  1. Accede a la interfaz web en http://localhost:4000 en el navegador.

  2. Ingresa el nombre de una canción y su intérprete en los campos.

  3. Envía el formulario y espera las recomendaciones generadas por el modelo de IA.


## Herramientas
   • Python
   
   • FastApi
   
   • MySQL
   
   • Uvicorn
   
   • OpenAI
   
   • Docker
   
   • HTML
   
