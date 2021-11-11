# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
# 
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM stealthly/docker-java

MAINTAINER stealthly

#Kafka settings
ENV KAFKA_VERSION 0.8.1.1
ENV SCALA_VERSION 2.9.2
ENV KAFKA_RELEASE kafka_$SCALA_VERSION-$KAFKA_VERSION
ENV KAFKA_URL https://archive.apache.org/dist/kafka/$KAFKA_VERSION/$KAFKA_RELEASE.tgz
ENV KAFKA_HOME /opt/$KAFKA_RELEASE

#Unzip and place to permanent location
RUN wget -q $KAFKA_URL -O /tmp/$KAFKA_RELEASE.tgz
RUN tar xfz /tmp/$KAFKA_RELEASE.tgz -C /opt

EXPOSE 9092

#Adding startup script
ADD start-kafka.sh /usr/bin/start-kafka.sh

#Starting Kafka
CMD start-kafka.sh
