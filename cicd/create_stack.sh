#!/bin/bash

aws cloudformation create-stack \
 --capabilities CAPABILITY_NAMED_IAM \
 --stack-name flask-crud-app \
 --template-body file://template.yaml
