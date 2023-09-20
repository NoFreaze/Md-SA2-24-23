#!/bin/bash
helm repo add elastic https://helm.elastic.co

helm repo update elastic

helm upgrade --install elasticsearch --version 7.17.3 elastic/elasticsearch --set replicas=1 -n elastic --create-namespace --debug

helm upgrade --install kibana --version 7.17.3 elastic/kibana -n elastic --debug
