FROM alpine:latest

LABEL maintainer="Allen Vailliencourt <allen.vailliencourt@forty8fiftylabs.com>"
# parts of this dockerfile are from here - https://github.com/William-Yeh/docker-ansible/blob/master/alpine3/Dockerfile
# customized this for AWS usage primarily (adding boto3 dependencies)

#COPY requirements.txt /requirements.txt
# Adding boto dependencies. Also added but not required jq and nano.
RUN apk --update add python3 py3-pip openssl ca-certificates \
    && apk --update add --virtual build-dependencies python3-dev libffi-dev openssl-dev build-base \
    && pip3 install --upgrade pip cffi boto boto3 \
    && pip3 install ansible \
    && apk --update add sshpass openssh-client jq nano \
    && apk del build-dependencies \ 
    && rm -rf /var/cache/apk/*

COPY files/ec2.ini files/ec2.py files/ansible.cfg /etc/ansible/

RUN chmod +x /etc/ansible/ec2.py

WORKDIR /ansible

CMD [ "ansible-playbook", "--version" ]