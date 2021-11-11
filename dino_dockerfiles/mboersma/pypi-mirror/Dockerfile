FROM ubuntu:12.04
MAINTAINER Matt Boersma <matt@opdemand.com>

ENV DEBIAN_FRONTEND noninteractive

# install bandersnatch dependencies and nginx
RUN apt-get update && \
    apt-get install -y cron curl python-software-properties
RUN add-apt-repository -y ppa:nginx/stable
RUN apt-get update && \
    apt-get install -yq nginx

# install latest pip
RUN curl -s https://raw.github.com/pypa/pip/1.5.4/contrib/get-pip.py | python -

# install latest stable bandersnatch mirroring tool
RUN pip install -r https://bitbucket.org/ctheune/bandersnatch/raw/stable/requirements.txt
ADD files/ /

# expose the public HTTP site and the twisted PB API interface port
EXPOSE 80 80
WORKDIR /app
VOLUME /srv/pypi
CMD ["/app/bin/start"]
