FROM ubuntu:14.04
MAINTAINER frok

# mkdirs
RUN mkdir /home/downloads
RUN mkdir /home/workspace
RUN mkdir /etc/frok

# add files from repo
ADD /start.sh /start.sh
RUN chmod 755 /start.sh

# network configuration
EXPOSE 27015 27016 27017 27018 27019 27020 27021 27022 8080 4848 22 80

# installing via apt-get
RUN apt-get clean
RUN apt-get update
RUN apt-get -y dist-upgrade
RUN apt-get install -y default-jre
RUN apt-get install -y default-jdk
RUN apt-get install -y gcc
RUN apt-get install -y g++
RUN apt-get install -y git
RUN apt-get install -y cmake
RUN apt-get install -y libgtk2.0-dev
RUN apt-get install -y unzip
RUN apt-get install -y wget
RUN apt-get install -y maven

# dl with wget
RUN wget -P /home/downloads/ download.java.net/glassfish/4.0/release/glassfish-4.0.zip
RUN wget -P /home/downloads/ http://downloads.sourceforge.net/project/opencvlibrary/opencv-unix/2.4.9/opencv-2.4.9.zip

# install opencv 2.4.9
RUN unzip /home/downloads/opencv-2.4.9.zip -d /opt
RUN mkdir /opt/opencv-2.4.9/static
RUN cd /opt/opencv-2.4.9 && cmake -D CMAKE_BUILD_TYPE=RELEASE -D BUILD_SHARED_LIBS=NO -D CMAKE_INSTALL_PREFIX=/opt/opencv-2.4.9/static -D WITH_QT=NO ./
RUN cd /opt/opencv-2.4.9 && make -j 8
RUN cd /opt/opencv-2.4.9 && make -j 8  install

# install glassfish 4.0
RUN unzip /home/downloads/glassfish-4.0.zip -d /opt

# clone projects
RUN cd /home/workspace && git clone --depth 1 https://github.com/dmedov/frok-server.git
RUN cd /home/workspace && git clone --depth 1 https://github.com/dmedov/frok-download-server.git

# build frok-server
RUN cd /home/workspace/frok-server/build && make -j 8 CFG=debug CCFLAG+=-DNO_DAEMON CCFLAG+=-DFAST_SEARCH_ENABLED build
RUN cd /home/workspace/frok-server/build && make -j 8 CCFLAG+=-DFAST_SEARCH_ENABLED CCFLAG+=-DNO_DAEMON CFG=release build
RUN touch /var/log/frok.log
RUN touch /etc/frok/frok.conf
RUN echo "OUTPUT_FILE = /var/log/frok.log" > /etc/frok/frok.conf
RUN echo "PHOTO_BASE_PATH = /home/faces/" >> /etc/frok/frok.conf
RUN echo "TARGET_PHOTOS_PATH = /home/faces/" >> /etc/frok/frok.conf
RUN chmod 664 /etc/frok -R

# build frok-download server
RUN cd /home/workspace/frok-download-server/ && mvn package
RUN touch /etc/frok/frok.conf
RUN echo "FROK_SERVER = 127.0.0.1:27015" > /etc/frok/frok-ds.conf
RUN echo "PHOTO_BASE_PATH = /home/faces/" >> /etc/frok/frok-ds.conf
RUN echo "TARGET_PHOTOS_PATH = /home/faces/" >> /etc/frok/frok-ds.conf
RUN chmod 664 /etc/frok -R

# process clean up
RUN rm /home/downloads -r
