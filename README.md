[![wakatime](https://wakatime.com/badge/user/87464ce7-a479-47b1-b3aa-2548252894d7/project/d9b1bb54-68f2-4f12-a35e-809166b1a226.svg)](https://wakatime.com/badge/user/87464ce7-a479-47b1-b3aa-2548252894d7/project/d9b1bb54-68f2-4f12-a35e-809166b1a226)

# Upgraded Octo Lamp

Welcome to the Upgraded Octo Lamp repository! This project is a distributed image processing service built using Python, FastAPI, and Kubernetes. The service accepts image files, processes them to generate histograms, and demonstrates the power of parallel processing and Kubernetes orchestration.

The Upgraded Octo Lamp project demonstrates a scalable, distributed image processing service where multiple clients can send images to a server over HTTP, and the server will generate histograms of these images. The service is designed to run on a Kubernetes cluster and utilize FastAPI for handling HTTP requests.

## Architecture

Client: Sends images to the server for processing via HTTP requests.

Server: A FastAPI-based service that accepts image uploads, processes them to generate histograms, and returns the results.

Kubernetes: Orchestrates the deployment of the server, clients, and workers, ensuring scalability and reliability.

## Features

Scalable Image Processing: Easily scale the number of workers and clients to handle a large number of concurrent requests.

FastAPI for HTTP Communication: Efficient and modern web framework to handle HTTP requests and responses.

Kubernetes Integration: Deploy and manage the service on a Kubernetes cluster for high availability and fault tolerance.

Performance Testing: Simulate concurrent clients using tools like wrk2 or custom scripts to benchmark the service.

## Getting Started
### Prerequisites

Docker - To build and run containerized applications.

Kubernetes - To orchestrate and manage containerized applications.

kubectl - Command-line tool to interact with Kubernetes clusters.

## Installation

Clone the repository:

```
git clone https://github.com/Ingvord/upgraded-octo-lamp.git
cd upgraded-octo-lamp
```

Build Docker Images:

Build the Docker images for the server and client.

```
docker build -t upgraded-octo-lamp-server:latest -f server/Dockerfile .
docker build -t upgraded-octo-lamp-client:latest -f client/Dockerfile .
```

Push Docker Images to Your Registry (optional):

Push the images to a Docker registry to be used in your Kubernetes cluster.

```
docker tag upgraded-octo-lamp-server:latest <your-registry>/upgraded-octo-lamp-server:latest
docker push <your-registry>/upgraded-octo-lamp-server:latest

docker tag upgraded-octo-lamp-client:latest <your-registry>/upgraded-octo-lamp-client:latest
docker push <your-registry>/upgraded-octo-lamp-client:latest
```

Running the Service

Deploy to Kubernetes:

Apply the Kubernetes manifests to deploy the server, clients, and workers.

```
kubectl apply -f k8s/
```

Access the Service:

You can access the service via the provided Ingress, or you can forward a port to access the server locally:

```
kubectl port-forward svc/upgraded-octo-lamp-server 8080:80
```

Access the service at http://localhost:8080.

## Testing

You can use the provided client scripts or tools like wrk2 to test the performance of your service.

Run the Client Test Script:

```
python client.py --image=lenna.jpeg --url=http://<your-service-url>/process-image --histogram=out/histogram.png
```

Use wrk2 for Load Testing:

```
wrk2 -t12 -c100 -d30s -R1000 -s multipart.lua http://<your-service-url>/process-image
```

## Customization

Modify Kubernetes Manifests:

The Kubernetes manifests in the k8s/ directory can be customized to suit your environment. Adjust the number of replicas, resource limits, and other parameters as needed.
Customize Image Processing Logic:

The image processing logic in server.py can be modified to include additional features such as different image processing algorithms, logging, and more.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request to contribute to this project. Ensure your changes are well-documented and tested.

### License

This project is licensed under the MIT License - see the LICENSE file for details.

## Additional Notes

Troubleshooting: If you encounter any issues during setup or execution, please refer to the Issues section on GitHub to report and track known issues.
