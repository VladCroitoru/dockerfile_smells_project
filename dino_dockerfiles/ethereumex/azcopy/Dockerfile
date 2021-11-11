FROM microsoft/dotnet:runtime

RUN apt-get update
RUN apt-get install -y rsync
RUN apt-get install -y wget

RUN mkdir -p /var/lib/azcopy
WORKDIR /var/lib/azcopy

RUN wget -O azcopy.tar.gz https://aka.ms/downloadazcopyprlinux
RUN tar -xf azcopy.tar.gz
RUN chmod 0755 install.sh
RUN ./install.sh

