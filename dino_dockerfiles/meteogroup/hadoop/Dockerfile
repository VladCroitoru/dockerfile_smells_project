# Copyright © 2016 MeteoGroup Deutschland GmbH
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM meteogroup/java:8

ARG APACHE_MIRROR=http://www.apache.org/dist

RUN cd opt &&\
    curl -f "$APACHE_MIRROR/hadoop/common/hadoop-2.8.0/hadoop-2.8.0.tar.gz" | gunzip | tar -x &&\
    ln -s hadoop-* hadoop

RUN if [ ! -x /bin/which ]; then \
      echo '#!/bin/bash' >/bin/which &&\
      echo 'command -v "$1"' >>/bin/which &&\
      chmod 755 /bin/which; \
    fi

ENV JAVA_HOME=/etc/alternatives/jre \
    HADOOP_HOME=/opt/hadoop \
    HADOOP_PREFIX=/opt/hadoop \
    HADOOP_COMMON_HOME=/opt/hadoop \
    HADOOP_HDFS_HOME=/opt/hadoop \
    HADOOP_MAPRED_HOME=/opt/hadoop \
    HADOOP_YARN_HOME=/opt/hadoop \
    HADOOP_CONF_DIR=/opt/hadoop/etc/hadoop \
    YARN_CONF_DIR=$HADOOP_PREFIX/etc/hadoop \
    PATH=${PATH}:/opt/hadoop/bin
