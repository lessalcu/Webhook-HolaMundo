# Webhook REST API with Go and Swagger

This project implements a REST API server in Go that handles Webhooks. It is also documented with Swagger to facilitate its use and testing through a web interface.

## Description

This API is capable of receiving POST requests on the `/webhook` endpoint, which accept a payload in JSON format. The response is a confirmation with the status of the operation.

### Endpoints

#### `POST /webhook`
Receives a notification in JSON format.

##### Parameters
- **payload**: A JSON object containing the webhook data.

##### Successful response
```json
{
"status": "received",
"data": { ... }
}
```

##### Sample request

```bash
curl -X POST "http://localhost:8080/webhook" -H "Content-Type: application/json" -d '{"event": "test_event"}'
```

##### Sample response

```json
{
"status": "received",
"data": {
"event": "test_event"
}
}
```

## Installation

### Clone the repository

```bash
git clone https://github.com/lessalcu/Webhook-HelloWorld.git
cd Webhook-HelloWorld
```

### Run the application locally

1. Make sure You must have Go installed (version 1.20 or higher).
2. Install the dependencies:

```bash
go mod tidy
```

3. Generate the Swagger documentation:

```bash
swag init
```

4. Run the application:

```bash
go run main.go
```

5. Access the Swagger documentation at [http://localhost:8080/swagger/index.html](http://localhost:8080/swagger/index.html).

## Docker

### Download the image from Docker Hub

1. Download the image from Docker Hub:

```bash
docker pull lssalas/hello-world-webhook:latest
```

2. Run the container:

```bash
docker run -p 8080:8080 --name hello-world-webhook-container lssalas/hello-world-webhook
```

2. Access the API and Swagger via [http://localhost:8080/swagger/index.html](http://localhost:8080/swagger/index.html).

## Swagger

Swagger documentation is available at:

```
http://localhost:8080/swagger/index.html
```

This interface allows you to interact with the API directly from your browser.