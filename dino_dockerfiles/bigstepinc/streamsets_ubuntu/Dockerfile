#
#
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
#
#

FROM mcristinagrosu/bigstepinc_java_8_ubuntu

ARG SDC_URL=https://archives.streamsets.com/datacollector/3.0.2.0/tarball/streamsets-datacollector-core-3.0.2.0.tgz
#ARG SDC_USER=sdc
ARG SDC_VERSION=3.0.2.0

# We set a UID/GID for the SDC user because certain test environments require these to be consistent throughout
# the cluster. We use 20159 because it's above the default value of YARN's min.user.id property.
#ARG SDC_UID=20159

# The paths below should generally be attached to a VOLUME for persistence.
# SDC_CONF is where configuration files are stored. This can be shared.
# SDC_DATA is a volume for storing collector state. Do not share this between containers.
# SDC_LOG is an optional volume for file based logs.
# SDC_RESOURCES is where resource files such as runtime:conf resources and Hadoop configuration can be placed.
# STREAMSETS_LIBRARIES_EXTRA_DIR is where extra libraries such as JDBC drivers should go.
ENV SDC_DATA=/streamsets/data \
    SDC_DIST="/streamsets/streamsets-datacollector-${SDC_VERSION}" \
    SDC_LOG=/streamsets/logs \
    SDC_RESOURCES=/streamsets/resources \
    SDC_CONF="/streamsets/streamsets-datacollector-${SDC_VERSION}/etc" 
ENV STREAMSETS_LIBRARIES_EXTRA_DIR="${SDC_DIST}/streamsets-libs-extras"

#RUN addgroup -S -g ${SDC_UID} ${SDC_USER} && \
#    adduser -S -u ${SDC_UID} -G ${SDC_USER} ${SDC_USER}
RUN mkdir /streamsets/

RUN cd /tmp && \
    curl -o /tmp/sdc.tgz -L "${SDC_URL}" && \
    mkdir /streamsets/streamsets-datacollector-${SDC_VERSION} && \
    tar xzf /tmp/sdc.tgz --strip-components 1 -C /streamsets/streamsets-datacollector-${SDC_VERSION} && \
    rm -rf /tmp/sdc.tgz

# Add logging to stdout to make logs visible through `docker logs`.
RUN sed -i 's|INFO, streamsets|INFO, streamsets,stdout|' "${SDC_DIST}/etc/sdc-log4j.properties"

# Create necessary directories.
RUN mkdir -p /mnt \
    "${SDC_DATA}" \
    "${SDC_LOG}" \
    "${SDC_RESOURCES}" \
    "${SDC_CONF}"

# Move configuration to /etc/sdc
#RUN mv "${SDC_DIST}/etc" "${SDC_CONF}"

# Use short option -s as long option --status is not supported on alpine linux.
RUN sed -i 's|--status|-s|' "${SDC_DIST}/libexec/_stagelibs"

# Setup filesystem permissions.
#RUN chown -R "${SDC_USER}:${SDC_USER}" "${SDC_DIST}/streamsets-libs" \
#    "${SDC_CONF}" \
#    "${SDC_DATA}" \
#    "${SDC_LOG}" \
#    "${SDC_RESOURCES}" \
#    "${STREAMSETS_LIBRARIES_EXTRA_DIR}"

#USER ${SDC_USER}
EXPOSE 18630
COPY entrypoint.sh /
RUN chmod 777 /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
