FROM debian:jessie
MAINTAINER l.murawski

# Get and install required linux packages.
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y install build-essential \
    python-dev \
    python-pip \
    vim \
    telnet && \
    apt-get -y install freetds-dev && \
    apt-get update --fix-missing

#   Add Tini - tini 'init' for containers
RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

# Install required python libraries 
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

# create a place for mounting local directory with configuration
ENV CONF_DIR /conf
RUN mkdir -p $CONF_DIR &&\
  chown 65534:65534 $CONF_DIR

# Create a place to deploy the application
ENV APP_DIR /app
RUN mkdir -p $APP_DIR
COPY pacman.py $APP_DIR
COPY ZabbixReader.py $APP_DIR

ADD ssl /ssl
ADD conf /conf

WORKDIR $APP_DIR


ENTRYPOINT ["/usr/bin/tini", "--"]

CMD ["python","pacman.py"]
#CMD ["bash"]
