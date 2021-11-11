FROM debian:buster-slim

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
	less \
	net-tools \
	&& curl -L https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
	&& chmod +x /usr/local/bin/kubectl

# COPY .ssh/id_rsa /root/.ssh/
# RUN chmod 600 /root/.ssh/id_rsa

RUN curl -o /usr/local/bin/jq -L https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 && \
  	chmod +x /usr/local/bin/jq

COPY binaries/tanzu-cluster.template /usr/local/ 
RUN chmod +x /usr/local/tanzu-cluster.template

# COPY binaries/kubectl-vsphere /usr/local/bin/ 
# RUN chmod +x /usr/local/bin/kubectl-vsphere

# COPY binaries/tmc /usr/local/bin/ 
# RUN chmod +x /usr/local/bin/tmc

COPY binaries/init.sh /usr/local/ 
RUN chmod +x /usr/local/init.sh

ENTRYPOINT ["/usr/local/init.sh"]