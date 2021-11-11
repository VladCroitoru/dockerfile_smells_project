FROM alpine:latest
LABEL maintainer="gwaewion@gmail.com"
EXPOSE 5000
VOLUME /vetopytter-core

ENV MONGODB_ADDRESS 10.0.2.15
ENV MONGODB_DBNAME vl
ENV MONGODB_USERNAME vl
ENV MONGODB_PASSWORD vl_password

RUN apk update
RUN apk add python3 python3-dev git openssh gcc musl-dev libffi-dev openssl-dev
RUN pip3 install --upgrade pip
RUN pip3 install flask jwt bson pymongo pyyaml

COPY run.sh /root

CMD ["sh", "/root/run.sh"]
