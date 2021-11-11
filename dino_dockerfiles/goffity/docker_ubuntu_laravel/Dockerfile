FROM ubuntu

MAINTAINER Goffity Corleone

RUN apt-get update && apt-get upgrade -y

RUN apt-get install -y curl wget build-essential php php-cli php-curl php-xml php-mbstring php-zip git zip unzip nginx

RUN curl -sS https://getcomposer.org/installer -o composer-setup.php

RUN php -r "if (hash_file('SHA384', 'composer-setup.php') === '669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"

RUN php composer-setup.php --install-dir=/usr/local/bin --filename=composer

RUN apt-get update && apt-get install -y openssh-server

RUN mkdir /var/run/sshd

RUN echo 'root:screencast' | chpasswd

RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22 80

CMD ["/usr/sbin/sshd", "-D"]
