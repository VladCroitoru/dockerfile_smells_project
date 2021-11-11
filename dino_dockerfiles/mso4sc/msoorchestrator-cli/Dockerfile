# Copyright 2017 MSO4SC - javier.carnero@atos.net
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

FROM centos:7

LABEL maintainer="javier.carnero@atos.net"

RUN mkdir /cli
WORKDIR /cli

# Basic dependencies
RUN yum -y update
RUN yum -y install yum-utils wget openssh-clients ntp
RUN yum clean all

# Cloudify-cli
ADD ./centos-cloudify-cli.sh ./
RUN /bin/bash ./centos-cloudify-cli.sh
RUN rm ./centos-cloudify-cli.sh

# Bootstrap script
ADD ./bootstrap-manager.sh ./

# SSH Keys
RUN mkdir ~/.ssh
ADD check-ssh-keys.sh /
RUN chmod +x /check-ssh-keys.sh

# Set all scripts as executables
RUN chmod +x ./*.sh

# Shared volume
VOLUME ['/cli/resources']

ENTRYPOINT ["bash", "-c", "/check-ssh-keys.sh && exec $@"]
CMD ["bash"]

