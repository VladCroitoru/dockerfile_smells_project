FROM debian:jessie

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6

RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.2 main" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list

RUN apt-get update && apt-get install --force-yes -y mongodb-org-tools python python-pip
RUN pip install awscli

ADD dump.sh .

RUN chmod +x dump.sh

RUN mkdir ~/.aws
ADD config ~/.aws

ENTRYPOINT ["/bin/bash", "./dump.sh"]
