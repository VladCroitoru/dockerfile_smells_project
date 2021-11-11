# Copyright 2015, 2018 Guillaume Pellerin, Thomas Fillon
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

FROM debian:jessie

MAINTAINER Guillaume Pellerin <yomguy@parisson.com>, Thomas fillon <thomas@parisson.com>



# install confs, keys and deps
COPY debian-requirements.txt /

RUN apt-get update && \
    DEBIAN_PACKAGES=$(egrep -v "^\s*(#|$)" debian-requirements.txt) && \
    apt-get install -y --force-yes $DEBIAN_PACKAGES && \
    apt-get clean && \
    rm debian-requirements.txt

# Install conda in /opt/miniconda
ENV PATH /opt/miniconda/bin:$PATH
RUN wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O miniconda.sh && \
    bash miniconda.sh -b -p /opt/miniconda && \
    rm miniconda.sh && \
    hash -r && \
    conda config --set always_yes yes --set changeps1 yes && \
    conda update -q conda

# Install binary dependencies with conda
COPY environment.yml /
RUN conda env update --name root --file environment.yml && \
    conda clean --all --yes  && \
    rm environment.yml

COPY link_gstreamer.py /
RUN python link_gstreamer.py

# Install bower
RUN npm install -g bower

