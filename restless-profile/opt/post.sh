#!/bin/bash

curl -X Post -H "Content-type: application/json" -d '{"firstname":"xyz","lastname":"xyz"}' http://127.0.0.1:5000/api/v1/author
