# Webhook REST API con Go y Swagger

Este proyecto implementa un servidor REST API en Go que maneja Webhooks. Además, está documentado con Swagger para facilitar su uso y pruebas a través de una interfaz web.

## Descripción

Esta API es capaz de recibir peticiones POST en el endpoint `/webhook`, que aceptan un payload en formato JSON. La respuesta es una confirmación con el status de la operación.

### Endpoints

#### `POST /webhook`
Recibe una notificación en formato JSON.

##### Parámetros
- **payload**: Un objeto JSON que contiene los datos del webhook. 

##### Respuesta exitosa
```json
{
  "status": "received",
  "data": { ... }
}
```

##### Ejemplo de peticion

```bash
curl -X POST "http://localhost:8080/webhook" -H "Content-Type: application/json" -d '{"event": "test_event"}'
```

##### Respuesta de ejemplo

```json
{
  "status": "received",
  "data": {
    "event": "test_event"
  }
}
```

## Instalación

### Clonar el repositorio

```bash
git clone https://github.com/lessalcu/Webhook-HolaMundo.git
cd Webhook-HolaMundo
```

### Ejecutar la aplicación localmente

1. Asegúrate de tener Go instalado (versión 1.20 o superior).
2. Instalar las dependencias:

   ```bash
   go mod tidy
   ```

3. Generar la documentación de Swagger:

   ```bash
   swag init
   ```

4. Ejecuta la aplicación:

   ```bash
   go run main.go
   ```

5. Accede a la documentación Swagger en [http://localhost:8080/swagger/index.html](http://localhost:8080/swagger/index.html).

## Docker

### Descargar la imagen desde Docker Hub

1. Ddescargar la imagen de Docker Hub:

    ```bash
    docker pull lssalas/hello-world-webhook:latest
    ```

2. Ejecutar el contenedor:

   ```bash
   docker run -p 8080:8080 --name hello-world-webhook-container lssalas/hello-world-webhook
   ```

2. Accede a la API y a Swagger a través de [http://localhost:8080/swagger/index.html](http://localhost:8080/swagger/index.html).

## Swagger

La documentación de Swagger está disponible en la ruta:

```
http://localhost:8080/swagger/index.html
```

Esta interfaz permite interactuar con la API directamente desde tu navegador.

