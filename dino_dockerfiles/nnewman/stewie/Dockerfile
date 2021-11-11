FROM python:3.5-alpine

RUN apk --update add git

RUN pip install -e git+https://github.com/nnewman/stewie.git@master#egg=stewie

ENV CONFIG_PATH /opt/stewie
WORKDIR /opt/stewie

USER nobody
EXPOSE 8043
