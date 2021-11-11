FROM debian:buster-slim

# NOTE: If you don't run the mkdir -p /usr/share/man/man1 /usr/share/man/man2 you'll run into dependency problems with ca-certificates, 
# openjdk-11-jre-headless etc. 
# I've been using this fix provided by community, haven't really checked the permanent fix.
# https://stackoverflow.com/questions/61815233/install-java-runtime-in-debian-based-docker-image
RUN mkdir -p /usr/share/man/man1 /usr/share/man/man2

# culr (optional) for downloading/browsing stuff
# openssh-client (required) for creating ssh tunnel
# psmisc (optional) I needed it to test port binding after ssh tunnel (eg: netstat -ntlp | grep 6443)
# nano (required) buster-slim doesn't even have less. so I needed an editor to view/edit file (eg: /etc/hosts) 


RUN apt-get update && apt-get install -y \
	apt-transport-https \
	ca-certificates \
	curl \
	unzip \
    openssh-client \
	psmisc \
	nano \
	net-tools \
	openjdk-11-jre \
	&& curl -L https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
	&& chmod +x /usr/local/bin/kubectl

RUN curl -o /usr/local/bin/jq -L https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 && \
  	chmod +x /usr/local/bin/jq

# COPY .ssh/id_rsa /root/.ssh/
# RUN chmod 600 /root/.ssh/id_rsa

# COPY binaries/kubectl-vsphere /usr/local/bin/ 
# RUN chmod +x /usr/local/bin/kubectl-vsphere

# COPY binaries/tmc /usr/local/bin/
# RUN chmod +x /usr/local/bin/tmc

COPY binaries/init.sh /usr/local/
RUN chmod +x /usr/local/init.sh

ENTRYPOINT [ "/usr/local/init.sh" ]