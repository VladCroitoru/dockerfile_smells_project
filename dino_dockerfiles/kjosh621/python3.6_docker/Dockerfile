FROM python:3.6

# Install.
RUN \
  sed -i 's/# \(.*multiverse$\)/\1/g' /etc/apt/sources.list && \
  apt-get update && \
  apt-get -y upgrade && \
  apt-get install -y build-essential && \
  apt-get install -y vim wget curl bash-completion python3 && \
  pip install mysql-connector-python-rf && \
  rm -rf /var/lib/apt/lists/*

RUN rm /usr/bin/python && ln -s /usr/local/bin/python /usr/bin/python

WORKDIR /opt/warming_engine

CMD ["python"]

