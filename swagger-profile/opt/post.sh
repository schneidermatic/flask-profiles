#!/bin/bash

curl -X POST -H "Content-type: application/json" -d '{"firstname":"Jim","lastname":"Rogers"}' http://127.0.0.1:5000/authors/identity
