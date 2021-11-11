FROM centos

MAINTAINER gecko655 <aqwsedrft1234@yahoo.co.jp>

WORKDIR /root

RUN echo "set -o vi" >> /etc/bashrc
RUN cp -p /usr/share/zoneinfo/Japan /etc/localtime
# RUN yum update -y
RUN yum install git gcc openssl-devel make crontabs wget -y

RUN git clone git://git.ffmpeg.org/rtmpdump
RUN (cd rtmpdump && make SYS=posix && make install)
# http://qiita.com/yayugu/items/12c0ffd92bc8539098b8
RUN echo "/usr/local/lib" > /etc/ld.so.conf.d/rtmpdump.conf 
RUN ldconfig
# http://blogs.yahoo.co.jp/mrsd_tangerine/40359620.html

RUN wget http://www.swftools.org/swftools-0.9.2.tar.gz
RUN tar xvzf swftools-0.9.2.tar.gz
COPY src/swftools swftools
RUN cp swftools/Makefile.in swftools-0.9.2/swfs/Makefile.in
RUN (cd swftools-0.9.2 && ./configure --prefix=/usr --libdir=/usr/lib64 && make && make install)
RUN rm -f swftools-0.9.2.tar.gz
RUN rm -rf swftools-0.9.2

RUN mkdir -p /opt/agqr
RUN touch /tmp/cron.log
COPY crontab.config .
RUN (crontab -l; cat crontab.config ) | crontab

COPY src/rec.sh rec.sh
COPY src/radiko.sh radiko.sh
COPY src/init.sh init.sh

CMD /sbin/init
