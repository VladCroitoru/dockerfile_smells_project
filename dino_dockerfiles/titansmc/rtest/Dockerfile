FROM ubuntu
RUN apt-get update
RUN apt-get install -y wget 
RUN wge https://github.com/gravitational/teleport/releases/download/v1.3.2/teleport-v1.3.2-linux-amd64-bin.tar.gz
RUN tar -xzvf teleport-v1.3.2-linux-amd64-bin.tar.gz && cp teleport/tsh /usr/local/bin
RUN hostname
