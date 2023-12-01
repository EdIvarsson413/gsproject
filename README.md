# Instrucciones de cómo usar el proyecto
1.  Dentro del proyecto creas el entorno virtual con el comando `python -m venv .venv`

2. Luego usas `pip install -r requerimientos.txt` para que no tengas que instalar tu mismo
    las dependencias

3. Al proyecto le va a faltar el sqlite, para ello primero:
    * Ejecutas `python manage.py runserver` (opcional por si quieres ver que todo esté bien)
    * Usas python manage.py makemigrations
    * Luego usas python manage.py migrate
    
   Con esto te deberia de crear todas las tablas sql y por si acaso deben de aplicarse las 
   migraciones de : admin (esto es de Django), contacto, metodos y cuentas

   Tablas sql importantes (En Admin Page):
    * cuentas_usuariopers (Cuentas - Usuarios)
    * contacto_metodo (Contado - Metodo)
    * metodos_metodo (Metodos - Metodo)
    * metodos_comentario (Metodos - Comentarios)

4. El uso de la pagina es por usuario y administrador, te registras en la pagina de forma normal
   para ser usuario normal. Para registrar a un admin usas el comando `python manage.py createsuperuser`, das algunos datos
   que sean faciles de recordar y ahora ya podrias entrar a la url localhost:8000/admin

5. Para la creación de los metodos antes debiste ser admin, si ya lo eres aqui están el txt de los metodos y las imagenes que por ahora he llegado a usar. [Se encuentran aqui](https://mega.nz/file/FV5Ezb4b#kOFYlRa9I_KJgu0wYyK9UiRHyiBOJIlyBI3St3xCx9)

## Iniciar servidor
1. `venv/Scripts/Activate.ps1`
2.  `python manage.py runserver`


# Ejecutar proyecto con Docker
En este punto del proyecto ya estan declaros los Docker files necesarios para llevar el proyecto a contenedores. Por lo que explico como se debería ejecutar el proyecto.

## Instrucciones
1. Tener Docker Desktop instalado (junto con la virtualización activada)

2. Llevar la carpeta del proyecto a un directorio llamado `code`. Esto es necesario ya que el Docker file viene especificado con esa instrucción.

`Nota: tu tienes que crear el directorio code`

3. Revisar los comandos de Docker para ejecutar el proyecto.

## Comandos de Docker

Ahora la lista de comandos necesarios tanto para Docker como el proyecto:

+ docker-compose up
    - Ejecuta el contenedor y se muestran los logs en la terminal actual.
    - Con ese comando ya no es necesario usar `python manage.py runserver`

+ docker-compose up -d --build
    - Esto correrá el contenedor pero antes va a crearlo con las especificaciones del archivo yml.
    - Adémas, el comando tambien hará que el contenedor se ejecute en segundo plano.

+ docker-compose logs
    - Sirve para mostrar los logs en la terminal si el contenedor se ejecuta en segundo plano.
    - Después se le debe indicar de qué servicio vendrán esos logs. Ej. `docker-compose logs web` para mostrar los logs del servicio de web.

## Comandos de Docker para el proyecto
+ docker-compose exec web python manage.py makemigrations
    - Prepara las migraciones para el proyecto en el contenedor.

+ docker-compose exec web python manage.py migrate
    - Le indica a Docker que ejecute el comando para realiar las migraciones del proyecto.

+ docker-compose exec web python manage.py collectstatic
    - Recolecta los archivos estáticos.

Los otros comandos se indican de la misma manera.