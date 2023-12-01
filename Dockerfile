# Obtener imagen base
FROM --platform=linux/amd64 python:3.11.0-slim-bullseye

# Definir varibales de entorno
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONNONBUFFERED 1

# Directorio
WORKDIR /code

# Instalar dependencias
COPY ./requerimientos.txt . 
RUN pip install -r requerimientos.txt

# Copiar proyecto
COPY . .
