# DebiaNVM
FROM debian:jessie
MAINTAINER houjie <deffyc@gmail.com>

RUN apt update && \
    apt install -y sudo && \
   # rm -rf /var/lib/apt/lists/* && \
    apt install -y curl wget vim    

#Optional variables defaults

ARG user=c9
ARG pass=rules


ENV user $user
ENV pass $pass

RUN echo "Creating user ${user}:${pass}"

RUN useradd --create-home --no-log-init --shell /bin/bash $user
RUN adduser $user sudo
RUN echo ${user}:${pass} | chpasswd

# Sudo without password
RUN echo "#!/usr/bin/env bash" > /bin/visudoset
RUN echo "echo \"${user} ALL=(ALL) NOPASSWD: ALL\" >> \$1" >> /bin/visudoset
RUN chmod a+x /bin/visudoset
RUN EDITOR=visudoset visudo
RUN rm -f /bin/visudoset

USER $user
WORKDIR /home/$user


RUN curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.31.6/install.sh | bash
