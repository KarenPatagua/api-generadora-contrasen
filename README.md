# 🔐 Generador de Contraseñas Seguras (Python + Flask + Docker)

Este proyecto es una aplicación web simple desarrollada con **Python** y **Flask** que genera contraseñas aleatorias cada vez que se accede a la página principal. Está contenerizado usando **Docker** para que puedas ejecutarlo fácilmente en cualquier entorno.

---

## 📋 Requisitos

- Tener instalado [Docker](https://www.docker.com/)
- Tener instalado [Git](https://git-scm.com/) para clonar el repositorio (opcional)
- Conexión a internet para descargar la imagen base

---

## 🚀 Instrucciones de uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/KarenPatagua/api-generadora-contrasen.git
cd api-generadora-contrasen
```

> 💡 Reemplazá la URL con la de tu propio repositorio.

---

### 2. Construir la imagen de Docker

```bash
docker build -t generador-password .
```

---

### 3. Ejecutar el contenedor

```bash
docker run -p 5000:5000 generador-password
```

---

### 4. Ver la aplicación

Abrí tu navegador en [http://localhost:5000](http://localhost:5000)

Deberías ver una contraseña generada automáticamente cada vez que recargues la página.

---

## 📦 Imagen base utilizada

Este proyecto utiliza la imagen oficial de **Python 3.11** desde Docker Hub:

```dockerfile
FROM python:3.11
```

---

## 🗂 Estructura del proyecto

```
/api-generadora-contrasen
│
├── app.py
├── requirements.txt
├── Dockerfile
├── style.css
├── README.md
└── templates
    └── index.html


---

## 📌 Detalles adicionales

- El puerto expuesto por Flask es el **5000**
- Se utiliza `Flask` como microframework
- El contenedor puede ser reutilizado en otros entornos fácilmente

---


