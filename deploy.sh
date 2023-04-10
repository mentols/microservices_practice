#!/bin/bash

SERVICES=( "core" "auth" "statistic" )

for service in "${SERVICES[@]}"
do
    echo "Applying k8s files for $service..."
    kubectl apply -f ./$service/k8s/code/
done
