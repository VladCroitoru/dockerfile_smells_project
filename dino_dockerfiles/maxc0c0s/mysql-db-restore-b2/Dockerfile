FROM maxc0c0s/mysql-db-restore:latest

USER root

RUN apt-get update
RUN apt-get install -y sudo python python-pip
RUN pip install --upgrade b2

RUN echo "restorer ALL=NOPASSWD: /usr/local/bin/b2" >> /etc/sudoers

USER restorer
