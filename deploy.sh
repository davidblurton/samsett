#!/bin/bash
set -e

docker build -t davidblurton/samsett-api .
docker push davidblurton/samsett-api
