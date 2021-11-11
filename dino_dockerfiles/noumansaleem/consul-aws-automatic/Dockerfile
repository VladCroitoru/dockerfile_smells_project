FROM ubuntu

RUN apt-get update
RUN apt-get install -y curl python-pip
RUN pip install awscli

ADD ./configure /opt/configure
CMD /opt/configure