FROM ubuntu
MAINTAINER John Sanabria - john.sanabria@gmail.com
ENV user opencpu
RUN apt-get install -y software-properties-common
RUN add-apt-repository -y ppa:opencpu/opencpu-1.5
RUN useradd -m -p "pa7.iYd6RO4JU" -s /bin/bash ${user} # passwd 'opencpu'
RUN usermod -aG sudo ${user}
RUN apt-get update  
RUN export DEBIAN_FRONTEND=noninteractive ; apt-get install -y opencpu
USER ${user}
