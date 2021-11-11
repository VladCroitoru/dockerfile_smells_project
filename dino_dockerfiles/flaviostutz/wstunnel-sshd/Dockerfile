FROM nodesource/trusty:6.3.0
# FROM node:9.3.0-wheezy

RUN apt-get update
RUN apt-get install -y ed ssh openssh-server openssh-client supervisor python-pyinotify

# google authenticator
RUN apt-get install libqrencode3 -y
RUN cd /tmp && wget http://ftp.us.debian.org/debian/pool/main/g/google-authenticator/libpam-google-authenticator_20130529-2_amd64.deb
RUN dpkg -i /tmp/libpam-google-authenticator_20130529-2_amd64.deb && rm /tmp/libpam-google-authenticator_20130529-2_amd64.deb

RUN apt-get clean

# Config SSHD
RUN sed -i '2i auth required pam_google_authenticator.so nullok' /etc/pam.d/sshd
RUN sed -i 's/ChallengeResponseAuthentication no/ChallengeResponseAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/UsePrivilegeSeparation yes/UsePrivilegeSeparation no/' /etc/ssh/sshd_config
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
# RUN sed -ri 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config

# Config wstunnel
RUN npm install -g wstunnel

ADD sshd-supervisor.sh /usr/local/bin/
ADD wstunnel-supervisor.sh /usr/local/bin/
ADD supervisor.d/* /etc/supervisor/conf.d/
RUN mkdir -p /var/run/sshd /var/log/supervisor /root/.ssh

CMD ["/usr/bin/supervisord","-c","/etc/supervisor/supervisord.conf"] 

ENV GOOGLE_AUTHENTICATOR_ENABLE  false
ENV ROOT_PASSWORD                root123

EXPOSE 22 80
