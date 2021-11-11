# FROM ubuntu:rolling
FROM ubuntu:16.04
# FROM ubuntu:18.04

MAINTAINER Mirek

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update -y && apt-get install -y aptitude && aptitude dist-upgrade --purge-unused -y && aptitude clean
RUN apt-get update && apt-get install -y software-properties-common python-software-properties python3-software-properties sudo

# install useful system apps
RUN apt-get install -y nano htop vim xterm ssh openssh-server curl wget git mc 

# install Open JDK 8 and 9
RUN apt-get install -y openjdk-8-jdk # openjdk-9-jdk 

RUN add-apt-repository universe
#RUN add-apt-repository ppa:ubuntubudgie/backports
# RUN add-apt-repository ppa:webupd8team/tor-browser
RUN apt-get update -y && apt-get install -y locales && \
  # RUN localedef -i en_IE -c -f UTF-8 -A /usr/share/locale/locale.alias en_IE.UTF-8
  localedef --force --inputfile=en_US --charmap=UTF-8 --alias-file=/usr/share/locale/locale.alias en_US.UTF-8

# ENV LANG en_IE.utf8
ENV LANG en_US.UTF-8
#ENV LANG="en_IE.UTF-8"
# ENV LANGUAGE=en_IE
ENV LANGUAGE=en_US


### set up user account
ENV NX_USER=nomachine
ENV NX_PASSWORD=nomachine
ENV NX_UID=1000
ENV NX_GID=1000

RUN groupadd -r $NX_USER -g $NX_GID && \
  useradd -u $NX_UID -r -g $NX_USER -d /home/$NX_USER -s /bin/bash -c "NX_$USER" $NX_USER && \
  # adduser $NX_USER sudo && \
  mkdir /home/$NX_USER && \
  chown -R $NX_USER:$NX_GID /home/$NX_USER && \
  echo $NX_USER':'$NX_PASSWORD | chpasswd


#RUN apt-get install -y ubuntu-gnome-desktop
#RUN apt-get install -y kubuntu-full kubuntu-restricted-addons kubuntu-restricted-extras
RUN apt-get install -y lubuntu-desktop lubuntu-restricted-addons lubuntu-restricted-extras
#RUN apt-get install -y ubuntu-budgie-desktop budgie-indicator-applet

#RUN apt-get install -y pulseaudio cups libgconf2-4 iputils-ping libnss3 libxss1 xdg-utils libpango1.0-0 fonts-liberation
# RUN apt-get install -y firefox libreoffice chromium-browser

# Chrome is not needed - Lubuntu has Firefox
# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add - 
# RUN sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
# RUN apt-get update -y && apt-get install -y google-chrome-stable

#http://docs.aws.amazon.com/directoryservice/latest/admin-guide/join_linux_instance.html
#RUN apt-get -y install sssd realmd krb5-user samba-common


### Data science tools for Python

# Spyder3 (latest version, not the old one bundled in with Lubuntu) 
RUN apt-get install -y python3-pip python3-pyqt4 python3-pyqt5 python3-pyqt5.qtsvg python3-pyqt5.qtwebkit && \
  pip3 install --upgrade pip && \
  pip install --upgrade setuptools && \
  pip install spyder

# PyCharm CE
RUN apt-get install -y software-properties-common && \
  add-apt-repository -y ppa:mystic-mirage/pycharm

RUN apt-get update -y && \ 
  apt-get install -y pycharm-community

# pandas, matplotlib
RUN pip install pandas matplotlib

# xgboost
# git clone --recursive https://github.com/dmlc/xgboost
# cd xgboost
# make -j4
RUN pip install xgboost



### CRAN R 

# ARG R_BASE_VER=3.4.4
ARG R_BASE_VER=3.5.0

# add to sources lists Michael Rutter's Launchpad repo with R-base 3.5 (RRutter v3.5)
RUN echo "deb [trusted=yes] http://ppa.launchpad.net/marutter/rrutter3.5/ubuntu xenial main" > /etc/apt/sources.list.d/rrutter3.5_xenial.list
# RUN echo "deb [trusted=yes] http://ppa.launchpad.net/marutter/rrutter3.5/ubuntu bionic main" > /etc/apt/sources.list.d/rrutter3.5_xenial.list

# add Michael Rutters key
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9

# Now install R-base[-dev] 3.5.0 from Michael Rutter's Launchpad repo
RUN apt-get update && apt-get install -y \
		r-base=${R_BASE_VER}-* \
		r-base-dev=${R_BASE_VER}-* \
		r-recommended=${R_BASE_VER}-*

### Data science tools for R

# RStudio
ENV RSTUDIO_VER=1.1.453

RUN wget --quiet -O /tmp/rstudio.deb https://download1.rstudio.org/rstudio-xenial-${RSTUDIO_VER}-amd64.deb && \
        chmod +x /tmp/rstudio.deb && \
        gdebi -n /tmp/rstudio.deb && \
        rm -rf /tmp/rstudio.deb


### NoMachine ###

# Goto https://www.nomachine.com/download/download&id=10 and update the latest 
# NOMACHINE_PACKAGE_NAME and MD5 sum:
# ENV NOMACHINE_PACKAGE_NAME nomachine_5.3.12_10_amd64.deb
# ENV NOMACHINE_MD5 78f25ceb145b1e6972bb6ad2c69bf689
# ENV NOMACHINE_PACKAGE_NAME nomachine_6.0.78_1_amd64.deb
# ENV NOMACHINE_BUILD 6.0
# ENV NOMACHINE_MD5 3645673090788ea0b2a3f664bb71a7dd
ENV NOMACHINE_PACKAGE_NAME nomachine_6.2.4_1_amd64.deb
ENV NOMACHINE_BUILD 6.2
ENV NOMACHINE_MD5 210bc249ec9940721a1413392eee06fe

# Install nomachine, change password and username to whatever you want here
RUN curl -fSL "http://download.nomachine.com/download/${NOMACHINE_BUILD}/Linux/${NOMACHINE_PACKAGE_NAME}" -o nomachine.deb \
&& echo "${NOMACHINE_MD5} *nomachine.deb" | md5sum -c - && dpkg -i nomachine.deb

# edit the Nomachine node configuration;
# caution: both node.cfg and server.cfg files 
# must be edited for the changes to take effect;
# define the location and names of the config files
ARG NX_NODE_CFG=/usr/NX/etc/node.cfg
ARG NX_SRV_CFG=/usr/NX/etc/server.cfg
# (note we edit the config files *[i]n place* (hence sed -i)
# and replace *[c]omplete* lines using "c\" switch):
# - replace the default desktop command (DefaultDesktopCommand) used by NoMachine with the preferred (lightweight) desktop
RUN sed -i '/DefaultDesktopCommand/c\DefaultDesktopCommand "/usr/bin/startlxde"' $NX_NODE_CFG
RUN sed -i '/DefaultDesktopCommand/c\DefaultDesktopCommand "/usr/bin/startlxde"' $NX_SRV_CFG

# # - replace the location of the nxserver log file, because the default one required sudo 
# # (but first create a new folder and empty logfile inside the user home folder)
# COPY nxserver.log /tmp
# RUN chown $NX_USER:$NX_GID /tmp/nxserver.log
# RUN sed -i "/SystemLogFile/c\SystemLogFile ${LOG_FOLDER}nxserver.log" $NX_NODE_CFG && \
# 	sed -i "/SystemLogFile/c\SystemLogFile ${LOG_FOLDER}nxserver.log" $NX_SRV_CFG

# # instead of blind editing using sed, simply edit the config files
# # outside the container (in git), and then copy them to the container
# COPY node.cfg /usr/NX/etc/node.cfg
# COPY server.cfg /usr/NX/etc/server.cfg

# add nx_user to sudoers file but only for startup of the nxserver service
RUN echo "${NX_USER} ALL=(ALL:ALL) NOPASSWD: /etc/NX/nxserver --startup" >> /etc/sudoers && \
	# add also nx_user to sudoers file but only for nxserver log monitoring
	echo "${NX_USER} ALL=(ALL:ALL) NOPASSWD: /usr/bin/tail -f /usr/NX/var/log/nxserver.log" >> /etc/sudoers

### Cleanup
#RUN apt-get autoclean \
#    && apt-get autoremove \
#    && rm -rf /var/lib/apt/lists/*

# listen to NX port (4000 by default)
# EXPOSE 22 4000
EXPOSE 4000
# EXPOSE 23 4001


# use environment variables USER and PASSWORD (passed by docker run -e) 
# to create a priviledged user account, and set it up for use by SSH and NoMachine;
# note that ADD is executed by the host, not the container (unlike RUN)
ADD nxserver.sh /

ENTRYPOINT ["/nxserver.sh"]

# Switch back to unpriviledged user (using its UID, not name) 
# to avoid accidental container runs as root
USER $NX_UID
