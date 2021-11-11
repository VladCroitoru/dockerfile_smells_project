# The MIT License
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

FROM cupenya/docker-jenkins-slave-mongo-ivy2-cache
MAINTAINER Elmar Weber <elmar(.)weber(@)cupenya(.)com>

# Setup Elastic Search
USER root
RUN apt-key adv --keyserver ha.pool.sks-keyservers.net --recv-keys 46095ACC8548582C1A2699A9D27D666CD88E42B4

ENV ELASTICSEARCH_VERSION 2.3.3
ENV ELASTICSEARCH_REPO_BASE http://packages.elasticsearch.org/elasticsearch/2.x/debian

RUN echo "deb $ELASTICSEARCH_REPO_BASE stable main" > /etc/apt/sources.list.d/elasticsearch.list && \
  apt-get update && \
  apt-get install -y elasticsearch=$ELASTICSEARCH_VERSION

WORKDIR /usr/share/elasticsearch
RUN for path in \
		./data \
		./logs \
		./config \
		./config/scripts \
    ; do \
		mkdir -p "$path"; \
		chown -R elasticsearch:elasticsearch "$path"; \
    done

COPY config ./config

COPY supervisord-elasticsearch.conf /etc/supervisor/conf.d/elasticsearch.conf

# Restore user for Jenkins slave
USER jenkins
WORKDIR /home/jenkins

