#!/bin/env bash

cd background; docker build -t background .; cd -
cd app; docker build -t app .; cd -

source set-env-vars.sh
envsubst < template.yml > docker-compose.yml

docker-compose up

