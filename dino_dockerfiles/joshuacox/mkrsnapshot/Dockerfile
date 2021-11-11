FROM debian:jessie
LABEL maintainer="Josh Cox <josh 'at' http://webhosting coop/>"

ENV PARALLEL_JOBS 4
ENV SHELL /bin/bash

RUN apt-get update && apt-get install -yqq --no-install-recommends autossh curl rsync bzip2 unzip zip time parallel rsnapshot; \
apt-get -y autoremove ; \
apt-get clean ; \
rm -Rf /var/lib/apt/lists/*

RUN mkdir /var/run/sshd
# RUN echo 'root:screencast' | chpasswd
# RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
# RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

# ENV NOTVISIBLE "in users profile"
# RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
VOLUME /home/ssh
COPY ./start.sh /start.sh
RUN chmod 755 /start.sh
CMD ["/start.sh"]
