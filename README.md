nvm install 16.17.0


# Frontend 

npm run dev (any)


NPM Custom package

npm publish --access public

npm version patch 

npm run build

npm publish 

npm install @scriptmotor/common

npm update @scriptmotor/common

# Docker
Make sure docker is running. 

docker images (any) 

docker ps (any)

docker build -t (image_id/image)  .

docker push (image_id/image) (any)

docker run -p PORT:PORT melmore123/notifications (any)

docker logs (image_id)


# Kubectl

kubectl get pods (any)

kubectl log (pod)

kubectl describe pod (pod_name)

kubectl get pods -o wide 

kubectl create secret generic jwt-secret --from-literal=JWT_KEY=asdf

kubectl get secrets

kubectl delete pod (pod_id) (any)

kubectl apply -f 

kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.8.2/deploy/static/provider/cloud/deploy.yaml

kubeadm init --kubelet-insecure-tls

kubectl exec -it pod_id_name sh (any) (shell)

kubectl rollout restart deployment (image)

kubectl get nodes (any)

kubectl config view

kubectl config use-context docker-desktop



# Skaffold run app 

skaffold dev (dir)

skaffold delete (dir)


# Chrome security bypass

type: thisisunsafe


# NATS Streaming Server

…

# Jest Unit Test

npm run test (test dir)


# Mongo 

….

# Redis 
redis-commander


# Bull



# Pipenv

conda deactivate (optional)

pip3 install --user pipenv (dir)

export PATH="/path/to/pip:$PATH"

export PIPENV_VENV_IN_PROJECT=1 (dir)

pipenv install --python 3.11 (dir)

pipenv shell  (dir)

pipenv run (dir)
 


#  Flask
flask db init

flask db migrate

flask db upgrade

# GCloud

Troubleshoot 
Build History
Error Reporting
Logs Explorer

# Deployment Digital Ocean

brew install dolt

doctl auth init --context <NAME>

doctl account get

doctl kubernetes cluster kubeconfig save <cluster-id|cluster-name> [flags]

