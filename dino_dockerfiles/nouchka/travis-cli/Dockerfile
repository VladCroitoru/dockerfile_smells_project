FROM debian:jessie
LABEL maintainer="Jean-Avit Promis docker@katagena.com"
LABEL org.label-schema.vcs-url="https://github.com/nouchka/docker-travis-cli"
LABEL version="latest"

RUN apt-get update --fix-missing && \
	apt-get update && \
	apt-get install -y -q ruby ruby-dev build-essential git

RUN gem install travis --no-rdoc --no-ri

ENV TRAVIS_CONFIG_PATH /home/developer/.travis

RUN export uid=1000 gid=1000 && \
    mkdir -p /home/developer && \
    echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${uid}:" >> /etc/group && \
    chown ${uid}:${gid} -R /home/developer

WORKDIR /home/developer/workspace/
VOLUME /home/developer/workspace/
USER developer

RUN mkdir -p /home/developer/.travis

ENTRYPOINT ["/usr/local/bin/travis"]
