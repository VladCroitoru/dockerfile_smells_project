from ubuntu:latest

ENV HOME /packetbeat-setup

ADD setup.sh $HOME/
ADD scripts/* $HOME/scripts/
ADD https://raw.githubusercontent.com/packetbeat/packetbeat/master/packetbeat.template.json $HOME/
ADD packetbeat-kibana $HOME/packetbeat-kibana

# download latest docker client
RUN apt-get update && \
	apt-get install -y curl && \
	apt-get clean && rm -rf /var/lib/apt/lists/* && \
	curl https://get.docker.io/builds/Linux/x86_64/docker-1.3.0 -o /usr/local/bin/docker && \
    chmod +x /usr/local/bin/docker $HOME/setup.sh $HOME/scripts/*

ENTRYPOINT ["/bin/bash", "-c", "$HOME/setup.sh"]
