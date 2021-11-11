FROM docker.io/centos
MAINTAINER Anthony Jones <anthony@anthonyandtobie.com>
RUN yum -y install wget tar samba samba-client
RUN yum -y update
RUN if [ ! -d /hdhomerun ];then mkdir /hdhomerun; fi
RUN if [ ! -d /hdhomerun/video ];then mkdir /hdhomerun/video; fi
RUN if [ ! -d /hdhomerun/etc ];then mkdir /hdhomerun/etc; fi
RUN if [ ! -d /hdhomerun/bin ];then mkdir /hdhomerun/bin; fi
ADD hdhomerun.conf /hdhomerun/etc/
WORKDIR /hdhomerun/bin
ADD hdhomerun_start.sh /hdhomerun/bin/
RUN curl -O -L http://download.silicondust.com/hdhomerun/hdhomerun_record_linux
#RUN useradd -ms /bin/bash hdhomerun
#RUN chown -R hdhomerun:hdhomerun /hdhomerun
RUN chmod 755 /hdhomerun/bin
RUN chmod 755 /hdhomerun/etc
RUN chmod 755 /hdhomerun/video
RUN chmod 755 /hdhomerun/bin/*
RUN chmod 744 /hdhomerun/etc/*
ADD smb.conf /etc/samba/
RUN smbpasswd -an nobody
EXPOSE 137 138 139 445 65001

RUN /usr/sbin/smbd && sleep 10 && smbcontrol smbd shutdown

#USER hdhomerun

CMD ["/hdhomerun/bin/hdhomerun_start.sh"]

