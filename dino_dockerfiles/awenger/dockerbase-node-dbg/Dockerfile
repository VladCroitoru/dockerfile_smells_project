FROM fbarth/dockerbase-node

RUN echo deb http://archive.ubuntu.com/ubuntu trusty main universe > /etc/apt/sources.list
RUN echo deb http://archive.ubuntu.com/ubuntu trusty-updates main universe >> /etc/apt/sources.list

RUN apt-get update \
&& apt-get upgrade -y --no-install-recommends \
&& apt-get install -y python-minimal make gcc build-essential g++

RUN npm config set python /usr/bin/python

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*