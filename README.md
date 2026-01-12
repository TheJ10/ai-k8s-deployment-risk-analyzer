# Reusable Backend Base

This repository provides a clean, reusable FastAPI backend foundation intended to be forked and extended by other projects such as Kubernetes-based systems or multi-cloud deployments.

This repository is not a standalone production service and is not deployed independently.

---

## Purpose

The purpose of this repository is to act as a base backend platform that can be reused across multiple future projects.

It provides:
- Clean API structure
- Clear separation between API and business logic
- Dockerized runtime
- Unit-testable service layer
- Cloud-agnostic design

This backend will be reused by:
- Kubernetes AI project
- Multi-cloud DevOps project
- Future backend systems

---

## Architecture Overview

```text
	Request  
	   ↓  
API Layer (FastAPI Routers)  
	   ↓  
Service Layer (Pure Python Logic)  
	   ↓  
	Response
```  

### Design Principles

- APIs are thin (no business logic)
- Services contain reusable logic
- Configuration via environment variables
- Same code runs locally, in Docker, cloud, and Kubernetes

---

## Project Structure

 ```text
app/  
├── api/              — API routes (HTTP layer only)  
├── services/         — Core reusable logic  
├── main.py           — Application entry point  
tests/                — Unit tests for service layer  
Dockerfile             — Production-ready Docker image  
requirements.txt       — Python dependencies  
```

---

## Available APIs

### Health Check

`GET /health`

Used for:
- Liveness checks
- Orchestration systems
- Monitoring

---

### Service Info

`GET /info`

Returns service metadata:
- Service name
- Version
- Environment

---

### Generic Processing API

`POST /api/process`

Example request:

```json
{
  "text": "hello world"
}
```

Example response:

```json
{
  "original": "hello world",
  "length": 11,
  "uppercase": "HELLO WORLD"
}
```

This endpoint is intentionally generic and will be extended by downstream projects.

---

## Docker Usage
Build Image
```bash
docker build -t backend-base:latest .
```

Run Container
```bash
docker run -p 8000:8000 backend-base:latest
```

Access endpoints:
- http://localhost:8000/health
- http://localhost:8000/docs

---

## Testing

Run unit tests:
```bash
pytest
```

Tests focus on the service layer, not the API transport layer.

---

## Reuse Strategy

### This repository is intended to be:
- Forked by other projects
- Extended with project-specific logic
- Integrated with cloud, Kubernetes, and CI/CD in downstream projects
- Downstream projects should not modify this repository directly.

---

## What This Repository Does NOT Include

- CI/CD pipelines
- Cloud deployments
- Kubernetes manifests
- Databases
- Authentication or authorization
These concerns are intentionally handled in downstream projects.

---

## Design Philosophy

> Build once.
> Reuse everywhere.
> Deploy only when it matters.

---

## Author:
Jaspal Gundla
