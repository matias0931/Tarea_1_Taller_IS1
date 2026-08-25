Diferencias entre GET, POST, PATCH y DELETE:

GET: Se usa solo para leer o consultar información del servidor.

POST: Se usa para crear un recurso completamente nuevo. NO ES IDEMPOTENTE porque cada vez que se envía, el servidor genera un         recurso con un identificador nuevo, nunca el mismo sin importar si el resto de la informacion es la misma. Sería                idempotente si al ejecutarlo una vez tuviera el mismo efecto que ejecutarlo muchas veces.

PATCH: Se usa para hacer una modificación de un recurso existente. Es parcial, osea que solo actualiza los campos específicos          que se envían en el cuerpo de la petición. Lo demás queda igual.

DELETE: Se usa para eliminar un recurso del servidor.
