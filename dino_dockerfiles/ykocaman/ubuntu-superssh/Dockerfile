FROM ubuntu
MAINTAINER ykocaman

#install Supervisor.
RUN \
  apt-get update && \
  apt-get install -y supervisor  --force-yes && \
  apt-get install -y openssh-server  --force-yes && \
  rm -rf /var/lib/apt/lists/* && \
  rm -rf /var/cache/apt/* && \
  sed -i 's/^\(\[supervisord\]\)$/\1\nnodaemon=true/' /etc/supervisor/supervisord.conf

#for ssh connecting adding user
RUN useradd -ms /bin/bash user

#adding sudoers
RUN adduser user sudo

#change password as "user"
RUN echo "user:user" | chpasswd

#for sshd process
RUN mkdir /var/run/sshd

#copy your id_rsa.pub to ssh/authorized_keys
RUN mkdir /home/user/.ssh
COPY ssh/authorized_keys /home/user/.ssh/
RUN chown user:user /home/user/.ssh -R

#copy conf of supervisor
COPY supervisor/conf.d /etc/supervisor/conf.d/

EXPOSE 22

#ENTRYPOINT ["/usr/bin/supervisord"] does not work.
# --> "Error: positional arguments are not supported"
# http://stackoverflow.com/questions/22465003/error-positional-arguments-are-not-supported
CMD ["/usr/bin/supervisord"]