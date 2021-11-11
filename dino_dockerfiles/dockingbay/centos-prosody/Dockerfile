#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

FROM centos:centos7
MAINTAINER Jiri Stransky <jistr@jistr.com>

ADD usr/local/share/prosody/rebuild_counter /usr/local/share/prosody/rebuild_counter

RUN yum -y update; yum clean all

ADD prosody-install.sh /prosody-install.sh
RUN /prosody-install.sh
RUN rm /prosody-install.sh

ADD etc/prosody /etc/prosody
ADD usr/local/bin/prosody_wrapper /usr/local/bin/prosody_wrapper

VOLUME ["/var/lib/prosody"]

EXPOSE 5222 5269 5582

CMD ["/usr/local/bin/prosody_wrapper"]
