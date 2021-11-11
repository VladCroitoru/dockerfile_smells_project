#
# Copyright 2021 Splunk Inc.
#
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
#
FROM registry.access.redhat.com/ubi8/ubi
RUN groupadd -g 1001 celery \
    && useradd -m -u 1001 -g celery celery

RUN curl -fsSL https://goss.rocks/install | GOSS_VER=v0.3.13 sh
ARG PYTHON_RUNTIME_VERSION=3.8

RUN cd /tmp ;\
    dnf install tzdata curl wget nc python${PYTHON_RUNTIME_VERSION} python3-pip procps-ng -y ;\
    dnf update -y ;\
    mkdir /work

COPY entrypoint.sh /work/entrypoint.sh
COPY dist/*.whl /tmp
RUN pip${PYTHON_RUNTIME_VERSION} install $(ls /tmp/*.whl); rm -f /tmp/*.whl

WORKDIR /work
USER 1001
ENTRYPOINT [ "/work/entrypoint.sh" ]