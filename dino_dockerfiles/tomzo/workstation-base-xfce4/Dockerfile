FROM phusion/baseimage:0.9.17

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

RUN apt-get update && apt-get install -y dictionaries-common
RUN apt-get update && apt-get install -y xfce4 xfce4-terminal xfce4-goodies xfce4-taskmanager xfce4-screenshooter
RUN apt-get update && apt-get install -y lightdm lightdm-gtk-greeter gnome-icon-theme xubuntu-icon-theme file-roller ristretto
RUN apt-get update && apt-get install -y git gitk git-cola
RUN apt-get update && apt-get install -y subversion
RUN apt-get update && apt-get install -y mercurial

# start xfce4 desktop on container boot
RUN mkdir -p /etc/my_init.d
ADD startxfce4.sh /etc/my_init.d/50_startxfce4.sh
