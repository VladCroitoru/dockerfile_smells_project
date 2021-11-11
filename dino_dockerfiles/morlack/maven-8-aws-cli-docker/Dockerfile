FROM twalter/maven-docker
MAINTAINER Mitchell Herrijgers

RUN apt-get install -y python python-pip
RUN pip install --upgrade awscli s3cmd python-magic
RUN apt-get remove -y --purge python-pip
RUN rm -r /var/cache/apt/*
VOLUME /root/.aws