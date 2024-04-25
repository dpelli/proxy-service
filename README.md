# Salesloft TechOps Exercise - Proxy Service API

This is a simple proxy service API built using Python with Flask, Docker for containerization, and Kubernetes for deployment.

## Overview

The Proxy Service API allows you to abstract away the provider you use behind the scenes by providing a robust HTTP API with an endpoint that returns data from another API. The API returns data in JSON format.

## Setup

### Prerequisites

- Python 3.9 or higher
- Docker
- Kubernetes cluster (for deployment)

### Installation

1. Clone this repository:

   ```bash
   git clone <repository-url>
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the API Locally

1. Navigate to the project directory:

   ```bash
   cd proxy-service-api
   ```

2. Run the Flask application:

   ```bash
   python app.py
   ```

   The API will be accessible at `http://localhost:5000`.

### Docker Containerization

To run the API within a Docker container:

1. Build the Docker image:

   ```bash
   docker build -t proxy-service .
   ```

2. Run the Docker container:

   ```bash
   docker run -p 5000:5000 proxy-service
   ```
   
### Docker Compose

To run the API within a Docker container using docker-compose:
   
   ```bash
   docker compose up
   ```

### Deployment with Kubernetes

1. Apply the Kubernetes deployment and service files:

   ```bash
   kubectl apply -f deployment.yaml
   kubectl apply -f service.yaml
   ```

2. Access the API through the Kubernetes service.

## API Documentation

The API documentation is available using Swagger UI. Once the API is running, you can access the documentation at `http://localhost:5000/apidocs`.

## Endpoints

- `/`: Proxy endpoint that returns data from another API.

## Usage

- Make a GET request to the `/` endpoint to retrieve data from the proxied API.

## License

This project is licensed under the [MIT License](LICENSE).
