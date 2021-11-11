FROM gawbul/docker-ubuntu1604-base

RUN mkdir -p /opt/tools

WORKDIR /opt/tools

# install fastqc
RUN \
  wget -c http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip && \
  unzip fastqc_v0.11.5.zip && \
  cd FastQC && \
  chmod +x fastqc && \
  cp fastqc /usr/local/bin
