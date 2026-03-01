# Importamos Flask y sus herramientas
from flask import Flask, render_template, request, redirect, url_for, session
import database

app = Flask(__name__)
app.secret_key = 'cinevault_secret_key_2526'

# ============================================================
# ZONA PÚBLICA
# ============================================================

@app.route('/')
def inicio():
    peliculas = [
        {
            "titulo": "El Padrino (1972)",
            "director": "Francis Ford Coppola",
            "genero": "Drama / Crimen",
            "sinopsis": "La saga de los Corleone: una familia mafiosa que lucha por mantener su poder en la Nueva York de los años 40. Marlon Brando y Al Pacino protagonizan una de las obras maestras absolutas del cine.",
            "imagen": "imagenes/godfather.jpg"
        },
        {
            "titulo": "Pulp Fiction (1994)",
            "director": "Quentin Tarantino",
            "genero": "Crimen / Neo-noir",
            "sinopsis": "Las vidas de dos sicarios, un boxeador y la esposa de un gángster se cruzan en esta obra maestra de narrativa no lineal que revolucionó el cine independiente de los 90.",
            "imagen": "imagenes/pulpfiction.jpg"
        },
        {
            "titulo": "El Señor de los Anillos: El Retorno del Rey (2003)",
            "director": "Peter Jackson",
            "genero": "Fantasía épica",
            "sinopsis": "La batalla final por la Tierra Media. Frodo y Sam se acercan al Monte del Destino mientras el ejército de Aragorn planta cara a las huestes de Sauron en los campos de Pelennor.",
            "imagen": "imagenes/lotr.jpg"
        },
        {
            "titulo": "El Caballero Oscuro (2008)",
            "director": "Christopher Nolan",
            "genero": "Acción / Superhéroes",
            "sinopsis": "Batman se enfrenta al Joker, un agente del caos sin motivaciones claras, en una batalla filosófica sobre el orden, la ética y los límites de la justicia en Gotham City.",
            "imagen": "imagenes/darkknight.jpg"
        },
        {
            "titulo": "Origen (2010)",
            "director": "Christopher Nolan",
            "genero": "Ciencia ficción / Thriller",
            "sinopsis": "Dom Cobb es un ladrón especializado en infiltrarse en los sueños de otros para robar secretos del subconsciente. Ahora le proponen la tarea inversa: plantar una idea.",
            "imagen": "imagenes/inception.jpg"
        },
        {
            "titulo": "Parásitos (2019)",
            "director": "Bong Joon-ho",
            "genero": "Drama / Thriller",
            "sinopsis": "Una familia de clase baja se infiltra en la vida de una familia adinerada mediante el engaño. Primera película no anglófona en ganar el Óscar a Mejor Película.",
            "imagen": "imagenes/parasite.jpg"
        },
        {
            "titulo": "Interestelar (2014)",
            "director": "Christopher Nolan",
            "genero": "Ciencia ficción",
            "sinopsis": "Un equipo de exploradores viaja a través de un agujero de gusano en busca de un nuevo hogar para la humanidad mientras la Tierra se acerca a su extinción.",
            "imagen": "imagenes/interstellar.jpg"
        },
        {
            "titulo": "Oppenheimer (2023)",
            "director": "Christopher Nolan",
            "genero": "Drama histórico / Biopic",
            "sinopsis": "La historia de J. Robert Oppenheimer y el Proyecto Manhattan: la creación de la bomba atómica y las consecuencias morales que perseguirían para siempre a su creador.",
            "imagen": "imagenes/oppenheimer.jpg"
        }
    ]
    return render_template('index.html', peliculas=peliculas)


@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


# ============================================================
# FORMULARIO 1 — REGISTRO
# ============================================================

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        user = request.form['username']
        pwd  = request.form['password']
        if database.registrar_usuario(user, pwd):
            return redirect(url_for('registro_correcto'))
        else:
            return render_template('register.html', error="El usuario ya existe.")
    return render_template('register.html')


@app.route('/registro_correcto')
def registro_correcto():
    return render_template('registro_correcto.html')


# ============================================================
# FORMULARIO 2 — LOGIN / LOGOUT
# ============================================================

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd  = request.form['password']
        if database.verificar_usuario(user, pwd):
            session['usuario'] = user
            return redirect(url_for('sala_criticas'))
        else:
            return render_template('login.html', error="Credenciales incorrectas.")
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('usuario', None)
    return redirect(url_for('inicio'))


# ============================================================
# ZONA PRIVADA
# ============================================================

@app.route('/sala_criticas')
def sala_criticas():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    todas_resenas  = database.obtener_resenas()
    mis_resenas    = database.obtener_resenas_usuario(session['usuario'])
    return render_template(
        'sala_criticas.html',
        usuario=session['usuario'],
        todas_resenas=todas_resenas,
        mis_resenas=mis_resenas
    )


# ============================================================
# FORMULARIO 3 — AÑADIR RESEÑA
# ============================================================

@app.route('/add_valoracion', methods=['GET', 'POST'])
def add_valoracion():
    if 'usuario' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        pelicula   = request.form['pelicula']
        puntuacion = request.form['puntuacion']
        comentario = request.form['comentario']
        database.guardar_resena(session['usuario'], pelicula, puntuacion, comentario)
        return redirect(url_for('sala_criticas'))
    return render_template('add_valoracion.html')


# Arranca el servidor
if __name__ == '__main__':
    app.run(debug=True, port=5000)