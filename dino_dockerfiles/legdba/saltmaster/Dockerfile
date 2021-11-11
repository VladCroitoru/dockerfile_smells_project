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
FROM ubuntu:16.04
MAINTAINER legdba <legdba@yahoo.com>

# Install Salt 2016.3 (latest stable version at time of writting)
RUN apt-get -q -y update && \
    apt-get -q -y upgrade && \
    apt-get -q -y install wget curl software-properties-common && \
    apt-get -q -y install python-software-properties && \
    wget -O - https://repo.saltstack.com/apt/ubuntu/16.04/amd64/2016.3/SALTSTACK-GPG-KEY.pub | apt-key add - && \
    echo "deb http://repo.saltstack.com/apt/ubuntu/16.04/amd64/2016.3 xenial main" | tee /etc/apt/sources.list.d/saltstack.list && \
    apt-get -q -y update && \
    apt-get -q -y install salt-api salt-cloud salt-master salt-minion salt-ssh salt-syndic && \
    rm -rf /var/lib/apt/lists/*

ENV LOG_LEVEL=${LOG_LEVEL:-"error"}

ADD run.sh /usr/local/bin/run.sh
# Add patch file that changes salt environment verification to disable chowning /etc/salt and /srv when run as root.
# This is required to run it in a clean way within a docker container.
# The "clean" way involves mounting drives for config (/etc/salt and /srv) in read only.
# As the docker run -v option mount as root, salt has to run as root.
# Running salt as root, salt will try to chown those mounted directory and fail as they are read-only.
# Salt the trying to chown directories for security reasons, which is moot in a dockerized environment.
# Therefore that chown is removed.
ADD patch.txt /var/tmp/patch.txt
RUN patch -p1 < /var/tmp/patch.txt && \
    chmod +x /usr/local/bin/run.sh && \
    /usr/local/bin/run.sh --version

EXPOSE 4505 4506
ENTRYPOINT ["/usr/local/bin/run.sh"]
