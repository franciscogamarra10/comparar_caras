# Face Match App: Sistema de Reconocimiento Facial

Este proyecto permite comparar dos imágenes para verificar si pertenecen a la misma persona utilizando el reconocimiento facial. Además, proporciona una funcionalidad para verificar si dos personas (del mismo sexo) se parecen. Esta aplicación está diseñada principalmente para mostrar la facilidad de la puesta en producción del modelo de detección en **Render** y/o **Fly.io**. El proyecto está estructurado de manera que será fácil de implementar.

Aunque el propósito principal de esta aplicación es educativo, el concepto de reconocimiento facial se puede generalizar para ser utilizado en diversos sistemas como **asistencia**, **seguridad** o **autenticación**, donde se necesita verificar la identidad de una persona mediante su rostro.

## Requisitos

### Requisitos de software

Este proyecto requiere las siguientes dependencias para funcionar correctamente:

- **Python 3.8** (recomendado para `face-recognition`)
- **Flask**: Framework web ligero.
- **dlib** y **face-recognition**: Bibliotecas de Python para el reconocimiento facial.
- **gunicorn**: Servidor WSGI para producción.

Para instalar las dependencias, simplemente ejecuta:
El archivo requirements.txt contiene todas las dependencias necesarias para ejecutar la aplicación correctamente.
```bash
pip install -r requirements.txt

```
Instrucciones de uso
Usar Docker (recomendado)
Si prefieres usar Docker para ejecutar la aplicación (lo recomendado para producción y despliegue en Render o Fly.io), asegúrate de tener Docker instalado en tu máquina. Luego, simplemente ejecuta los siguientes comandos:

```bash

docker build -t face-match-app .
docker run -p 5000:5000 face-match-app
```
Esto construirá y ejecutará la aplicación en un contenedor Docker en el puerto 5000.

## Despliegue en Fly.io o Render
Aunque la aplicación puede ejecutarse localmente, se recomienda usar plataformas de despliegue como Fly.io o Render para producción. Estas plataformas te permiten desplegar tu aplicación de manera sencilla y con alta disponibilidad.

## Despliegue sin Docker
Si no deseas usar Docker, también puedes seguir las instrucciones de despliegue para Fly.io o Render sin contenerizar la aplicación.

## Licencia
Este proyecto está licenciado bajo la Licencia MIT
