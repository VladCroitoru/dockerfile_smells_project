FROM ubuntu:14.04

RUN apt-get update && apt-get -y install build-essential libssl-dev libffi-dev python-dev python-pip libsasl2-dev libldap2-dev

RUN pip install virtualenv

WORKDIR /root
RUN virtualenv venv
RUN . ./venv/bin/activate &&  pip install --upgrade setuptools pip && pip install superset

WORKDIR /root/venv/bin
RUN ls
RUN ./fabmanager create-admin --username admin --firstname admin --lastname admin --email 222@qq.com  --password admin --app superset

RUN ./superset db upgrade

RUN ./superset load_examples
RUN ./superset init

ADD ./init.sh /root/
RUN chmod +x /root/init.sh

EXPOSE 8088

ENTRYPOINT ["/root/init.sh"]
