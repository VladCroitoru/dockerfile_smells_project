FROM ubuntu:12.04

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python-pip python-dev libssl-dev
RUN pip install docker-py python-etcd
ADD register /bin/register

ENTRYPOINT ["/bin/register"]
