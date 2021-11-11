
FROM nimbix/ubuntu-desktop:trusty
MAINTAINER stephen.fox@nimbix.net

RUN apt-get update && \
    apt-get install -y curl && \
    apt-get install -y make && \ 
    apt-get install -y gfortran && \

    apt-get -y install software-properties-common python-software-properties && \

    wget -O- -q http://s3tools.org/repo/deb-all/stable/s3tools.key | apt-key add - && \
    wget -O/etc/apt/sources.list.d/s3tools.list http://s3tools.org/repo/deb-all/stable/s3tools.list && \
    apt-get update && \
    apt-get install s3cmd 

WORKDIR /home/nimbix
RUN /usr/bin/wget https://s3.amazonaws.com/yb-lab-cfg/admin/yb-admin.NIMBIX.x86_64.tar \
&& tar xvf yb-admin.NIMBIX.x86_64.tar -C /usr/bin \
&& apt-get install -y tcl \
&& apt-get install -y git \
&& apt-add-repository ppa:octave/stable \
&& apt-get update \
&& apt-get install -y octave \
&& apt-get build-dep -y octave 


# Install R + RStudio on Ubuntu 14.04

RUN sudo apt-get install -y r-base \
&& sudo apt-get install -y r-base-dev 
RUN sudo apt-get install -y gdebi-core 
RUN /usr/bin/wget https://download2.rstudio.org/rstudio-server-1.1.442-amd64.deb 
RUN echo "y" |sudo gdebi rstudio-server-1.1.442-amd64.deb 
RUN rm rstudio-server-1.1.442-amd64.deb 


RUN mkdir -p /opt/images \
&& mkdir -p /opt/icons \
&& apt-get install -y awscli

RUN echo "auth-minimum-user-id=500" >> /etc/rstudio/rserver.conf


ADD ./scripts /usr/local/scripts

# Add PushToCompute Work Flow Metadata
ADD ./NAE/nvidia.cfg /etc/NAE/nvidia.cfg
ADD ./NAE/AppDef.json /etc/NAE/AppDef.json
ADD ./NAE/screenshot.png /etc/NAE/screenshot.png
ADD ./Wallpaper-yaybench_1280x720.png /opt/images/Wallpaper.png
ADD ./yaymark_57x57.png /opt/icons/yaybench.png
ADD ./xfce4-desktop.xml /etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-desktop.xml
ADD ./xfce4-panel.xml /etc/skel/.config/xfce4/xfconf/xfce-perchannel-xml/xfce4-panel.xml

CMD /usr/local/scripts/start.sh
CMD /usr/local/scripts/update_drivers.sh
