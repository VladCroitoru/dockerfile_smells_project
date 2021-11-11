# Copyright 2015 Akamai Technologies, Inc. All Rights Reserved.
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License at 
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
FROM python:2.7.10
MAINTAINER Kirsten Hunter (khunter@akamai.com)
RUN apt-get update
RUN apt-get install -y curl patch gawk g++ gcc make libc6-dev patch libreadline6-dev zlib1g-dev libssl-dev libyaml-dev libsqlite3-dev sqlite3 autoconf libgdbm-dev libncurses5-dev automake libtool bison pkg-config libffi-dev supervisor
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q curl libssl-dev python-all wget vim python-pip php5 ruby-dev nodejs-dev npm php-pear php5-dev ruby perl5 
RUN pip install httpie-edgegrid 
ADD ./examples /opt/examples
ADD ./contrib/python /opt/examples/python/contrib
WORKDIR /opt/examples/ruby
RUN gem install bundler
RUN bundler install
WORKDIR /opt/examples/node
RUN npm install
WORKDIR /opt/examples/python
RUN python /opt/examples/python/tools/setup.py install
ADD ./MOTD /opt/MOTD
RUN echo "alias gen_edgerc=/opt/examples/python/gen_edgerc_new.py" >> /root/.bashrc
RUN echo "alias verify_creds=/opt/examples/python/verify_creds.py" >> /root/.bashrc
RUN echo "cat /opt/MOTD" >> /root/.bashrc
RUN mkdir /root/.httpie
ADD ./config.json /root/.httpie/config.json
RUN echo "PS1='Akamai API Bootcamp >> '" >> /root/.bashrc

#Add conf supervisor
COPY src_sysc0d/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

#Add scripts and files
RUN mkdir /src
COPY src_sysc0d/ccu_v3.py.example /src/ccu_v3.py.example
COPY src_sysc0d/fast-purge.sh /src/fast-purge.sh
COPY src_sysc0d/genere_config.sh /src/genere_config.sh

#Exec supervisor and script in background 
COPY src_sysc0d/entrypoint.sh /entrypoint.sh
RUN chmod 755 /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
