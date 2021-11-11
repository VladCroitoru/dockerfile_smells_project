FROM ubuntu
MAINTAINER Marchand D. https://github.com/marchandd/term_ssh_root_wine
ENV VE_version="MarchandD_20151117_v02.01" 
# i386 usage
RUN dpkg --add-architecture i386
RUN apt-get update && apt-get install -y openssh-server firefox supervisor dbus-x11 pwgen
# Add ppa
RUN apt-get update -y && apt-get install -y bash software-properties-common && add-apt-repository -y ppa:ubuntu-wine/ppa
# Install wine dev version and config
RUN apt-get update -y && apt-get install -y wine1.7:i386 cabextract winetricks
# update and clean
RUN apt-get update -y && apt-get purge -y python-software-properties &&apt-get autoclean -y
RUN mkdir /var/run/sshd
# Copy root privileges script from local to ve and run it
COPY ./root_privileges.sh /
RUN chmod 755 /*.sh
RUN bash -c '/root_privileges.sh'
# Supervisor settings for ssl
COPY ./supervisor/supervisor.conf /etc/supervisor/supervisor.conf
RUN chmod 775 /etc/supervisor/*.conf
COPY ./supervisor/ssl.conf /etc/supervisor/conf.d/
RUN chmod 775 /etc/supervisor/conf.d/ssl.conf
# SSL port
EXPOSE 22
# Copy install scripts from local to /usr/local/sbin
COPY scripts/_installFirst_winetricksOptions.sh /usr/local/sbin/
RUN chmod 755 /usr/local/sbin/*.sh
# Directory ready
WORKDIR /etc/supervisor
# Supervisor daemon
CMD supervisord -c /etc/supervisor/supervisor.conf
