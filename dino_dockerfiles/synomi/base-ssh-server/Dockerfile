#based on garland/base-ssh-server, modified for Kuopio Hacklab's use. 

# Pull base image.
FROM ubuntu:15.04

RUN apt-get update
RUN apt-get install -y -q supervisor openssh-server nano irssi screen mysql-client
RUN mkdir -p /var/run/sshd

RUN apt-get autoremove && apt-get autoclean

# Output supervisor config file to start openssh-server
RUN echo "[program:openssh-server]" >> /etc/supervisor/conf.d/supervisord-openssh-server.conf
RUN echo "command=/usr/sbin/sshd -D" >> /etc/supervisor/conf.d/supervisord-openssh-server.conf
RUN echo "numprocs=1" >> /etc/supervisor/conf.d/supervisord-openssh-server.conf
RUN echo "autostart=true" >> /etc/supervisor/conf.d/supervisord-openssh-server.conf
RUN echo "autorestart=true" >> /etc/supervisor/conf.d/supervisord-openssh-server.conf

# Allow root login via password
# root password is: password
RUN sed -ri 's/PermitRootLogin without-password/PermitRootLogin yes/g' /etc/ssh/sshd_config

# Set root password
#password hash generated using this command: openssl passwd -1 -salt 123 xx
RUN sed -ri 's/root\:\*/root\:\$1\$123\$h1KrmyAdUSC7XnlWKCmKQ\./g' /etc/shadow

#update locale to finnish
RUN locale-gen fi_FI.UTF-8 && update-locale LANG=fi_FI.UTF-8
#set timezone to Helsinki
RUN cp /usr/share/zoneinfo/Europe/Helsinki /etc/localtime


EXPOSE 22

# Start supervisor
CMD ["/usr/bin/supervisord", "-n"]








