FROM ubuntu:latest

MAINTAINER Thomas Kilian

ENV DEBIAN_FRONTEND=noninteractive LANGUAGE=en_US:en LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 TERM=xterm

RUN echo "Hello Docker! Hello World!"

#########################################################
# Install Packages
#########################################################
#COPY target/sources.list /etc/apt/sources.list

RUN apt-get -q update --fix-missing && \
    apt-get -y upgrade && \
    apt-get -y install \
        vim \
        tmux \
        gcc \
        libc6-i386 `# /lib/ld-linux.so.2 for 32 bit support` \
        strace \
        netcat \
        telnet \
        gdb \
        htop \
        nmap \
        man-db \
        openssh-server \
        python python-dev \
        python3 python3-dev \
        git \
        golang \
        rustc \
        cargo \
        locales

# gdb-peda
RUN git clone https://github.com/longld/peda.git /home/me/peda && echo "source ~/peda/peda.py" >> /home/me/.gdbinit

RUN locale-gen en_US.UTF-8
RUN useradd -m -d /home/me -s /bin/bash me


#########################################################
# install vundle and plugins for vim
#########################################################
RUN git clone https://github.com/gmarik/Vundle.vim.git /home/me/.vim/bundle/Vundle.vim
COPY target/vimrc /home/me/.vimrc
COPY target/bashrc /home/me/.profile
RUN chown -R me:me /home/me/.vim /home/me/.vimrc
RUN su me -c 'vim -E -u /home/me/.vimrc -S /home/me/.vim/vundle.vim +PluginInstall +qall > /dev/null' || true


#########################################################
# create required folder for sshd
#########################################################
RUN mkdir /var/run/sshd && chmod 0755 /var/run/sshd


#########################################################
# CREATE FOLDERS AND PERMISSIONS SECTION
#########################################################
RUN mkdir /home/me/.ssh && chown -R me:me /home/me/ && mkdir /root/.ssh


#########################################################
# preparations for operation
#########################################################
EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]
