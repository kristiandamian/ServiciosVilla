from google.appengine.api import mail

def enviarCorreo(nombre, correo, titulo, mensaje):
	mail.send_mail(sender="serviciosvilla.com Support <serviciosvilla88@gmail.com>",
		       to="Daniel Diaz<danieldiaz@getwell.care>; Vaqueton <kristiandamian@getwell.care>",
		       subject="Un nuevo comentario en serviciosvilla.com de "+nombre,
                       body="""
	Hola Patricia:

	Hay un nuevo comentario en serviciosvilla.com:

	Nombre: """+nombre+"""
	Correo: """+correo+"""
	Telefono: """+titulo+"""
	Mensaje: """+mensaje+"""

        Saludos""")
