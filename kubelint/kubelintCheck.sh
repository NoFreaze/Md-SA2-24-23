#!/bin/bash
filename=$1

if [[ -z "$filename" ]]; then
   echo "No file selected, using format kubelintCheck.sh <filename.yml>"
   exit 1
fi

if [ -f $1 ]; then
   echo "File found, kubelinter starting"
else
   echo "FILE NOT FOUND!!!"
   exit 1
fi

docker run -v $PWD:/dir stackrox/kube-linter lint /dir/$1

echo $result
if [ $result -eq 0 ]; then
   kubectl apply -f ingress_rule.yml
   echo "No errors found, creating service"
   exit 0
else
   echo "The file failed verification!" 
   exit 1
fi
