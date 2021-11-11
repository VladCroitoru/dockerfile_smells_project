FROM ubuntu:15.10

RUN apt-get update && apt-get install -y \
	openssh-server \
	vim \
	git \
	zsh \
	sudo \
	net-tools \
	iputils-ping \
	iperf \
	htop \
	iftop \
	curl \
	httpie \
	python-pip \
	postgresql-client

RUN pip install butterfly
	
RUN useradd -ms /usr/bin/zsh kaskada && adduser kaskada sudo && echo 'kaskada ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && echo 'kaskada:toolbox' | chpasswd && echo 'Defaults !secure_path' >> /etc/sudoers

RUN echo "LANGUAGE=en_US.UTF-8\nLANG=en_US.UTF-8\nLC_ALL=en_US.UTF-8\nPATH=$PATH:/host/usr/bin:/host/usr/local/bin" >> /etc/environment && locale-gen en_US.UTF-8 && dpkg-reconfigure locales

RUN mkdir /var/run/sshd

ADD run.sh /opt/run.sh

USER kaskada
WORKDIR /home/kaskada

RUN git clone https://github.com/robbyrussell/oh-my-zsh.git .oh-my-zsh
ADD .zshrc .zshrc
ADD .box-name .box-name

EXPOSE 22 57575

VOLUME ["/host/usr", "/var/run/docker.sock"]

ENTRYPOINT ["/bin/bash", "-c", "/opt/run.sh"]
