##############################################################
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
##############################################################
FROM node:8.10.0-alpine

# Prepare for dir
RUN mkdir -p /opt/node-app
WORKDIR /opt/node-app

# Install all dependencies and test
COPY package.json /opt/node-app/
COPY app/ /opt/node-app/app/
COPY test/ /opt/node-app/test/
COPY LICENSE NOTICE /opt/node-app/app/
RUN npm install && \
    npm test && \
    # Now that tests passed, reinstall the minimum dependencies to keep image as small as possible
    rm -rf node_modules && \
    export NODE_ENV=production && \
    npm install && \
    npm dedupe && \
    # Remove swagger 78MB beast that is installed but usefull for testing only!
    rm -rf node_modules/swagger-express-mw/node_modules/swagger-node-runner/node_modules/sway/node_modules/json-schema-faker && \
    # Check the app starts
    node app/server.js --help

# Prepare for service
CMD ["-p", "8080"]
ENTRYPOINT [\
    "npm",\
    "start",\
    "--"\
    ]
EXPOSE 8080

# TODO: add a production.json with production settings (gzip, etc.)
# ENV NODE_ENV production
