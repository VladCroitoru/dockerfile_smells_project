#
# min && simple
# 
# docker build -t dante  ./ 
# docker run --name dante -d -p 1080:1080 dante
# docker run --name dante -d -p 1080:1080 -e DANTE_User="proxy" -e DANTE_Pass="proxy" dante

FROM centos

MAINTAINER lianshufeng <251708399@qq.com>


ENV DANTE_VER 1.4.2
ENV DANTE_URL https://www.inet.no/dante/files/dante-$DANTE_VER.tar.gz
ENV DANTE_FILE dante.tar.gz
ENV DANTE_TEMP dante
ENV DANTE_User ""
ENV DANTE_Pass ""

#download and install
RUN set -xe \
    && rpm --rebuilddb \
	&& yum install gcc  pcre-devel zlib-devel libtool c++ make -y \
    && mkdir $DANTE_TEMP \
	&& cd $DANTE_TEMP \
	&& curl -sSL $DANTE_URL -o $DANTE_FILE \
	&& tar xzf $DANTE_FILE --strip 1 \
	&& ./configure \
	&& make install \
	&& cd .. \
	&& rm -rf $DANTE_TEMP 

	
#增加配置文件	
ADD sockd_none.conf /etc/sockd_none.conf
ADD sockd_user.conf /etc/sockd_user.conf
ADD sockd.sh /opt/sockd.sh
RUN chmod -R 777 /opt/sockd.sh




ENV CFGFILE_NONE /etc/sockd_none.conf
ENV CFGFILE_USER /etc/sockd_user.conf
ENV PIDFILE /tmp/sockd.pid

EXPOSE 1080

#ENTRYPOINT sockd -f $CFGFILE_NONE -p $PIDFILE 
#ENTRYPOINT sockd -f $CFGFILE_USER -p $PIDFILE 


ENTRYPOINT  /opt/sockd.sh 