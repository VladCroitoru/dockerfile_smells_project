# IEEE 802.15.4 (Zigbee/Zwave/900MHz) Testing Tools Installed on Ubuntu
# Prerequists
#    Install VirtualBox Extension Pack for USB support: https://www.virtualbox.org/wiki/Downloads
#    Edit VirtualBox to permit USB 2.0 support. If necessary, select ATMEL Raven USB device.
# Run with Kitematic as it is easier to control for beginner
# 
FROM ubuntu:14.04
MAINTAINER cutawaysecurity@gmail.com

# Quick update
WORKDIR /
RUN apt-get update
RUN apt-get upgrade

# Install basic functionality for configuring and running tools
RUN apt-get install -y vim ipython git mercurial wget screen usbutils tcpdump tshark
WORKDIR /root
RUN wget https://gist.githubusercontent.com/cutaway/d69c1dcc868eb1896998/raw/3126fdf17cd911b1ead61b295d76dfb541ada26d/.vimrc
RUN wget https://gist.githubusercontent.com/cutaway/0ddfd31d993bf2f71378/raw/172f53c51a241fc9422df8b5cfc984d98ccd8ebf/.screenrc
RUN sed -i 's/home\/<user>/root/' .screenrc
RUN sed -i 's/shell -\${SHELL}/shell \/bin\/bash/' .screenrc
RUN mkdir screen_logs
# NOTE: To leverage screen within a Docker container shell use the following command
#       after SSHing to the docker machine.
# docker exec -i -t <image_id> bash -c "exec >/dev/tty 2>/dev/tty </dev/tty && /usr/bin/screen -s /bin/bash"

# Install Scapy-com from cutaway
RUN apt-get install -y python-gtk2 python-cairo python-usb python-crypto python-serial python-dev libgcrypt-dev
RUN mkdir Tools
WORKDIR /root/Tools
RUN hg clone https://bitbucket.org/cutsec/scapy-com
WORKDIR /root/Tools/scapy-com
RUN python setup.py install

# Install Killerbee
WORKDIR /root/Tools
RUN git clone https://github.com/riverloopsec/killerbee.git
WORKDIR /root/Tools/killerbee
RUN python setup.py install

# Install rfcat
WORKDIR /root/Tools
RUN hg clone https://bitbucket.org/atlas0fd00m/rfcat
WORKDIR /root/Tools/rfcat
RUN python setup.py install

# Install Killerzee
WORKDIR /root/Tools
RUN git clone https://github.com/joswr1ght/killerzee.git
WORKDIR /root/Tools/killerzee
RUN python setup.py install

# Install Zigbee Tools
WORKDIR /root/Tools
RUN git clone https://github.com/inguardians/zigbee_tools.git

# Reset Working Directory
WORKDIR /root
