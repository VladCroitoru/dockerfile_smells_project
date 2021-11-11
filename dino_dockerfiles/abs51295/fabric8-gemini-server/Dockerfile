FROM registry.centos.org/centos/centos:7

ENV F8A_WORKER_VERSION=3055b19

RUN yum install -y epel-release &&\
    yum install -y gcc git python34-pip python34-requests httpd httpd-devel python34-devel &&\
    yum clean all

COPY ./requirements.txt /

RUN pip3 install -r requirements.txt && rm requirements.txt

COPY ./src /src

RUN pip3 install git+https://github.com/abs51295/fabric8-analytics-worker.git@${F8A_WORKER_VERSION}

ADD scripts/entrypoint.sh /bin/entrypoint.sh

RUN chmod 777 /bin/entrypoint.sh

ENTRYPOINT ["/bin/entrypoint.sh"]
