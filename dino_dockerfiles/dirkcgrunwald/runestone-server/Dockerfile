FROM ubuntu
MAINTAINER grunwald@cs.colorado.edu

RUN apt-get update && apt-get -y --no-install-recommends install \
    ca-certificates \
    curl git \
    python-pip python-dev python-pkgconfig python-setuptools python-numpy python-matplotlib \
    libfreetype6-dev freetype* \
    postgresql-client \
    libpq-dev libxml2-dev libxslt1-dev \
    build-essential autoconf libtool pkg-config

RUN  gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4
RUN  curl -o /usr/local/bin/gosu -SL "https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-architecture)" \
     && curl -o /usr/local/bin/gosu.asc \
     	-SL "https://github.com/tianon/gosu/releases/download/1.4/gosu-$(dpkg --print-architecture).asc" \
     && gpg --verify /usr/local/bin/gosu.asc \
     && rm /usr/local/bin/gosu.asc \
     && chmod +x /usr/local/bin/gosu

RUN mkdir -p /opt && \
    cd /opt && \
    git clone -b R-2.14.6 --recursive https://github.com/web2py/web2py.git && \
    cd /opt/web2py/gluon && \
    sed -i 's/127.0.0.1/0.0.0.0/' widget.py && \
    cd /opt/web2py/applications && \
    git clone https://github.com/RunestoneInteractive/RunestoneServer runestone && \
    cd runestone && \
    pip install -r requirements.txt

VOLUME /opt
WORKDIR /opt

EXPOSE 8000

ADD imagefiles/routes.py /opt/web2py/routes.py
ADD imagefiles/0.py /opt/web2py/applications/runestone/models/0.py
ADD imagefiles/1.py /opt/web2py/applications/runestone/models/1.py

ADD  imagefiles/entrypoint.sh /opt/entrypoint.sh
ADD  imagefiles/runestone-server /opt/runestone-server

CMD [ "/bin/bash", "/opt/entrypoint.sh" ]

