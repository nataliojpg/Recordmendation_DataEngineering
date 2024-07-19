from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import uvicorn
import openai
import pymysql
from langchain_core.prompts import PromptTemplate

app = FastAPI()

# Directorio de archivos (fondo de la web)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configurar tu clave de API de OpenAI
api_key1 = "tu-api-key"  
openai.api_key = api_key1

# Prompt Template
prompt_template = PromptTemplate.from_template(
    "Recomiéndame 5 canciones que sean similares a {cancion} de {artista},  y que no sean covers de {artista}. Dame las recomendaciones en una lista ordenada."
)


# Conectar con la base de datos
DB_CONFIG = {
    'host': 'datos-api-record.cp2aaumeq6eu.eu-north-1.rds.amazonaws.com',
    'port': 3306,
    'user': 'admin',
    'password': '12345678',
    'database': 'query_songs',
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def execute_insert_query(query, params):
    connection = pymysql.connect(**DB_CONFIG)
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, params)
        connection.commit()
    finally:
        connection.close()


# Inicio
@app.get("/")
async def hallo():
    return FileResponse("index.html")



# Endpoint para generar recomendación de música
@app.post("/recommend")
async def recommend_music(request: Request):
    data = await request.json()
    cancion = data.get('cancion')
    artista = data.get('artista')
    
    if not cancion or not artista:
            raise HTTPException(status_code=400, detail="Es necesario poner la canción y el artista.")
    
    try:
        prompt = prompt_template.format(cancion=cancion, artista=artista)
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
        {
            "role": "user",
            "content": prompt,
        }])
        
        recom = response.choices[0].message.content
        
        # Insertar datos en la base de datos
        insert_query = "INSERT INTO query_responses (song, artist, response) VALUES (%s, %s, %s)"
        insert_params = (cancion, artista, recom)
        execute_insert_query(insert_query, insert_params)

        return {"recommendations": response.choices[0].message.content}
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Fin
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)