FROM phusion/baseimage:latest

# Install Autodesk ochopod and MongoDB.
RUN \
  apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 7F0CEB10 && \
  echo 'deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse' > /etc/apt/sources.list.d/mongodb-org-3.0.list && \
  apt-get update && \
  apt-get install -y mongodb-org curl python python-requests git supervisor && \
  curl https://bootstrap.pypa.io/get-pip.py | python && pip install git+https://github.com/autodesk-cloud/ochopod.git && \
  apt-get -y remove git && \
  apt-get -y autoremove && \
  rm -rf /var/lib/apt/lists/* && \
  mkdir -p /var/lib/mongodb

ADD resources/pod /opt/mongod/pod
ADD resources/supervisor /etc/supervisor/conf.d

# start pod
CMD /usr/bin/supervisord -n -c /etc/supervisor/supervisord.conf
