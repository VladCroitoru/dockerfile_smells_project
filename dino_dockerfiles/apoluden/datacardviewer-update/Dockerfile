#COMMENT
#DOCKER-VERSION 0.3.4
#boot2docker VERSION 1.2.0
FROM ubuntu:14.04
#MAINTAINER Artiom Poluden<artiomnkkm@gmail.com>
RUN echo "cache-bust"
RUN apt-get update
#Install basic applications for Ubuntu 14.04 image
RUN apt-get install -y -q git
RUN apt-get update
# Install Python and Basic Python Tools
RUN apt-get install -y -q python-all-dev python-pip
#add github repo where locates DatacardViewer WEB app and specify location
RUN git clone https://github.com/aPoluden/DatacardViewer-Update.git /dcv
#Select work directory
WORKDIR /dcv
#install requerements for WEB application
RUN pip install -r application/requirements.txt
# expose application current port wich will be connected with some port Distribution on wich will run application
EXPOSE 5000
# command to run inside container
CMD ["python", "run.py"]
