FROM python:3.6-alpine

RUN apk add --update zip git

ADD appspec.yml /opt/appspec.yml

RUN git config --global credential.helper '!aws codecommit credential-helper $@'
RUN git config --global credential.UseHttpPath true