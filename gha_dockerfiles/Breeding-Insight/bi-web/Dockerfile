#
# See the NOTICE file distributed with this work for additional information
# regarding copyright ownership.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

FROM node:lts

ARG HOST_USER_ID=1001
ARG HOST_GROUP_ID=1001
ARG CONT_USERNAME="host"
ARG CONT_GROUPNAME="host"
# ARG CONT_FILES=""

# create container user with same id as the host user
RUN groupadd -g ${HOST_GROUP_ID} ${CONT_GROUPNAME}
RUN useradd -l -u ${HOST_USER_ID} -g ${CONT_GROUPNAME} ${CONT_USERNAME}
RUN install -d -m 0755 -o ${CONT_USERNAME} -g ${CONT_GROUPNAME} /home/${CONT_USERNAME}

# switch to host user
USER ${CONT_USERNAME}

# Switch to the working directory
# NOTE: be sure to make the working directory explictly. If you let the WORKDIR
# command make it then it will be owned by root
RUN ["mkdir", "/home/host/biweb"]
WORKDIR /home/${CONT_USERNAME}/biweb

# Install the app dependencies and configuration
COPY --chown=host:host ["./src", "/home/host/biweb/src/"]
COPY --chown=host:host ["./task", "/home/host/biweb/task/"]
COPY --chown=host:host ["./tests", "/home/host/biweb/test/"]
COPY --chown=host:host ["./public", "/home/host/biweb/public/"]
COPY --chown=host:host ["babel.config.js", ".browserslistrc", "cypress.json", ".eslintrc.js", ".npmrc", "tsconfig.json", "vue.config.js", ".env.development","./"]
COPY --chown=host:host ["package.json", "/home/host/biweb/package.json"]
COPY --chown=host:host ["package-lock.json", "/home/host/biweb/package-lock.json"]
COPY --chown=host:host ./src ./src/
COPY --chown=host:host ./task ./task/
RUN ["npm", "--verbose", "ci"]

# start the web server
ENTRYPOINT ["npm", "run", "serve"]
