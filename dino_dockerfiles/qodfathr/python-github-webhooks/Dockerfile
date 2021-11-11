FROM centos:7 
MAINTAINER "Todd Mancini" <todd.mancini@daxat.com>

ENV container docker
RUN yum -y update
RUN yum -y install epel-release
RUN yum -y install python-pip
RUN yum -y install git

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000
CMD ["python", "webhooks.py"]
