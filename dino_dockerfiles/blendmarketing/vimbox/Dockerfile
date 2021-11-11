FROM ubuntu:16.04
MAINTAINER Marc Tanis <marc@blendimc.com>

# Install Needed Software
RUN apt-get update  && \
apt-get install -y curl python-software-properties sudo apt-transport-https software-properties-common coreutils sysvinit-utils && \
add-apt-repository -yu ppa:pi-rho/dev && \
add-apt-repository ppa:neovim-ppa/stable && \
add-apt-repository ppa:mc3man/xerus-media && \
add-apt-repository ppa:longsleep/golang-backports && \
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add - && \
curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash - && \
add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable" && \
apt-key fingerprint 0EBFCD88 && \
apt-get update && \
apt-get install -y vim neovim tmux-next docker-ce nodejs iputils-ping unzip whois software-properties-common git dialog python3-pip golang-go openssh-server awscli jq && \ 
npm install -g yarn && \
rm -rf /var/lib/apt/lists/*

# Docker Compose
RUN curl -L https://github.com/docker/compose/releases/download/1.15.0/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose && \
chmod +x /usr/local/bin/docker-compose


# SSH
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
#sed -i 's|[#]*PasswordAuthentication yes|PasswordAuthentication no|g' /etc/ssh/sshd_config && \
#sed -i 's|UsePAM yes|UsePAM no|g' /etc/ssh/sshd_config
EXPOSE 22

# Setup Entrypoin
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Setup User
RUN groupadd -r user -g 1000 && \
useradd -u 1000 -r -g user -m -d /home/user -s /sbin/nologin -c "Dev User" user && \
usermod -a -G docker user && \
mkdir /home/user/go && \ 
chmod -R 755 /home/user && \
chown -R user:user /home/user  && \
chsh -s /bin/bash user && \
echo "user ALL=(root) NOPASSWD:ALL" > /etc/sudoers.d/user && \
chmod 0440 /etc/sudoers.d/user

USER user
WORKDIR /home/user

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/bin/bash"]

