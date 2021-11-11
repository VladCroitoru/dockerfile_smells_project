FROM ubuntu:latest
MAINTAINER Bioboxes

RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install -y  wget

#install soap
RUN apt-get install soapdenovo2 -y

#install python 
RUN apt-get install python -y
RUN mkdir /opt/bin
RUN wget -O /opt/bin/PyYAML-3.11.tar.gz http://pyyaml.org/download/pyyaml/PyYAML-3.11.tar.gz
RUN tar xzvf /opt/bin/PyYAML-3.11.tar.gz -C /opt/bin
WORKDIR /opt/bin/PyYAML-3.11
RUN python setup.py install

#add schema, parser and run command
ADD bbx/ /bbx
RUN chmod a+x /bbx/run/default

#load the input-validator
ENV BASE_URL https://s3-us-west-1.amazonaws.com/bioboxes-tools/validate-biobox-file
ENV VERSION  0.x.y
RUN apt-get install -y xz-utils
RUN mkdir -p /bbx/bin/biobox-validator
RUN wget --quiet --output-document - ${BASE_URL}/${VERSION}/validate-biobox-file.tar.xz  |  tar xJf - --directory /bbx/bin/biobox-validator  --strip-components=1

ENV PATH /bbx/run:$PATH
