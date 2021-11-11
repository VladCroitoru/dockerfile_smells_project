FROM ubuntu:16.04

RUN apt-get update && apt-get install git lsof net-tools inetutils-ping build-essential libgl1 vim screen torque-mom torque-pam torque-client torque-server torque-scheduler wget curl hdf5-tools -y ; rm -rf /var/lib/apt/lists/*
RUN echo 'root:root' | chpasswd

#Add start script for torque
ADD startup.sh /
RUN chmod +x /startup.sh

#Add user
RUN useradd -ms /bin/bash icuser
RUN echo 'icuser:icpass' | chpasswd

#Create directories
RUN mkdir -p /software/ /analysis
RUN chown icuser:icuser /software /analysis
USER icuser

#Data files
RUN mkdir -p /analysis/4730/hdf5/data
ADD data/*h5 /analysis/4730/hdf5/data/

WORKDIR /home/icuser

#Install miniconda
ADD setup_conda_and_env.sh .
RUN bash setup_conda_and_env.sh

USER root
CMD /startup.sh; su icuser; /bin/bash

