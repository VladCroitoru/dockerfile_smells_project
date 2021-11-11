FROM ubuntu:17.04
MAINTAINER Sebastian Szwaczyk <sebastian.szwaczyk@wat.edu.pl>

RUN apt-get update && apt-get -y install sudo
RUN apt-get -y install openssl
RUN apt-get -y install libcap-ng-dev
RUN apt-get -y install apt-utils
RUN apt-get -y install net-tools
RUN apt-get install -y iputils-ping

#JAVA-install
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y  software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y && \
    apt-get update && \
    echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y oracle-java8-installer && \
    apt-get clean

#Mininet-install
COPY mininet /root/mininet
RUN cd /root/mininet && util/install.sh -nf

#OVS-install
COPY openvswitch-2.7.1 /root/openvswitch-2.7.1
RUN cd /root/openvswitch-2.7.1 && ./configure && make && make install
ENV PATH=$PATH:/usr/local/share/openvswitch/scripts

#Eclipse-install
COPY eclipse /home/student/eclipse

RUN apt-get -y install adwaita-icon-theme ant ant-optional binfmt-support dbus-x11 default-jdk default-jdk-headless default-jre default-jre-headless fastjar fontconfig gconf-service gconf-service-backend gconf2 gconf2-common gtk-update-icon-cache hicolor-icon-theme humanity-icon-theme jarwrapper junit junit4 libapache-pom-java \
  libart-2.0-2 libasm-java libasm3-java libasound2 libasound2-data libatk1.0-0 libatk1.0-data libavahi-client3 libavahi-common-data libavahi-common3 libavahi-glib1 libbonobo2-0 libbonobo2-common \
  libbonoboui2-0 libbonoboui2-common libcairo2 libcanberra0 libcglib-java libcommons-beanutils-java libcommons-cli-java libcommons-codec-java libcommons-collections3-java libcommons-compress-java \
  libcommons-dbcp-java libcommons-digester-java libcommons-httpclient-java libcommons-logging-java libcommons-parent-java libcommons-pool-java libcroco3 libcups2 libdatrie1 libdb-java libdb-je-java \
  libdb5.3-java libdb5.3-java-jni libeasymock-java libecj-java libequinox-osgi-java libfelix-bundlerepository-java libfelix-gogo-command-java libfelix-gogo-runtime-java libfelix-gogo-shell-java \
  libfelix-osgi-obr-java libfelix-shell-java libfelix-utils-java libgail-common libgail18 libgconf-2-4 libgdk-pixbuf2.0-0 libgdk-pixbuf2.0-bin libgdk-pixbuf2.0-common libglade2-0 libgnome-2-0 \
  libgnome-keyring-common libgnome-keyring0 libgnome2-common libgnomecanvas2-0 libgnomecanvas2-common libgnomeui-0 libgnomeui-common libgnomevfs2-0 libgnomevfs2-common libgraphite2-3 libgtk2.0-0 \
  libgtk2.0-bin libgtk2.0-common libhamcrest-java libharfbuzz0b libicu4j-4.2-java libicu4j-49-java libjbig0 libjetty9-java libjline-java libjpeg-turbo8 libjpeg8 libjsch-java libjtidy-java libjzlib-java \
  libkxml2-java liblucene2-java libobjenesis-java libogg0 liborbit-2-0 libosgi-annotation-java libosgi-compendium-java libosgi-core-java libpango-1.0-0 libpangocairo-1.0-0 libpangoft2-1.0-0 libpipeline1 \
  libpixman-1-0 libregexp-java librsvg2-2 librsvg2-common libservlet3.1-java libswt-cairo-gtk-3-jni libswt-glx-gtk-3-jni libswt-gnome-gtk-3-jni libswt-gtk-3-java libswt-gtk-3-jni libswt-webkit-gtk-3-jni \
  libtdb1 libthai-data libthai0 libtiff5 libtomcat8-java libvorbis0a libvorbisfile3 libxcb-render0 libxcb-shm0 libxcursor1 sat4j sound-theme-freedesktop ubuntu-mono

#Add student user
RUN adduser --disabled-password --gecos '' student
RUN echo student:student | chpasswd
RUN usermod -a -G sudo student
RUN echo "student ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/student && chmod 0440 /etc/sudoers.d/student
RUN cp /etc/skel/.bashrc /home/student & cp /etc/skel/.profile /home/student

#Add symlink to start eclipse
RUN ln -s /home/student/eclipse/eclipse /usr/bin/eclipse

#Floodlight
COPY floodlight /home/student/floodlight
RUN apt-get install -y build-essential maven
RUN mkdir /var/lib/floodlight
RUN chmod 777 /var/lib/floodlight
RUN cd /home/student/floodlight && ant eclipse

#Apache2 install
RUN apt-get -y install apache2

#Floodlight WEB-GUI
RUN rm /var/www/html/index.html
COPY floodlight-webui/ /var/www/html/

#Change persmissions for eclipse and floodlight
RUN cd /home/student && chown -R student .
RUN cd /home/student && chgrp -R student .

#Wireshark-install
RUN DEBIAN_FRONTEND=noninteractive apt-get install wireshark -y
RUN groupadd wireshark && usermod -a -G wireshark student && chgrp wireshark /usr/bin/dumpcap && chmod 750 /usr/bin/dumpcap && setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap

#Install text editors
RUN apt-get install gedit nano -y

#SET X11UseLocalhost=no
RUN echo 'X11UseLocalhost=no' >> /etc/ssh/sshd_config

#SET Xauthority for root user for correct authentication for X11 forwarding
RUN echo 'export XAUTHORITY=/home/student/.Xauthority' >> /etc/profile 

#Install CURL
RUN apt-get install -y curl

#RUN sshd and start OVS 
CMD service ssh start && service apache2 start && ovs-ctl start && bash


#RUN export uid=1000 gid=1000 && \
#    mkdir -p /home/student && \
#    echo "student:x:${uid}:${gid}:student,,,:/home/student:/bin/bash" >> /etc/passwd && \
#    echo "student:x:${uid}:" >> /etc/group && \
#    echo "student ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/student && \
#    chmod 0440 /etc/sudoers.d/student && \
#    chown ${uid}:${gid} -R /home/student



