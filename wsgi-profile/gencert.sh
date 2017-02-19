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

C_VAL="DE"
ST_VAL="FFM"
L_VAL="FRANKFURT"
O_VAL="SCHNEIDERMATIC"
OU_VAL="NERDFARM"
CN_VAL="ssl.schneidermtic.org"

if [ -e $CWD/ssl ]
then
  rm -rf $CWD/ssl
fi

mkdir $CWD/ssl

cd $CWD/ssl
openssl req -nodes -newkey rsa:2048 -keyout server.key -out server.csr -subj "/C=$C_VAL/ST=$ST_VAL/L=$L_VAL/O=$O_VAL/OU=$OU_VAL/CN=$CN_VAL"

cp server.key server.key.org
openssl rsa -in server.key.org -out server.key

openssl x509 -req -days 3650 -in server.csr -signkey server.key -out server.crt
cp server.crt ssl.crt
cp server.key ssl.key
