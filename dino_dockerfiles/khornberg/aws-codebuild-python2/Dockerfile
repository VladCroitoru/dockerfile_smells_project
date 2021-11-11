# Copyright 2017-2017 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Amazon Software License (the "License"). You may not use this file except in compliance with the License.
# A copy of the License is located at
#
#    http://aws.amazon.com/asl/
#
# or in the "license" file accompanying this file.
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, express or implied.
# See the License for the specific language governing permissions and limitations under the License.
#

# Modified

FROM amazonlinux:1

RUN curl -sL -o /tmp/node.rpm 'https://rpm.nodesource.com/pub_0.12/el/7/x86_64/nodejs-0.12.18-1nodesource.el7.centos.x86_64.rpm' \
    && yum groupinstall -y 'Development Tools' \
    && yum install python27-pip openssh-clients git gcc libxml2-devel libyaml-devel libxslt-devel zlib-devel libtiff-devel libjpeg-devel zlib-devel freetype-devel lcms2-devel libwebp-devel tcl-devel libxslt python27-devel bzip2 freetype fontconfig python26 parallel python34 python34-devel python34-pip python34-setuptools python34-virtualenv -y \
    && yum clean all \
    && rpm -i --nosignature --force /tmp/node.rpm \
    && rm -rf /var/cache/yum \
    && pip install virtualenv  --no-cache-dir

RUN set -x && \
    # Install docker-compose
    # https://docs.docker.com/compose/install/
    DOCKER_COMPOSE_URL=https://github.com$(curl -L https://github.com/docker/compose/releases/latest | grep -Eo 'href="[^"]+docker-compose-Linux-x86_64' | sed 's/^href="//' | head -1) && \
    curl -Lo /usr/local/bin/docker-compose $DOCKER_COMPOSE_URL && \
    chmod a+rx /usr/local/bin/docker-compose && \
    \
    # Basic check it works
    docker-compose version \
    && rm -rf /tmp/* /var/tmp/*

VOLUME /var/lib/docker

COPY dockerd-entrypoint.sh /usr/local/bin/

ENV PATH="/usr/local/bin:$PATH"

ENV LANG="en_US.utf8"

CMD ["python"]

ENTRYPOINT ["dockerd-entrypoint.sh"]
