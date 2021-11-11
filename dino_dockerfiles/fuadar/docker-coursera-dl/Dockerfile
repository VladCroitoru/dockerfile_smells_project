FROM oraclelinux:7-slim

VOLUME ["$PWD":/data]
WORKDIR /data
RUN yum-config-manager --enable ol7_latest ol7_developer ol7_addons ol7_developer_epel \
   &&  yum -y install python34 wget unzip  build-essential python-dev libssl-dev libffi-dev  \
   && rm -rf /var/cache/yum/*
RUN  wget https://bootstrap.pypa.io/get-pip.py 

RUN echo "export LC_ALL=en_US.UTF-8" >> ~/.bashrc
RUN echo  "export LANG=en_US.UTF-8" >> ~/.bashrc

ENV  LC_ALL en_US.UTF-8 
ENV  LANG en_US.UTF-8 

#COPY get-pip.py /data
RUN python3.4 get-pip.py
RUN pip3 install coursera-dl
 
CMD ["/bin/bash"]
