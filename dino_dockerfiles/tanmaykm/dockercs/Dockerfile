# Circuitscape as a Docker image
# Allows the command line and cloud interfaces to be used.

FROM dockerfile/python
MAINTAINER Tanmay Mohapatra <tanmaykm@gmail.com>

RUN apt-get update

RUN apt-get install liblapack3 liblapack-dev libblas3 libblas-dev -y
RUN apt-get install python-numpy -y
RUN apt-get install python-scipy -y
RUN apt-get install python-tornado -y
RUN apt-get install python-sockjs-tornado -y

RUN pip install --upgrade pip
RUN pip install google-api-python-client 
RUN pip install pyamg 
RUN pip install psutil 
RUN pip install Circuitscape 

RUN mkdir -p /circuitscape
WORKDIR /circuitscape
RUN git clone https://github.com/Circuitscape/cloudCS.git

VOLUME /data

# Don't run as root.
# To avoid output files being created as root.
RUN groupadd csuser
RUN useradd -m -d /data -s /bin/bash -g staff csuser

WORKDIR /data
USER csuser

