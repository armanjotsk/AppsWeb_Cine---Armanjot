#  CineVault - Proyecto Final Python + Flask - Armanjot Singh

**CineVault** es una aplicación web desarrollada en Python con el framework Flask y base de datos MySQL. Permite a los usuarios explorar un catálogo de cine clásico y registrarse para llevar un control de sus propias valoraciones en un panel privado.

**Autor:** Armanjot Singh Kaur  
**Módulo:** Implantacion de Aplicaciones Web (ASIX)  
**Curso:** 2025-2026  

---

## Funcionalidades Principales

Este proyecto cumple con todos los requisitos establecidos en la rúbrica de evaluación:
- **Parte Publica:** Catálogo visual de películas accesible sin necesidad de registro.
- **Autenticacion Segura:** Sistema de Registro y Login con contraseñas encriptadas mediante `Werkzeug`.
- **Parte Privada:** Panel de usuario (Mis Valoraciones) protegido por sesiones de Flask.
- **Formularios:** Tres formularios funcionales (Registro, Login y un tercer formulario para añadir valoraciones).
- **Base de Datos Relacional:** Uso de Claves Foráneas (`FOREIGN KEY`) en MySQL para enlazar cada reseña con su autor de forma exclusiva.
- **Portafolio Integrado:** Sección "About Me" con el listado de prácticas de Python que hemos ido haciendo.
- **Diseño Modular:** Uso de herencia de plantillas HTML (`base.html`).

---

## Tecnologías Utilizadas

- **Backend:** Python 3, Flask.
- **Frontend:** HTML5, CSS3 (Diseño propio responsivo usando Flexbox).
- **Base de Datos:** MySQL (XAMPP).
- **Seguridad:** `Werkzeug` (Hash de contraseñas).

---

## Instalación y Puesta en Marcha

Para desplegar este proyecto en un entorno local, seguimos  estos pasos:

### 1. Preparar la Base de Datos (XAMPP)
1. Iniciamos **Apache** y **MySQL** en el panel de XAMPP.
2. Accedemos a `http://localhost/phpmyadmin`.
3. Vamos a la pestaña **SQL** y ejecutamos el siguiente script para crear la base de datos y las tablas:

```sql
CREATE DATABASE IF NOT EXISTS projecte_cinema;
USE projecte_cinema;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

CREATE TABLE resenas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT NOT NULL,
    pelicula VARCHAR(150) NOT NULL,
    puntuacion INT NOT NULL,
    comentario TEXT NOT NULL,
    fecha DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id) ON DELETE CASCADE
);
```` 
Este script SQL inicializa la base de datos projecte_cinema y establece su estructura relacional mediante dos tablas principales.
La tabla usuarios gestiona el acceso seguro garantizando identificadores únicos y espacio suficiente para las contraseñas encriptadas. 
Por otro lado, la tabla resenas almacena el contenido y utiliza una Clave Foránea (FOREIGN KEY) con borrado en cascada (ON DELETE CASCADE) para vincular cada crítica exactamente con su creador, asegurando la integridad referencial y manteniendo el sistema limpio de datos huérfanos.

### 2. Runeamos el virtual enviroment para realizar el despliegue de este proyecto
1. Abrimos la terminal de VS Code:
2. Creamos entorno virtual `python -m venv venv`
3. Activamos el entorno `.\venv\Scripts\activate`

### 3. Instalamos la conexión con nuestra base de datos que se está ejecutando con el Xammp (apache y mysql activos)
1. En la terminal ponemos `pip install Flask mysql-connector-python Werkzeug`

### 4. Ahora nos queda ejecutar la applicacion
`python app.py`
Después de ejecutar nos aparecerá la ip localhost 127.0.0.1/5000 o con el puerto que le hayamos establecido a nuestro ficher app.py. Tambien se recomienda establecer el debug=on para no tener que ir guardando los cambios cada vez que modoificamos algun fichero.

### Estructura del protyecto:

```
APPSWEB_CINE-Armanjot/
│
├── static/
│   ├── imagenes/          # Pósters de las películas y favicon
│   └── styles.css         # Hoja de estilos principal
│
├── templates/
│   ├── base.html          # Plantilla padre con el menú de navegación
│   ├── index.html         # Catalogo público (parte pública)
│   ├── login.html         # Formulario de acceso
│   ├── register.html      # Formulario de creación de cuenta
│   ├── registro_correcto.html # Confirmación visual de registro
│   ├── sala_criticas.html # Panel privado (panel de comunidad y usuario)
│   ├── add_valoracion.html# Formulario para publicar reseñas (tercer formulario)
│   └── portfolio.html     # Seccion "About me" con prácticas anteriores
│
├── app.py                 # Codigo principal con flask
└── database.py            # Funciones de conexión, encriptación y consultas MySQL
```
