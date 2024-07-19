FROM python:3.10.11

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar el resto de los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias
RUN pip install -r requirements.txt

# Exponer el puerto 4000
EXPOSE 4000

# Comando para ejecutar la aplicación
CMD ["python", "app_record.py"]
