# sshd
#
# VERSION               1.0

FROM ubuntu:14.04

RUN apt-get update && apt-get install -y openssh-server && \
	rm -rf /var/lib/apt/lists/* && \
	mkdir /var/run/sshd

RUN usermod www-data -s /bin/bash -d /var/www/html && \
	echo 'www-data:123' | chpasswd

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
RUN echo "AllowUsers drupal"

ENV TERM xterm

# Set the locale
RUN locale-gen es_ES.UTF-8  
ENV LANG es_ES.UTF-8  
ENV LANGUAGE es_ES:en  
ENV LC_ALL es_ES.UTF-8

WORKDIR /var/www/html

ADD ./ssh-wrapper.sh /root/ssh-wrapper.sh
RUN chmod u+x /root/ssh-wrapper.sh

EXPOSE 22

CMD ["/root/ssh-wrapper.sh"]
