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

FROM adoptopenjdk/openjdk13

ARG HOST_USER_ID=1001
ARG HOST_GROUP_ID=1001
ARG CONT_USERNAME="host"
ARG CONT_GROUPNAME="host"

# create container user with same id as the host user
#RUN groupadd -g ${HOST_GROUP_ID} ${CONT_GROUPNAME}
#RUN useradd -l -u ${HOST_USER_ID} -g ${CONT_GROUPNAME} ${CONT_USERNAME}
#RUN install -d -m 0755 -o ${CONT_USERNAME} -g ${CONT_GROUPNAME} /home/${CONT_USERNAME}

# switch to host user
#USER ${CONT_USERNAME}

# Switch to the working directory
# NOTE: be sure to make the working directory explicitly. If you let the WORKDIR
# command make it then it will be owned by root
#RUN ["mkdir", "/home/host/biapi"]
WORKDIR /home/${CONT_USERNAME}/biapi

#install bi-api source
COPY ./target/bi-api*.jar ./

ENTRYPOINT java -jar --enable-preview -Dmicronaut.environment=prod bi-api*.jar
