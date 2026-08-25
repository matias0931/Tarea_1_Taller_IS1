import json
from wsgiref.simple_server import make_server
tasks = {}
def app(environ, start_response):
    metodo = environ['REQUEST_METHOD']
    ruta = environ['PATH_INFO']
    if ruta=='/tasks':
        if metodo=='GET':   #GET /tasks
            body=json.dumps(tasks).encode('utf-8')
            status = '200 OK'
        elif metodo == 'POST':  # POST /tasks
            try:
                request_body_size = int(environ.get('CONTENT_LENGTH', 0))
            except ValueError:
                request_body_size = 0
            request_body = environ['wsgi.input'].read(request_body_size).decode('utf-8')
            nueva_tarea = json.loads(request_body)
            if tasks:
                nuevo_id = max(tasks.keys()) + 1
            else:
                nuevo_id = 1
            nueva_tarea['id'] = nuevo_id
            tasks[nuevo_id] = nueva_tarea
            body = json.dumps(nueva_tarea).encode('utf-8')
            status = '201 Created'
    elif ruta.startswith('/tasks/'):
        partes = ruta.split('/')
        task_id= int(partes[2])
        if metodo== 'DELETE':   #DELETE /tasks/{id}
            if task_id in tasks:
                status='204 No Content'
                del tasks[task_id]
                headers=[("Content-Type", "application/json")]
                start_response(status, headers)
                return[]
        elif metodo == 'GET':   #GET /tasks/{id}
            if task_id in tasks:
                status = '200 OK'
                body=json.dumps(tasks[task_id]).encode('utf-8')
            else:
                status='404 Not Found'
                body=json.dumps({"error": "Not Found"}).encode('utf-8')    
        elif metodo == 'PATCH': #PATCH /tasks/{id}
            if task_id in tasks:
                try:
                    request_body_size = int(environ.get('CONTENT_LENGTH', 0))
                except ValueError:
                    request_body_size = 0
            request_body = environ['wsgi.input'].read(request_body_size).decode('utf-8')
            datos_nuevos=json.loads(request_body)
            tasks[task_id].update(datos_nuevos)
            status = '200 OK'
            body=json.dumps(tasks[task_id]).encode('utf-8')
    else:
        status='404 Not Found'
        body=json.dumps({"error": "Not Found"}).encode('utf-8')
    headers = [("Content-Type", "application/json")]
    start_response(status, headers)
    return[body]
with make_server("", 9292, app) as server:
    print("Listening on http://localhost:9292")
    server.serve_forever()