FROM ubuntu:xenial
LABEL maintainer="Chris Simpson"
RUN apt-get update && apt-get install -y \
gcc \
build-essential \
make \
flex \
bison \
libwrap0-dev \
libpam-dev \
python-mysql.connector \
vim \
net-tools \
ssh \
wget \
sudo \
inetutils-ping \
rsyslog \
libproc-daemon-perl
ADD tacacs-F4.0.4.28.tar.gz /tmp/
ADD tac_plus.conf /etc/
ADD do_auth.ini /root/
ADD do_auth.py /root/
ADD tac_plus /etc/init.d/
ADD rsyslog_tacplus.conf /etc/rsyslog.d/
COPY start-services.sh /start-services.sh
RUN cd /tmp/tacacs-F4.0.4.28; ./configure; make install; echo "include /etc/ld.so.conf.d/*.conf /usr/local/lib" > /etc/ld.so.conf; ldconfig
LABEL release_notes="LAB TACACS"
EXPOSE 49/tcp 
EXPOSE 22/tcp
RUN /start-services.sh
ENTRYPOINT ["/usr/local/sbin/tac_plus", "-C", "/etc/tac_plus.conf", "-G", "-d", "2"]
