# this docker file is used to try building a work environment
FROM centos:latest
MAINTAINER arthurkiller "arthur-lee@qq.com"

# setup develope envrionment
RUN yum -y install vim sudo gcc tmux openssh-server make cmake git tmux

RUN mkdir /var/run/sshd \
    &&  ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key \ 
    && ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key \

# 指定root密码
RUN echo toor | passwd root --stdin
RUN /bin/echo 'root:toor'|chpasswd

RUN /bin/sed -i 's/.*session.*required.*pam_loginuid.so.*/session optional pam_loginuid.so/g' /etc/pam.d/sshd
RUN sed -i "s/^#PermitRootLogin yes/PermitRootLogin yes/" /etc/ssh/sshd_config
RUN echo "export VISIBLE=now" >> /etc/profile
RUN /bin/echo -e "LANG=\"en_US.UTF-8\"" > /etc/default/local

# config git list tool
RUN git config --global alias.list "log --graph --all --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen<%aD> %Cred(%ad) %C(bold blue)<C:%cn%Creset %ci%C(bold blue)>%Creset' --abbrev-commit --date=relative"

# setup vim environment
RUN cd /root && git clone https://github.com/arthurkiller/vimrc.git && cd vimrc && make install
RUN git clone https://github.com/tony/tmux-config.git ~/.tmux && ln -s ~/.tmux/.tmux.conf ~/.tmux.conf

#set the time && add alias into profile
RUN echo 'alias ll="ls -lah --color=auto"' >> /etc/profile
RUN echo "Asia/shanghai" > /etc/timezone
RUN cp /usr/share/zoneinfo/PRC /etc/localtime

#start the sshd server
EXPOSE 22
CMD /usr/sbin/sshd -D
