FROM ubuntu:latest
RUN apt update && \ 
	apt install -y software-properties-common && \
	apt-add-repository ppa:ansible/ansible && \
	apt update && \
	apt install -y ansible python-shade vim openssh-client && \
	apt clean

WORKDIR "/ansible"
ENTRYPOINT ["/bin/bash"]
