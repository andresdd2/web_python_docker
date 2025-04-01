# Usamos la imagen base de Python
FROM python:3.10

# Se establece el directorio de trabajo
WORKDIR /app

# Copiamos los archivos al contenedor
COPY app/ app/
COPY requirements.txt .

# Instalamos las dependencias
RUN pip --no-cache-dir install -r requirements.txt

# Exponemos el puerto
EXPOSE 5000

# Definimos el comando a ejecutar
CMD ["python", "app/main.py"]