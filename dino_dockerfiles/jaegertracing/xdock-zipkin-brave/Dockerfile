#
# Copyright 2017 The Jaeger Authors
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License
# is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing permissions and limitations under
# the License.
#

FROM openjdk:alpine

MAINTAINER Pavol Loffay <ploffay@redhat.com>

ENV APP_HOME /app/

COPY pom.xml $APP_HOME
COPY src $APP_HOME/src
COPY .mvn $APP_HOME/.mvn
COPY mvnw $APP_HOME

WORKDIR $APP_HOME
RUN ./mvnw package -Dlicense.skip=true && rm -rf ~/.m2

ENV ZIPKIN_URL=http://jaeger-collector:9411
ENV JSON_ENCODER=JSON_V1

EXPOSE 8080
EXPOSE 8081

# set env variables when starting the container
CMD java -jar -Dzipkin.encoding=$ENCODING -Dzipkin.json.encoder=$JSON_ENCODER -Dzipkin.url=$ZIPKIN_URL target/jaegertracing-xdock-brave-0.0.1-SNAPSHOT.jar
