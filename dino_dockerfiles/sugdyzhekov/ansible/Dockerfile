FROM python:2.7-alpine

LABEL maintainer="Sergey Ugdyzhekov, sergey@ugdyzhekov.org"

ENV ansible_version v2.2.1.0-1

RUN apk --no-cache add git mariadb-client mariadb-dev libffi openssh docker
RUN pip install -U pysphere boto boto3 docker-py awscli hvac

RUN apk --no-cache add --virtual build-dependencies gcc python-dev libffi-dev linux-headers musl-dev openssl-dev && \
    pip install git+git://github.com/ansible/ansible.git@${ansible_version} && \
    pip install mysql-python && \
    apk del build-dependencies

ADD https://raw.githubusercontent.com/ansible/ansible/devel/contrib/inventory/ec2.py /usr/local/lib/python2.7/site-packages/ansible/plugins/inventory/
RUN chmod 755 /usr/local/lib/python2.7/site-packages/ansible/plugins/inventory/ec2.py
COPY plugins/callback/timestamp.py /usr/local/lib/python2.7/site-packages/ansible/plugins/callback/
COPY ansible.cfg /etc/ansible/ansible.cfg
COPY exec.sh /bin/exec.sh
RUN chmod +x /bin/exec.sh

WORKDIR /workbench
ENTRYPOINT ["/bin/exec.sh"]
