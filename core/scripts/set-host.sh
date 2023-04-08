#!/bin/bash
# workdir /
set -o errexit

#source ./scripts/set-env.sh

HOST_IP=`kubectl get ingress --namespace=todo-project | grep 'fastapi-core-http' |  cut -d ' ' -f 10`

sudo echo "$HOST_IP todo-project.com" >> /etc/hosts