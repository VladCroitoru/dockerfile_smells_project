# Copyright 2015 Guillaume Pellerin
# Copyright 2015 Thomas Fillon
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

FROM parisson/timeside:latest-dev

MAINTAINER Guillaume Pellerin <yomguy@parisson.com>, Thomas Fillon <thomas@parisson.com>

RUN mkdir /opt/TimeSide-Diadems
WORKDIR /opt/TimeSide-Diadems

# Install binary dependencies with conda
ADD conda-requirements.txt /opt/TimeSide-Diadems/
#ADD requirements.txt /opt/TimeSide-Diadems/

RUN conda install -c thomasfillon -c piem --file conda-requirements.txt

# Install remaining depencies with pip
# RUN pip install -r requirements.txt

# Clone app
ADD . /opt/TimeSide-Diadems
WORKDIR /opt/TimeSide-Diadems

# Install remaining depencies with pip (+ install in develop mode with "-e .")
RUN pip install -r requirements.txt


EXPOSE 8000
