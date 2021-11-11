FROM julia:latest

########################################################
# Essential packages for remote debugging and login in
########################################################

RUN apt-get update && apt-get upgrade -y && apt-get install -y \
    apt-utils gcc g++ openssh-server cmake build-essential gdb \
    gdbserver rsync vim locales
RUN apt-get install -y bzip2 wget gnupg dirmngr apt-transport-https \
	ca-certificates openssh-server tmux && \
    apt-get clean

#setup ssh
RUN mkdir /var/run/sshd && \
    echo 'root:new_pwd' |chpasswd && \
    sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' \
    /etc/ssh/sshd_config && \
    sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config && \
    mkdir /root/.ssh

#remove leftovers
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Expose 22 for ssh server. 7777 for gdb server.
EXPOSE 22 7777

# add user for debugging
RUN useradd -ms /bin/bash debugger
RUN echo 'debugger:debugger_pwd' | chpasswd

########################################################
# I do this separately
########################################################

CMD ["/usr/sbin/sshd", "-D"]

#add support for English 
COPY locale.gen /etc/locale.gen
RUN locale-gen
