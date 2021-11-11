FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y \
  ca-certificates 

RUN apt-get update && apt-get upgrade -y && apt-get clean
RUN apt-get update  && apt-get install -y vim curl wget unzip jq bash ca-certificates git openssl
##
RUN apt-get clean
RUN apt-get update
RUN apt-get install --yes --no-install-recommends software-properties-common
RUN apt-get install --yes --no-install-recommends --fix-missing libffi-dev
RUN apt-get install --yes --fix-missing  libssl-dev
#libxml2-dev libxslt1-dev libmysqlclient-dev
RUN apt-get install --yes --no-install-recommends --fix-missing
# RUN usermod -s /bin/bash abc
RUN apt-get update
# RUN apt-get install -y curl vim python3.7 python3.7-dev python3.7-distutils python3-venv  python3-pip
# RUN update-alternatives --install /usr/bin/python python /usr/bin/python3.7 1
# RUN update-alternatives --set python /usr/bin/python3.7
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 install --upgrade pip

# RUN curl -s https://bootstrap.pypa.io/get-pip.py -o get-pip.py && \
#     python get-pip.py --force-reinstall && \
#     rm get-pip.py

##
RUN apt-get install -y  python3-dateutil python3-mysqldb uwsgi-plugin-python3
RUN pip install --upgrade setuptools

##
RUN python3 -V
RUN python -V

##
RUN pip3 install supervisor
RUN ln -s /usr/local/bin/supervisorctl /usr/bin/supervisorctl
RUN ln -s /usr/local/bin/supervisord /usr/bin/supervisord
RUN mkdir -p /var/log/supervisor

##
RUN pip3 install boto3
RUN apt-get install -y awscli
RUN apt-get install -y openssh-client
RUN pip install setuptools awscli


##
RUN apt-get clean && \
rm -rf \
 /tmp/* \
 /var/lib/apt/lists/* \
 /var/tmp/*

ARG NODE_VERSION=14.16.0
ARG NODE_PACKAGE=node-v$NODE_VERSION-linux-x64
ARG NODE_HOME=/opt/$NODE_PACKAGE

ENV NODE_PATH $NODE_HOME/lib/node_modules
ENV PATH $NODE_HOME/bin:$PATH

RUN curl https://nodejs.org/dist/v$NODE_VERSION/$NODE_PACKAGE.tar.gz | tar -xzC /opt/

RUN node -v
RUN npm -v

WORKDIR /code

ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 5000

ADD . /code
RUN npm i

ENTRYPOINT ["/bin/bash", "-c", "/usr/bin/supervisord -c /etc/supervisor/conf.d/supervisord.conf -n"]

# COPY docker-entrypoint.sh /usr/local/bin/
# ENTRYPOINT ["docker-entrypoint.sh"]
# ENTRYPOINT ["/bin/sh", "-c", "sleep 1h"]

# CMD [ "node" ]