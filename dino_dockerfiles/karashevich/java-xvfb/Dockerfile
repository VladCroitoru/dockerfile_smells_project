FROM ubuntu:latest

# Install VNC and xvfb
RUN apt-get update -y \
  && apt-get -y install \
    xvfb \
    x11vnc \
  && rm -rf /var/lib/apt/lists/* /var/cache/apt/*


#Update system
RUN apt-get update -qqy \
  && apt-get -qqy --no-install-recommends install \
    bzip2 \
    ca-certificates \
    default-jre \
    sudo \
    unzip \
    wget

#Install default JRE
RUN sudo apt-get -y install default-jre

#Install Fluxbox as a minimum X window manager
RUN sudo apt-get update -qqy && apt-get -y install fluxbox

#Expose port for Java debugging
EXPOSE 5009

ADD xinit.sh ./xinit.sh
RUN chmod +x ./xinit.sh

ENV DISPLAY :99