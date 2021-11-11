FROM ubuntu:14.04
MAINTAINER hey@morrisjobke.de

# add ownCloud client
ADD Release.key /
RUN apt-key add - < Release.key
RUN rm Release.key
RUN echo 'deb http://download.opensuse.org/repositories/isv:/ownCloud:/desktop/xUbuntu_14.04/ /' >> /etc/apt/sources.list.d/owncloud-client.list

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y owncloud-client git python-pip curl

RUN mkdir /smashbox
RUN mkdir /root/smashdir

WORKDIR /smashbox

RUN git clone https://github.com/juanbaez/smashbox.git /smashbox
RUN git checkout master

RUN pip install -r requirements.txt

ADD smashbox-docker.conf /smashbox/etc/smashbox.conf

ADD run.sh /
ENTRYPOINT ["/run.sh"]
