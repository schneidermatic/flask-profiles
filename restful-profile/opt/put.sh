#!/bin/bash

curl http://localhost:5000/todo1 -d "data=Remember the milk" -X PUT {"todo1": "Remember the milk"}
