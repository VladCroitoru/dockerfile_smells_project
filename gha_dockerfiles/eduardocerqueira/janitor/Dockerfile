FROM centos:8

ENV JANITOR_HOME=/home/janitor

USER root

RUN yum -y install python3-devel gcc python3-devel python3-pip
RUN yum clean all
RUN rm -rf /var/cache/yum

WORKDIR $JANITOR_HOME
COPY requirements/production.txt $JANITOR_HOME/
RUN touch $JANITOR_HOME/.janitor_history.txt

RUN useradd -r janitor
# fix permissions
RUN chown -R janitor $JANITOR_HOME
RUN chgrp -R 0 $JANITOR_HOME
RUN chmod -R g+rw $JANITOR_HOME


RUN pip3 install pip --upgrade
RUN pip3 install -r $JANITOR_HOME/production.txt
# installing from https://pypi.org/project/janitor-osp/
RUN pip3 install janitor-osp --upgrade
RUN pip3 freeze |grep janitor

USER janitor
RUN janitor --help
