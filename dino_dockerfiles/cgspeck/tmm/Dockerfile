# tinyMediaManager 
FROM hurricane/dockergui:x11rdp1.3
MAINTAINER Carlos Hernandez <carlos@techbyte.ca>

#########################################
##        ENVIRONMENTAL CONFIG         ##
#########################################
# Set correct environment variables
ENV LC_ALL="C.UTF-8" LANG="en_US.UTF-8" LANGUAGE="en_US.UTF-8" 
ENV APP_NAME tinyMediaManager


# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

#########################################
##         RUN INSTALL SCRIPT          ##
#########################################
COPY ./files/ /tmp/

#########################################
##         INSTALL LIBMEDIAINFO        ##
#########################################
RUN apt-get update
RUN apt-get install -y libmediainfo0

#########################################
## INSTALL DIRECTLY FROM RELEASE PAGE  ##
#########################################
RUN mkdir /tinyMediaManager
RUN wget https://release.tinymediamanager.org/dist/tmm_2.9.2_4c5fcb0_linux.tar.gz -O /tmp/tinyMediaManager.tar.gz
RUN tar -zxvf /tmp/tinyMediaManager.tar.gz -C /tinyMediaManager

RUN chmod +x /tmp/install/tmm_install.sh && /tmp/install/tmm_install.sh && rm -r /tmp/install

#########################################
##         EXPORTS AND VOLUMES         ##
#########################################
VOLUME ["/config"]
EXPOSE 3389 8080
