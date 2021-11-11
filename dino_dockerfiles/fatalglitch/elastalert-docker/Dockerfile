# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM alpine

LABEL maintainer="FatalGlitch - https://github.com/fatalglitch/elastalert-docker"

ENV CONFIG_DIR /opt/elastalert/config
ENV RULES_DIR /opt/elastalert/rules
ENV LOG_DIR /opt/elastalert/logs
ENV SET_CONTAINER_TIMEZONE False
ENV CONTAINER_TIMEZONE Europe/Stockholm
ENV ELASTALERT_URL https://github.com/Yelp/elastalert.git
ENV ELASTALERT_CONFIG ${CONFIG_DIR}/elastalert_config.yaml
ENV ELASTALERT_HOME /opt/elastalert
ENV ELASTALERT_SUPERVISOR_CONF ${CONFIG_DIR}/elastalert_supervisord.conf
ENV ELASTICSEARCH_HOST elasticsearch
ENV ELASTICSEARCH_PORT 9200
ENV ELASTICSEARCH_TLS False
ENV ELASTICSEARCH_TLS_VERIFY True
ENV ELASTALERT_INDEX elastalert_status

WORKDIR /opt

# Install software required for Elastalert and NTP for time synchronization.
RUN apk update && \
    apk upgrade && \
    apk add ca-certificates openssl-dev openssl libffi-dev python2 python2-dev py2-pip py2-yaml gcc musl-dev tzdata openntpd wget git

# Download latest version of elastalert (MASTER BRANCH)
RUN git clone https://github.com/Yelp/elastalert.git -b master /opt/elastalert

WORKDIR /opt/elastalert

# Install Elastalert.
RUN python setup.py install && \
    pip install -e . && \
    pip uninstall twilio --yes && \
    pip install twilio==6.0.0 && \
    pip install "elasticsearch>=5.0.0"

# Install Supervisor.
RUN easy_install supervisor

# Create directories. The /var/empty directory is used by openntpd.
RUN mkdir -p "${CONFIG_DIR}" && \
    mkdir -p "${RULES_DIR}" && \
    mkdir -p "${LOG_DIR}" && \
    mkdir -p /var/empty && \

# Clean up.
    apk del python2-dev && \
    apk del musl-dev && \
    apk del gcc && \
    apk del openssl-dev && \
    apk del libffi-dev && \
    rm -rf /var/cache/apk/*

# Copy the script used to launch the Elastalert when a container is started.
COPY ./start-elastalert.sh /opt/

# Make the start-script executable.
RUN chmod +x /opt/start-elastalert.sh

# Define mount points.
VOLUME [ "${CONFIG_DIR}", "${RULES_DIR}", "${LOG_DIR}"]

# Launch Elastalert when a container is started.
# CMD ["/opt/start-elastalert.sh"]

ENTRYPOINT ["elastalert", "--config", "/opt/elastalert/elastalert_config.yaml", "--verbose"]
