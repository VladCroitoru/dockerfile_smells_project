# Copyright 2018 SpiderOak, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

FROM centos:7

RUN curl -sSL http://dl.marmotte.net/rpms/redhat/el6/x86_64/storcli-1.16.06-2/storcli-1.16.06-2.x86_64.rpm > /tmp/storcli.rpm \
&& rpm -ivh /tmp/storcli.rpm \
&& rm /tmp/storcli.rpm

COPY . /

ENTRYPOINT ["/entrypoint.sh"]
