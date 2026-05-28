# 🚀 Guía Interactiva de Programación Orientada a Objetos

> Plataforma educativa desarrollada con Flask para aprender Programación Orientada a Objetos (POO) mediante módulos interactivos, ejemplos prácticos y una interfaz moderna.

---

# 📖 Descripción General

## 🎯 Propósito del proyecto

Este proyecto tiene como objetivo ofrecer una guía interactiva y visual para el aprendizaje de Programación Orientada a Objetos (POO), utilizando Python y Flask como tecnologías principales.

La aplicación organiza el contenido en bloques temáticos que permiten al usuario aprender conceptos fundamentales de POO de forma progresiva, clara y práctica.

## ❗ Problema que resuelve

Muchos estudiantes encuentran difícil comprender Programación Orientada a Objetos únicamente mediante teoría o ejemplos aislados. Esta plataforma busca resolver ese problema mediante:

* Explicaciones organizadas por bloques.
* Navegación visual e intuitiva.
* Ejemplos prácticos.
* Diseño enfocado en aprendizaje progresivo.
* Separación modular del contenido.

## 👥 Público objetivo

Este proyecto está dirigido a:

* Estudiantes de programación.
* Personas que están aprendiendo Python.
* Docentes que desean material interactivo.
* Desarrolladores principiantes.
* Personas interesadas en aprender arquitectura modular con Flask.

---

# 📚 Tabla de Contenidos

* [📖 Descripción General](#-descripción-general)
* [⚙️ Instalación](#️-instalación)
* [🚀 Uso](#-uso)
* [🧠 Modo de Uso](#-modo-de-uso)
* [🏗 Arquitectura del Proyecto](#-arquitectura-del-proyecto)
* [✨ Funcionalidades Principales](#-funcionalidades-principales)
* [🔧 Configuración](#-configuración)
* [🤝 Contribución](#-contribución)
* [👨‍💻 Créditos / Autores](#-créditos--autores)
* [📎 Recursos Adicionales](#-recursos-adicionales)

---

# ⚙️ Instalación

## 📌 Requisitos Previos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

| Herramienta | Versión recomendada |
| ----------- | ------------------- |
| Python      | 3.10 o superior     |
| pip         | Última versión      |
| Flask       | 3.x                 |
| Git         | Opcional            |

## 📥 Clonar el repositorio

```bash
git clone https://github.com/DGrex/Guia-de-POO
cd "Guia-de-POO"
```

## 🧪 Crear entorno virtual

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 📦 Instalar dependencias

```bash
pip install -r requeriments.txt
```

## ▶️ Ejecutar el proyecto

```bash
python run.py
```

La aplicación estará disponible en:

```txt
http://127.0.0.1:5000
```

---

# 🚀 Uso

## ▶️ Ejecución básica

Una vez iniciado el servidor:

1. Abre tu navegador.
2. Ingresa a:

```txt
http://localhost:5000
```

3. Accede a los diferentes bloques educativos desde la interfaz principal.

## 💻 Ejemplo de ejecución

```bash
python run.py
```

## 🖼 Capturas o ejemplos visuales

Puedes agregar capturas dentro de una carpeta llamada `screenshots/`.

Ejemplo:

```md
![Inicio del sistema](screenshots/home.png)
```

## 🧩 Ejemplo de código del proyecto

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hola Mundo"
```

---

# 🧠 Modo de Uso

## 🔄 Flujo típico del usuario

### 1. Acceso al sistema

El usuario ingresa a la página principal donde se muestran tarjetas o módulos interactivos.

### 2. Selección de bloque

Cada bloque representa un tema específico relacionado con Programación Orientada a Objetos.

Ejemplos:

* Introducción a POO.
* Clases y objetos.
* Herencia.
* Encapsulamiento.
* Polimorfismo.
* Métodos.
* Constructores.

### 3. Navegación entre contenidos

El usuario puede desplazarse entre bloques y visualizar:

* Explicaciones.
* Ejemplos prácticos.
* Diagramas.
* Fragmentos de código.

### 4. Aprendizaje progresivo

La plataforma está diseñada para que cada bloque complemente el anterior.

---

## 🌐 Endpoints principales

| Endpoint   | Descripción      |
| ---------- | ---------------- |
| `/`        | Página principal |
| `/bloque0` | Primer bloque    |
| `/bloque1` | Segundo bloque   |
| `/bloque2` | Tercer bloque    |
| `/bloque3` | Cuarto bloque    |
| `/bloque4` | Quinto bloque    |
| `/bloque5` | Sexto bloque     |
| `/bloque6` | Séptimo bloque   |
| `/bloque7` | Octavo bloque    |
| `/bloque8` | Noveno bloque    |
| `/bloque9` | Décimo bloque    |

---

## ✅ Buenas prácticas de uso

* Seguir los bloques en orden.
* Revisar cada ejemplo de código.
* Probar modificaciones propias.
* Ejecutar el proyecto localmente para experimentar.
* Mantener el entorno virtual actualizado.

---

# 🏗 Arquitectura del Proyecto

## 📂 Estructura general

```txt
Guia de POO/
│
├── app/
│   ├── blueprints/
│   │   ├── bloque0/
│   │   ├── bloque1/
│   │   ├── bloque2/
│   │   └── ...
│   │
│   ├── templates/
│   ├── static/
│   ├── __init__.py
│   ├── routes.py
│   └── models.py
│
├── .venv/
├── run.py
├── requeriments.txt
└── README.md
```

## 🧱 Explicación de componentes

| Componente         | Descripción                                |
| ------------------ | ------------------------------------------ |
| `app/`             | Contiene la lógica principal del proyecto  |
| `blueprints/`      | Módulos organizados por bloques educativos |
| `templates/`       | Plantillas HTML                            |
| `static/`          | Recursos estáticos (CSS, JS, imágenes)     |
| `routes.py`        | Manejo de rutas principales                |
| `models.py`        | Modelos de datos                           |
| `run.py`           | Punto de entrada de la aplicación          |
| `requeriments.txt` | Dependencias del proyecto                  |

---

# ✨ Funcionalidades Principales

## 📘 Sistema modular de aprendizaje

Cada tema está separado en módulos independientes utilizando Blueprints de Flask.

## 🎨 Interfaz moderna e intuitiva

Diseño visual orientado al aprendizaje.

## 📚 Contenido educativo estructurado

El sistema organiza los conceptos de manera progresiva.

## 🔧 Arquitectura escalable

La separación modular permite agregar nuevos bloques fácilmente.

## 💡 Casos de uso

* Aprender POO desde cero.
* Utilizar como guía académica.
* Base para proyectos educativos.
* Referencia para aplicaciones Flask modulares.

---

# 🔧 Configuración

## 🌍 Variables de entorno

Puedes crear un archivo `.env`:

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta
```

## ⚙️ Configuración Flask

Ejemplo:

```python
app.config['SECRET_KEY'] = 'secret-key'
```

## 📁 Archivos importantes

| Archivo            | Función                |
| ------------------ | ---------------------- |
| `.env`             | Variables de entorno   |
| `run.py`           | Inicializa el servidor |
| `requeriments.txt` | Dependencias           |

---

# 🤝 Contribución

## 📌 Cómo contribuir

1. Haz un fork del proyecto.
2. Crea una rama nueva.
3. Realiza tus cambios.
4. Envía un Pull Request.

## 🧹 Estándares de código

* Utilizar nombres descriptivos.
* Mantener código modular.
* Seguir buenas prácticas de Python.
* Documentar funciones importantes.
* Mantener consistencia visual.

## 🧪 Buenas prácticas

```python
# Ejemplo de función documentada

def sumar(a: int, b: int) -> int:
    """Retorna la suma de dos números."""
    return a + b
```

---

# 👨‍💻 Créditos / Autores

## ✍️ Autores principales

**Denis Goyes**
* Desarrollador de Software
* Estudiante de Ingeniería

**Alex Gualli**
* Estudiante de Ingeniería

## 🌐 Contacto

* GitHub: `https://github.com/DGrex`*
* Email: `goyesdenis14@gmail.com`

---

# 📎 Recursos Adicionales

## 📚 Documentación oficial

* Flask → [https://flask.palletsprojects.com/](https://flask.palletsprojects.com/)
* Python → [https://www.python.org/](https://www.python.org/)
* Jinja2 → [https://jinja.palletsprojects.com/](https://jinja.palletsprojects.com/)

## 🎓 Recursos educativos

* Programación Orientada a Objetos en Python.
* Arquitectura modular con Flask.
* Blueprints en Flask.

## 🔗 Referencias útiles

* [https://realpython.com/](https://realpython.com/)
* [https://www.freecodecamp.org/](https://www.freecodecamp.org/)
* [https://developer.mozilla.org/](https://developer.mozilla.org/)

---

# ⭐ Recomendación Final

Si este proyecto te resulta útil:

* Dale una ⭐ al repositorio.
* Comparte el proyecto.
* Contribuye con mejoras.
* Utilízalo como guía de aprendizaje.

---

# 📌 Estado del Proyecto

✅ En desarrollo activo.
