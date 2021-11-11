FROM ubuntu:16.04
MAINTAINER Shisei Hanai<ruimo.uno@gmail.com>

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y wget

# Set nginx mainline repository
RUN cd /tmp && \
  wget http://nginx.org/keys/nginx_signing.key && \
  apt-key add nginx_signing.key

RUN echo "deb http://nginx.org/packages/mainline/ubuntu/ xenial nginx" >> /etc/apt/sources.list
RUN echo "deb-src http://nginx.org/packages/mainline/ubuntu/ xenial nginx" >> /etc/apt/sources.list

RUN apt-get update
RUN apt-get install -y nginx monit openssh-server w3m

ADD monit   /etc/monit/conf.d/

# This is a user for ssh login. Initial password = 'password'.
RUN useradd -p `perl -e "print(crypt('password', 'AB'));"` -s /bin/bash --create-home --user-group admin
RUN useradd -s /bin/false --create-home --user-group sshnginx

# Force to change password.
RUN passwd -e admin
RUN gpasswd -a admin sudo

# Use non standard port for ssh(22) to prevent atack.
# Prohibit password authentication.
RUN sed -i.bak \
  -e "s/Port 22/Port 2201/" \
  -e "s/^\s*PasswordAuthentication\(.*\)$/# PasswordAuthentication\1/" \
  /etc/ssh/sshd_config
RUN echo "PasswordAuthentication no" >> /etc/ssh/sshd_config

RUN mkdir /home/admin/.ssh
RUN mkdir /home/sshnginx/.ssh

ONBUILD ADD authorized_keys /home/admin/.ssh/authorized_keys
ONBUILD ADD authorized_keys /home/sshnginx/.ssh/authorized_keys

ONBUILD RUN chmod 755 /home/admin
ONBUILD RUN chmod 600 /home/admin/.ssh/authorized_keys
ONBUILD RUN chown -R admin:admin /home/admin/.ssh

ONBUILD RUN chmod 755 /home/sshnginx
ONBUILD RUN chmod 600 /home/sshnginx/.ssh/authorized_keys
ONBUILD RUN chown -R sshnginx:sshnginx /home/sshnginx/.ssh

EXPOSE 80
EXPOSE 443
EXPOSE 2201

RUN mkdir -p /var/log/nginx

CMD ["/usr/bin/monit", "-I", "-c", "/etc/monit/monitrc"]
