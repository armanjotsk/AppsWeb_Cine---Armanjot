import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

def conectar_db():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='', 
        database='projecte_cinema' # <- conexion BD
    )

# --- USUARIOS ---

def registrar_usuario(username, password):
    try:
        conn = conectar_db()
        cursor = conn.cursor()
        pass_hash = generate_password_hash(password)
        cursor.execute("INSERT INTO usuarios (username, password) VALUES (%s, %s)", (username, pass_hash))
        conn.commit()
        return True
    except:
        return False
    finally:
        cursor.close()
        conn.close()

def verificar_usuario(username, password):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM usuarios WHERE username = %s", (username,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    
    if resultado and check_password_hash(resultado[0], password):
        return True
    return False

# --- RESEÑAS / VALORACIONES ---

def guardar_resena(username, pelicula, puntuacion, comentario):
    conn = conectar_db()
    cursor = conn.cursor()
    
    # 1. Buscamos la ID del usuario
    cursor.execute("SELECT id FROM usuarios WHERE username = %s", (username,))
    id_user = cursor.fetchone()[0]
    
    # 2. Guardamos la reseña enlazada a ese usuario
    query = "INSERT INTO resenas (id_usuario, pelicula, puntuacion, comentario) VALUES (%s, %s, %s, %s)"
    cursor.execute(query, (id_user, pelicula, puntuacion, comentario))
    
    conn.commit()
    cursor.close()
    conn.close()

def obtener_resenas():
    conn = conectar_db()
    cursor = conn.cursor()
    query = """
        SELECT u.username, r.pelicula, r.puntuacion, r.comentario, r.fecha 
        FROM resenas r 
        JOIN usuarios u ON r.id_usuario = u.id 
        ORDER BY r.fecha DESC
    """
    cursor.execute(query)
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados

def obtener_resenas_usuario(username):
    conn = conectar_db()
    cursor = conn.cursor()
    query = """
        SELECT r.pelicula, r.puntuacion, r.comentario, r.fecha 
        FROM resenas r 
        JOIN usuarios u ON r.id_usuario = u.id 
        WHERE u.username = %s 
        ORDER BY r.fecha DESC
    """
    cursor.execute(query, (username,))
    resultados = cursor.fetchall()
    cursor.close()
    conn.close()
    return resultados