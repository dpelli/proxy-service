# Salesloft TechOps Exercise - Proxy Service API

This is a simple proxy service API built using Python with Flask, Docker for containerization, and Kubernetes for deployment.

## Setup

### Prerequisites

- Python 3.9 or higher
- Docker
- Kubernetes cluster (for deployment)

### Installation

1. Create and activate Python virtual environment:

   ```bash
   python3 -m venv proxy-service-env && source proxy-service-env/bin/activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
   
3. Obtain API Key from [Tasty API](https://rapidapi.com/apidojo/api/tasty/) and add it to the `.env` file

### Running the API Locally

1. Navigate to the project directory:

   ```bash
   cd proxy-service
   ```

2. Run the Flask application:

   ```bash
   python server.py
   ```

   The API will be accessible at [http://localhost:5000](http://localhost:5000)

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
3. To describe the service:
   ```bash
   kubectl describe services proxy-service-ip-service
   ```
4. To teardown the deployment:
   ```bash
   kubectl delete deployment proxy-service
   ```

## Endpoints

- `/`: Proxy endpoint that returns a list of recipes data from [Tasty API](https://rapidapi.com/apidojo/api/tasty/).

## API Documentation

The API documentation is available using Swagger UI. Once the API is running, you can access the documentation at [http://localhost:5000/apidocs](http://localhost:5000/apidocs)
