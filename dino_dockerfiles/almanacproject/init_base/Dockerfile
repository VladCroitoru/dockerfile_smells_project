FROM alpine:3.3

MAINTAINER Raphael Ahrens

RUN apk update && apk add python3 git openssl openjdk8-jre

RUN python3 -m ensurepip && pip3 install --upgrade pip setuptools

RUN pip install PyYAML
RUN pip install git+https://github.com/almanacproject/rework.git@v0.0.2
RUN pip install git+https://github.com/almanacproject/psst.git@v0.0.2
RUN pip install git+https://github.com/almanacproject/bob_cert_builder.git@v0.0.2

COPY init /root/init
RUN chmod +x /root/init
CMD ["/root/init"]
