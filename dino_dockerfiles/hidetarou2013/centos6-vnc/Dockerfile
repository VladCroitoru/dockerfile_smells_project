FROM centos:6
MAINTAINER hidetarou2013 <hidetoshi_maekawa@e-it.co.jp>

#----------------------------
# tigervnc-server
#----------------------------
USER root
ENV DISPLAY "" 
RUN yum update -y && yum install -y tigervnc-server \
                   xorg-x11-server-utils \
                   xorg-x11-server-Xvfb \
                   xorg-x11-fonts-Type1 \
                   xorg-x11-fonts-misc \
                   xorg-x11-fonts-75dpi \
                   xorg-x11-fonts-100dpi \
                   xterm \
                   gnome-session && yum clean all; rm -rf /var/cache/yum

RUN /bin/dbus-uuidgen --ensure

#----------------------------
# kioskuser
#----------------------------
RUN useradd kioskuser; mkdir -p /home/kioskuser/.vnc
RUN echo kioskuser | passwd --stdin kioskuser
ADD xstartup /home/kioskuser/.vnc/
ADD passwd /home/kioskuser/.vnc/
RUN chown -R kioskuser:kioskuser /home/kioskuser; chmod 775 /home/kioskuser/.vnc/xstartup; chmod 600 /home/kioskuser/.vnc/passwd

EXPOSE 5901

#----------------------------
# ipa font
#----------------------------
RUN yum update -y && yum install -y ipa-mincho-fonts \
    ipa-gothic-fonts \
    ipa-pmincho-fonts \
    ipa-pgothic-font \
    gnome-session && yum clean all; rm -rf /var/cache/yum

#----------------------------
# japanese + GUI
#----------------------------
USER root
RUN yum reinstall -y glibc-common
ENV LANG ja_JP.utf8
RUN yum -y groupinstall "X Window System"
RUN yum -y groupinstall "GNOME Desktop Environment"
RUN yum groupinstall -y 'Desktop'
RUN yum groupinstall -y fonts
RUN yum groupinstall -y "Japanese Support" 
RUN sed -i -e 's/LANG=\"en_US.UTF-8\"/#LANG=\"en_US.UTF-8\"/g' /etc/sysconfig/i18n
RUN echo "LANG=\"ja_JP.UTF-8\"" >> /etc/sysconfig/i18n
RUN echo "SYSFONT=\"latarcyrheb-sun16\"" >> /etc/sysconfig/i18n

#----------------------------
# keyboard
#----------------------------
RUN sed -i -e 's/KEYTABLE=\"us\"/KEYTABLE=\"jp106\"/g' /etc/sysconfig/keyboard 
RUN sed -i -e 's/MODEL=\"pc105+inet\"/MODEL=\"jp106\"/g' /etc/sysconfig/keyboard 
RUN sed -i -e 's/LAYOUT=\"us\"/LAYOUT=\"jp\"/g' /etc/sysconfig/keyboard



ENTRYPOINT ["/usr/bin/vncserver","-fg"]
