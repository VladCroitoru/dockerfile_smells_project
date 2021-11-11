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

FROM stealthly/docker-ruby

RUN gem install riemann-client riemann-tools riemann-dash

ENV RIEMANN_VERSION 0.2.10
ENV RIEMANN_RELEASE riemann-$RIEMANN_VERSION
ENV RIEMANN_URL http://aphyr.com/riemann/$RIEMANN_RELEASE.tar.bz2
ENV RIEMANN_HOME /opt/$RIEMANN_RELEASE

RUN wget -q $RIEMANN_URL -O /tmp/$RIEMANN_RELEASE.tar.bz2
RUN tar xvfj /tmp/$RIEMANN_RELEASE.tar.bz2 -C /opt

ADD riemann.config /opt/riemann.config
ADD config.rb /opt/config.rb
ADD dash-config.json /opt/dash-config.json
ADD start.sh /usr/bin/start.sh

EXPOSE 4567 5555 5556

CMD start.sh
