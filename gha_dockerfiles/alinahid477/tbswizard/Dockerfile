FROM debian:buster-slim

# culr (optional) for downloading/browsing stuff
# openssh-client (required) for creating ssh tunnel
# psmisc (optional) I needed it to test port binding after ssh tunnel (eg: netstat -ntlp | grep 6443)
# nano (required) buster-slim doesn't even have less. so I needed an editor to view/edit file (eg: /etc/hosts) 
# libdigest-sha-perl needed to execute carvel/install.sh
# stern for looking at log across multiple k8s pods
RUN apt-get update && apt-get install -y \
	apt-transport-https \
	ca-certificates \
	unzip \
	curl \
    openssh-client \
	psmisc \
	nano \
	net-tools \
	libdigest-sha-perl \
	&& curl -L https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl -o /usr/local/bin/kubectl \
	&& chmod +x /usr/local/bin/kubectl \
	&& curl -L https://github.com/wercker/stern/releases/download/$(curl -s https://api.github.com/repos/wercker/stern/releases/latest | grep tag_name | cut -d '"' -f 4)/stern_linux_amd64 -o /usr/local/bin/stern \
	&& chmod +x /usr/local/bin/stern

RUN curl -o /usr/local/bin/jq -L https://github.com/stedolan/jq/releases/download/jq-1.6/jq-linux64 && \
  	chmod +x /usr/local/bin/jq

ENV DOCKERVERSION=20.10.8
RUN curl -fsSLO https://download.docker.com/linux/static/stable/x86_64/docker-${DOCKERVERSION}.tgz \
	&& tar xzvf docker-${DOCKERVERSION}.tgz --strip 1 \
					-C /usr/local/bin docker/docker \
	&& rm docker-${DOCKERVERSION}.tgz
# RUN curl -sSL https://get.docker.com/ | sh

# RUN curl -L https://raw.githubusercontent.com/alinahid477/VMW/main/tbs/carvel/install.sh | bash
RUN curl -L https://carvel.dev/install.sh | bash




COPY binaries/builder.template /usr/local/

COPY binaries/init.sh /usr/local/
COPY binaries/kp /usr/local/bin/ 
RUN chmod +x /usr/local/bin/kp && chmod +x /usr/local/init.sh

# COPY .ssh/id_rsa /root/.ssh/
# RUN chmod 600 /root/.ssh/id_rsa

# COPY binaries/tmc /usr/local/bin/
# RUN chmod +x /usr/local/bin/tmc

# COPY binaries/kubectl-vsphere /usr/local/bin/ 
# RUN chmod +x /usr/local/bin/kubectl-vsphere

ENTRYPOINT [ "/usr/local/init.sh"]