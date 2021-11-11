FROM ubuntu
MAINTAINER Marchand D. https://github.com/marchandd/term_ssh_user_firefox
ENV VE_version="MarchandD_20151117_v02.01" 
RUN apt-get update && apt-get install -y openssh-server firefox supervisor dbus-x11 pwgen
RUN mkdir /var/run/sshd
# Copy user script from local to root and run it
COPY ./usercreation.sh /
RUN chmod 755 /*.sh
RUN bash -c '/usercreation.sh'
# Supervisor settings for ssl
COPY ./supervisor/supervisor.conf /etc/supervisor/supervisor.conf
RUN chmod 775 /etc/supervisor/*.conf
COPY ./supervisor/ssl.conf /etc/supervisor/conf.d/
RUN chmod 775 /etc/supervisor/conf.d/ssl.conf
# SSL port
EXPOSE 22
# Directory ready
WORKDIR /etc/supervisor
# Supervisor daemon
CMD supervisord -c /etc/supervisor/supervisor.conf
