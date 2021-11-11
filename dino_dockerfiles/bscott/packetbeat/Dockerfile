FROM dockerfile/elasticsearch
MAINTAINER Brian L. Scott "Brainscott@gmail.com"
RUN apt-get install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:letmein' |chpasswd
RUN sudo apt-get install curl -y
RUN echo "Installing Kibana..."
WORKDIR /data RUN curl -L -O https://github.com/packetbeat/kibana/releases/download/v3.0.0-pb/kibana-3.0-packetbeat.tar.gz
WORKDIR /data RUN tar -xzvf kibana-3.0-packetbeat.tar.gz
WORKDIR /data RUN cd kibana-3.0-packetbeat

EXPOSE 8000
EXPOSE 9200
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
CMD ["python", "-m", "/data/kibana-3.0-packetbeat/SimpleHTTPServer"]
