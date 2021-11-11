FROM ubuntu
MAINTAINER Marchand D. https://github.com/marchandd/vncxvfb_wine_firefox
ENV VE_version="MarchandD_20151117_v02.01" 
# i386 usage
RUN dpkg --add-architecture i386
# Install vnc, xvfb in order to create a 'fake' display and firefox
RUN apt-get update -y && apt-get install -y x11vnc xvfb firefox pwgen
# Add ppa
RUN apt-get update -y && apt-get install -y bash software-properties-common && add-apt-repository -y ppa:ubuntu-wine/ppa
# Install wine dev version and config, supervisor
RUN apt-get update -y && apt-get install -y wine1.7:i386 cabextract winetricks supervisor
# update and clean
RUN apt-get update -y && apt-get purge -y python-software-properties &&apt-get autoclean -y
# Copy user password script from local to root and run it
COPY ./vnc-password.sh /root/
RUN chmod 755 /root/*.sh
RUN bash -c '/root/vnc-password.sh'
# Supervisor settings x11vnc for always listener, prompt passwd, FINDCREATEDISPLAY xvfb by default
COPY ./supervisor/supervisor.conf /etc/supervisor/supervisor.conf
RUN chmod 775 /etc/supervisor/*.conf
COPY ./supervisor/x11vnc-xvfb.conf /etc/supervisor/conf.d/
RUN chmod 775 /etc/supervisor/conf.d/x11vnc-xvfb.conf
# Port to expose x11vnc
EXPOSE 5900
# Directory ready
WORKDIR /etc/supervisor
# Supervisor daemon
CMD supervisord -c /etc/supervisor/supervisor.conf