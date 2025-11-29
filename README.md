# Serie Bases de Datos con Python
## Ficheros
### JSON


En el fichero Filedatabase.py declaramos el nombre del fichero
> books_file = 'book.txt'

Como vemos solo hace falta el fichero que maneja la base de datos, que en este caso es un fichero de texto.
El fichero de la aplicacion app.py, practicamente no hace falta modificarlo a excepcion de esta sentencia:

 > read = 'YES' if book_return['read'] else 'NO'
 
 por esta otra:

> read = 'YES' if book_return['read'] == '1' else 'NO'

Para ver paso a paso como se desarrolla visitar el este video de youtube
https://youtu.be/4yEKWer4cVI?si=hZPuBqtvZYlgMv8p
