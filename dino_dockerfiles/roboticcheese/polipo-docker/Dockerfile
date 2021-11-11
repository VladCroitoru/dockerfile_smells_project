# Author:: Jonathan Hartman (<j@p4nt5.com>)
#
# Copyright (C) 2014, Jonathan Hartman
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM roboticcheese/ubuntu:14.04
MAINTAINER Jonathan Hartman "j@p4nt5.com"

RUN mkdir /tmp/cheffing
ADD client.rb /tmp/cheffing/
ADD dna.json /tmp/cheffing/
ADD Berksfile /tmp/cheffing/
ADD https://opscode-omnibus-packages.s3.amazonaws.com/ubuntu/13.10/x86_64/chefdk_0.1.0-1_amd64.deb /tmp/cheffing/
RUN dpkg -i /tmp/cheffing/chefdk_0.1.0-1_amd64.deb
RUN cd /tmp/cheffing && berks vendor /tmp/cheffing/cookbooks
RUN chef-client -z -c /tmp/cheffing/client.rb -j /tmp/cheffing/dna.json -K /opt/chefdk/embedded/apps/test-kitchen/support/dummy-validation.pem
RUN rm -rf /tmp/cheffing/
RUN dpkg -P chefdk
RUN service polipo stop
EXPOSE 8123
CMD polipo -c /etc/polipo/config pidFile=/var/run/polipo/polipo.pid
