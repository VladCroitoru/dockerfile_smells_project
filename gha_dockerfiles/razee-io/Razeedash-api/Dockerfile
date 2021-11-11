################################################################################
# Copyright 2019 IBM Corp. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
################################################################################
#######################################
# Build the preliminary image
#######################################
FROM node:12-alpine as buildImg

RUN apk update
RUN apk --no-cache add python make g++

USER node
WORKDIR /home/node

COPY --chown=node . /home/node
RUN npm install --production --loglevel=warn


#######################################
# Build the production image
#######################################
FROM node:12-alpine

USER node
WORKDIR /home/node

RUN export BUILD_TIME=`date '+%Y-%m-%d %H:%M:%S'`
ARG BUILD_TIME
ENV BUILD_TIME=${BUILD_TIME}
ARG BUILD_ID
ENV BUILD_ID=${BUILD_ID}

COPY --chown=node --from=buildImg /home/node /home/node

EXPOSE 3333
CMD ["npm", "start"]
