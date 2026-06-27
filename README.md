# 🚀 Azure AKS Observability Platform

## 📌 Overview

Azure AKS Observability Platform is an end-to-end cloud-native DevOps project that demonstrates automated application deployment, container orchestration, and Kubernetes monitoring on Microsoft Azure.

The project automates the complete CI/CD workflow using GitHub Actions, Docker, Azure Container Registry (ACR), and Azure Kubernetes Service (AKS). It also integrates Prometheus and Grafana to provide real-time monitoring and observability for Kubernetes workloads.

This project was built to simulate a production-style deployment workflow and strengthen hands-on experience with modern DevOps practices.

---

# 🏗️ Solution Architecture

```
Developer
     │
     ▼
GitHub Repository
     │
     ▼
GitHub Actions (CI/CD)
     │
     ▼
Docker Image Build
     │
     ▼
Azure Container Registry (ACR)
     │
     ▼
Azure Kubernetes Service (AKS)
     │
     ▼
Kubernetes Deployment
     │
     ▼
Application Pods
     │
     ▼
LoadBalancer Service
     │
     ▼
Python Flask Application

────────────────────────────────────

Prometheus
     │
     ▼
Collect Kubernetes Metrics
     │
     ▼
Grafana
     │
     ▼
Real-Time Dashboards
```

---

# 🚀 Features

* Automated CI/CD pipeline using GitHub Actions
* Docker image build and push to Azure Container Registry
* AKS deployment using Kubernetes manifests
* Rolling deployment strategy
* Automatic image update during deployment
* Kubernetes LoadBalancer service
* Containerized Python Flask application
* Prometheus metrics endpoint
* Prometheus monitoring using Helm
* Grafana dashboards for visualization
* Kubernetes cluster observability
* Zero manual deployment after code push

---

# 🛠️ Technology Stack

## Cloud

* Microsoft Azure
* Azure Kubernetes Service (AKS)
* Azure Container Registry (ACR)

## Containers

* Docker
* Kubernetes

## CI/CD

* GitHub Actions

## Monitoring

* Prometheus
* Grafana
* Helm

## Programming

* Python
* Flask

## Operating System

* Ubuntu (WSL2)

---

# 📁 Project Structure

```
azure-aks-observability-platform/

├── .github/
│   └── workflows/
│       └── ci.yml
│
├── app/
│   ├── app.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── kubernetes/
│   ├── deployment.yaml
│   └── service.yaml
│
├── monitoring/
│   ├── grafana/
│   └── prometheus/
│
└── README.md
```

---

# ⚙️ CI/CD Workflow

The deployment pipeline is fully automated.

## Stage 1 – Source Code

Developer pushes code to GitHub.

↓

## Stage 2 – Continuous Integration

GitHub Actions automatically:

* Checks out source code
* Builds Docker image
* Tags image using Git SHA
* Pushes image to Azure Container Registry

↓

## Stage 3 – Continuous Deployment

GitHub Actions:

* Authenticates with Azure
* Connects to AKS
* Applies Kubernetes manifests
* Updates Deployment with latest image
* Performs rolling update
* Verifies rollout status

↓

## Stage 4 – Monitoring

Prometheus scrapes Kubernetes metrics.

↓

Grafana visualizes:

* Pod Health
* CPU Usage
* Memory Usage
* Node Status
* Workloads
* Cluster Metrics

---

# 📦 Application Endpoints

| Endpoint | Description        |
| -------- | ------------------ |
| /        | Application Home   |
| /health  | Health Check       |
| /info    | System Information |
| /metrics | Prometheus Metrics |

---

# 📈 Monitoring Stack

The monitoring stack was deployed using Helm.

### Prometheus

Collects metrics from:

* Kubernetes Nodes
* Pods
* Deployments
* Services
* kube-state-metrics
* Node Exporter

### Grafana

Dashboards include:

* Kubernetes Cluster Overview
* Node Metrics
* CPU Utilization
* Memory Utilization
* Pod Status
* Network Usage
* Workload Monitoring

---

# 📷 Project Screenshots


---

## Verification Commands

kubectl get nodes
kubectl get pods
kubectl get svc
kubectl get deployments

---

# 👨‍💻 Author

**Sowndarraj M**

Cloud | DevOps | Network Engineer

AWS Certified Solutions Architect – Associate

GitHub: https://github.com/Sowndar-1118

LinkedIn: https://www.linkedin.com/in/sowndarraj-m-b35634200
