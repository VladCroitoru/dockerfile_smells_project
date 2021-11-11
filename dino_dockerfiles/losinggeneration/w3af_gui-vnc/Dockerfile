FROM losinggeneration/w3af_gui:latest
MAINTAINER Harley Laue <losinggeneration@gmail.com>

# We need the local apt database up-to-date
RUN apt-get update -y

# Packages for remote usage
RUN apt-get install -y tightvncserver openbox

USER $USER
WORKDIR $HOME

# Add the VNC password
RUN mkdir -m 700 .vnc
ADD vnc/password $HOME/vnc.passwd
RUN vncpasswd -f < vnc.passwd > .vnc/passwd
RUN chmod 700 .vnc/passwd
RUN rm vnc.passwd

# Run w3af_gui with Xvnc
RUN echo "openbox &; /home/$USER/w3af/w3af_gui" > .xsession
RUN chmod +x .xsession

USER root

# Expose VNC
EXPOSE 5901

# Add the start script to /start.sh
ADD start.sh /start.sh

# Run Xvnc & tail the VNC logs
ENTRYPOINT /start.sh
