#!/bin/bash
#******************************************************************************
# Copyright 2016 the original author or authors.                              *
#                                                                             *
# Licensed under the Apache License, Version 2.0 (the "License");             *
# you may not use this file except in compliance with the License.            *
# You may obtain a copy of the License at                                     *
#                                                                             *
# http://www.apache.org/licenses/LICENSE-2.0                                  *
#                                                                             *
# Unless required by applicable law or agreed to in writing, software         *
# distributed under the License is distributed on an "AS IS" BASIS,           *
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.    *
# See the License for the specific language governing permissions and         *
# limitations under the License.                                              *
#******************************************************************************/

CWD=$(pwd)
FLASK_APP=$CWD/flask-app
VENV=$CWD/env

source $VENV/bin/activate

cd $FLASK_APP
gunicorn --bind 0.0.0.0:8443 --certfile $CWD/ssl/ssl.crt --keyfile $CWD/ssl/ssl.key --ssl-version 2 --ciphers TLSv1 main:app
