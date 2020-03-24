# Simple Python Flask Dockerized Application#

Build the image using the following command

```bash
$ docker build -t simple-flask-app:latest .
```

Run the Docker container using the command shown below.

```bash
$ docker run -d -p 5000:5000 simple-flask-app
```

The application will be accessible at http:127.0.0.1:5000 or if you are using boot2docker then first find ip address using `$ boot2docker ip` and the use the ip `http://<host_ip>:5000`


My Notes:

Running an App in K8 using Docker:

docker build -t get_multiplication_facts:v0.1 .
docker run -p 5000:5000 get_multiplication_facts:v0.1
docker tag get_multiplication_facts:v0.1 gcr.io/my-playground-267105/get_multiplication_facts:v0.1
docker push gcr.io/my-playground-268616/get_multiplication_facts:v0.1
kubectl edit deployment get-multiplication-facts

Continuous Delivery Pipelines with Spinnaker and Kubernetes Engine:
https://google.qwiklabs.com/focuses/552?parent=catalog

1. Created a SA with Storage Admin role access. Downloaded the key for future use.
2. Setup Cloud Pub/Sub to trigger Spinnaker pipelines
    a. Created a topic gcr
    b. Created a subscription gcr-trigger
    c. Gave permissions to Spinnaker account to read from gcr-triggers subscription.
3. Install Helm
    a. wget https://storage.googleapis.com/kubernetes-helm/helm-v2.10.0-linux-amd64.tar.gz
    b. Unzip: tar zxfv helm-v2.10.0-linux-amd64.tar.gz
4. Grant Tiller, the server side of Helm, the cluster admin role in your cluster.
    i. kubectl create clusterrolebinding user-admin-binding --clusterrole=cluster-admin --user=$(gcloud config get-value account)
    ii. kubectl create serviceaccount tiller --namespace kube-system
    iii. kubectl create clusterrolebinding tiller-admin-binding --clusterrole=cluster-admin --serviceaccount=kube-system:tiller
5. Grant Spinnaker the cluster-admin role so it can deploy resources across all namespaces
    i. kubectl create clusterrolebinding --clusterrole=cluster-admin --serviceaccount=default:default spinnaker-admin
6. Configure Spinnaker
    a. Create a storage bucket 
    b. Create spinnaker-config.yaml
7. Deploy the Spinnaker Chart
    a. ./helm install -n cd stable/spinnaker -f spinnaker-config.yaml --timeout 600 --version 1.1.6 --wait
    

    





# mathgarage-flask
