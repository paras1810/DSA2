'''
Involve designing small independent service that communicate via HTTP/REST or gRPC can deployed and scaled independently.

Rest Guiding Principles
    Uniform Interface
    Stateless
    Cacheable
    Client Server Design Pattern
    Layered System

Features of API
    Small
    Stateless
    Independent
    Communicates
    Language-agnostic

pip install fastapi uvicorn

uvicorn main:app --reload --port 8000

Dockerize your microservice

docker build -t user-service .
docker run -p 8000:8000 user-service

REST API using requests, httpx
Message Queueusing RabbitQueue, Kafka
gRPC (High performance binary communicate)

Logging structlog, loguru
Auth: JWT or OAuth2
Monitoring: Prometheus or Grafana
Rate Limiting: middleware or API Gateway
Resilience: Circuit breakers pybreaker
Deployment: Docker+Kubernetes
'''

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float 

@app.get("/")
def read_root():
    return {"message": "Hello from microservice"}

@app.post("/items")
def create_item(item: Item):
    return {"name": item.name, "price": item.price}

# Calling from another
import requests 
response = requests.post(
    "http://localhost:8000/items/",
    json={"name":"Book", "price":9.99}
)
print(response.json())

'''
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
'''

'''
API Gateway
    Single entry point for system of microservices.
    Manages and routes external requests to appropriate internal microservices, 
    handling authentication, rate limiting, logging, response aggregation.
    Request routing, load Balancing, caching

Service Discovery
    Process by which microservices automatically find and communicate with each other without hardcoding IPs or URLs.
    It keeps track of these services and provides current network location(IP and port)
    If its not there manually update hostnames/IPs of services in every other service.
        Client Side: Netflix Eureka with Ribbon
        Server Side: AWS ELB, Istio
'''



