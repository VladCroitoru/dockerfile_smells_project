FROM debian:8.2
MAINTAINER erdii <erdii@nym.hush.com>

# Update and install oh-my-zsh dependencies and some tools
RUN apt-get update && apt-get install -y openssh-server wget git zsh build-essential nano

# Install oh-my-zsh
RUN git clone git://github.com/robbyrussell/oh-my-zsh.git ~/.oh-my-zsh \
      && cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc \
      && chsh -s /bin/zsh

# enable ssh server
RUN mkdir /var/run/sshd

# set credentials
RUN echo "root:screencast" | chpasswd

# enable root password login
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

EXPOSE 22

# run ssh server
CMD ["/usr/sbin/sshd", "-D"]
