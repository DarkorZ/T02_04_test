# 🛒 Sistema de Gestión de Minimercado – FastAPI

Este proyecto corresponde al desarrollo de una **API REST para la gestión de un minimercado**, implementada como parte de la **Tarea T02.03** y extendida con **pruebas unitarias (T02.04)** de la carrera de Ingeniería de Software – Universidad Politécnica Salesiana.

La aplicación permite administrar productos, controlar inventario y registrar ventas, siguiendo una arquitectura organizada basada en **controladores, servicios, repositorios y modelos**.

---

## 🚀 Tecnologías Utilizadas

- **Python 3.10**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **Pytest**
- **Coverage.py (pytest-cov)**

---

## 📂 Estructura del Proyecto

-T02_03_minimercado
├── app
│ ├── controllers
│ ├── models
│ ├── repositories
│ ├── services
│ ├── init.py
│ └── main.py
├── tests
│ ├── conftest.py
│ ├── test_catalogo.py
│ ├── test_inventario.py
│ └── test_ventas.py
├── requirements.txt
├── README.md
└── .gitignore


---

## 🧪 Entorno Virtual (Recomendado)

Para garantizar la correcta ejecución del proyecto y evitar conflictos entre dependencias, se recomienda el uso de un **entorno virtual de Python**.

### 1️⃣ Crear entorno virtual

Desde la raíz del proyecto:

```bash
python -m venv venv


2️⃣ Activar entorno virtual

Windows

venv\Scripts\activate

Al activarlo, la consola mostrará:

(venv)

Ejecución del Proyecto
1️⃣ Instalar dependencias del proyecto

Con el entorno virtual activado:

pip install -r requirements.txt

Ejecutar la aplicación

Desde la raíz del proyecto:

uvicorn app.main:app --reload

Abrir en el navegador:

http://127.0.0.1:8000/docs



Testing con Pytest (T02.04)

git clone https://github.com/josephTc2003/-T02_03_minimercado.git
cd -T02_03_minimercado

Archivo .gitignore

venv/
__pycache__/
.pytest_cache/
htmlcov/
.env

Instalación de dependencias para testing

Con el entorno virtual activado:

pip install pytest pytest-cov httpx


Ejecutar pruebas unitarias

Desde la raíz del proyecto:

pytest

Ejecutar análisis de cobertura
pytest --cov=app --cov-report=term-missing

❌ ModuleNotFoundError: No module named 'fastapi'

Causa:
FastAPI no estaba instalada en el entorno virtual activo.

Solución:

pip install -r requirements.txt

❌ ModuleNotFoundError: No module named 'httpx'

Causa:
La librería httpx no estaba instalada. Es utilizada por TestClient de FastAPI para ejecutar pruebas sin levantar el servidor.

Solución:

pip install httpx

❌ Error al ejecutar Uvicorn desde la carpeta incorrecta

Causa:
El servidor fue ejecutado desde la carpeta app/.

Solución correcta:

uvicorn app.main:app --reload

❌ Pytest no mide cobertura

Causa:
La librería pytest-cov no estaba instalada.

Solución:

pip install pytest-cov
pytest --cov=app --cov-report=term-missing


