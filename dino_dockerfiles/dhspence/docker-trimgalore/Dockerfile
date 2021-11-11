FROM dhspence/docker-baseimage:latest

# File Author / Maintainer
MAINTAINER David Spencer <dspencer@wustl.edu>

# Install cutadapt 
WORKDIR /opt/

RUN wget https://github.com/ComputationalSystemsBiology/EoulsanDockerFiles/raw/master/TrimAdapt/cutadapt-1.8.1.tar.gz

RUN tar -xzf cutadapt-1.8.1.tar.gz && \
    ln -s /opt/cutadapt-1.8.1/bin/cutadapt /usr/local/bin/
    
RUN wget https://github.com/s-andrews/FastQC/archive/v0.11.8.tar.gz && \
    tar -zxf v0.11.8.tar.gz && \
    ln -s /opt/FastQC*/fastqc /usr/local/bin/

# Install Trim_Galore

RUN wget https://github.com/ComputationalSystemsBiology/EoulsanDockerFiles/raw/master/TrimAdapt/trim_galore_v0.4.1.zip

RUN apt-get install unzip

RUN unzip trim_galore_v0.4.1.zip -d .
RUN ln -s /opt/trim_galore_zip/trim_galore /usr/local/bin/


