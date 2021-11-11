FROM node:8-stretch
MAINTAINER Kitware, Inc. <kitware@kitware.com>

EXPOSE 8080

RUN mkdir /girder
RUN mkdir /girder/logs

RUN apt-get -qqy update && apt-get install -qy software-properties-common python-software-properties && \
  apt-get update -qqy && apt-get install -qy \
    build-essential \
    git \
    xsltproc \
    libffi-dev \
    libsasl2-dev \
    libssl-dev \
    libldap2-dev \
    libpython2.7-dev && \
  apt-get clean && rm -rf /var/lib/apt/lists/*

RUN npm config set progress false
RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py

WORKDIR /girder
COPY girder /girder/girder
COPY clients /girder/clients
COPY plugins /girder/plugins
COPY scripts /girder/scripts
COPY grunt_tasks /girder/grunt_tasks
COPY Gruntfile.js /girder/Gruntfile.js
COPY setup.py /girder/setup.py
COPY package.json /girder/package.json
COPY README.rst /girder/README.rst

RUN python2 -m pip install --upgrade --upgrade-strategy eager --editable .[plugins]
RUN girder-install web --all-plugins

ENTRYPOINT ["girder", "serve"]
