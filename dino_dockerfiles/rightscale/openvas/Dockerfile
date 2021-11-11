# OpenVAS 8


FROM rightscale/crs-apps:master

MAINTAINER Bart Falzarano bart.falzarano@rightscale.com

ADD bin/* /openvas/
ADD config/redis.config /etc/redis/redis.tmp

# First Install build deps
# 
# NOTES:
# openssh-client includes ssh-keygen which is for LSC credential generation for GNU/Linux targets         
# rpm is for LSC credential package generation for RPM based targets
# alien is for LSC credential package generation for DEB based targets
# nsis is for LSC credential package generation for Microsoft Windows targets
#
#
RUN apt-get update > /dev/null && \
    apt-get install -y > /dev/null \
      alien \
      autoconf \
      bison \
      build-essential \
      cmake \
      devscripts \
      doxygen \
      dpatch \ 
      heimdal-dev \ 
      heimdal-multidev \
      libassuan-dev \ 
      libglib2.0-dev \ 
      libgmp-dev \
      libgmp3-dev \
      libgnutls-dev \
      libgpgme11-dev \
      libhiredis-dev \ 
      libksba-dev \
      libldap2-dev \
      libmicrohttpd-dev \
      libopenvas2 \
      libpcap-dev \
      libpcre3-dev \
      libpopt-dev \
      libpth-dev \
      libsnmp-dev \
      libsqlite3-dev \
      libssh-dev \
      libssh2-1-dev \
      libwrap0-dev \
      libxml2-dev \
      libxslt1-dev \
      mingw32 \
      nmap \
      nsis \
      openssh-client \
      pkg-config \
      quilt \
      redis-server \
      rpm \
      rsync \
      sqlfairy \
      sqlite3 \
      texlive-latex-base \
      texlive-latex-extra \
      texlive-latex-recommended \
      uuid-dev \
      wamerican \
      wget \
      xmltoman \
      xsltproc && \
chmod a+x /openvas/setup.sh && \
chmod a+x /openvas/redis-fix.sh && \
chmod a+x /openvas/parsexml.sh && \
chmod a+x /openvas/startup.sh
RUN /openvas/redis-fix.sh
RUN cd /usr/local/src && \
wget --no-check-certificate https://wald.intevation.org/frs/download.php/2351/openvas-libraries-8.0.8.tar.gz && \
    wget --no-check-certificate https://wald.intevation.org/frs/download.php/2367/openvas-scanner-5.0.7.tar.gz && \
    wget --no-check-certificate https://wald.intevation.org/frs/download.php/2359/openvas-manager-6.0.9.tar.gz && \
    wget --no-check-certificate https://wald.intevation.org/frs/download.php/2363/greenbone-security-assistant-6.0.11.tar.gz && \
    wget --no-check-certificate https://wald.intevation.org/frs/download.php/2332/openvas-cli-1.4.4.tar.gz && \
    wget --no-check-certificate https://wald.intevation.org/frs/download.php/1975/openvas-smb-1.0.1.tar.gz && \
    tar zxvfp openvas-libraries-8.0.8.tar.gz > /dev/null && \
    tar zxvfp openvas-scanner-5.0.7.tar.gz > /dev/null && \
    tar zxvfp openvas-manager-6.0.9.tar.gz > /dev/null && \
    tar zxvfp greenbone-security-assistant-6.0.11.tar.gz > /dev/null && \
    tar zxvfp openvas-cli-1.4.4.tar.gz > /dev/null && \
    tar zxvfp openvas-smb-1.0.1.tar.gz > /dev/null && \
    cd openvas-smb* && \
    mkdir build && \
    cd build && \
    cmake .. > /dev/null && \
    make -j $(nproc) > /dev/null && \
    make install > /dev/null && \
      make rebuild_cache > /dev/null && \
    cd /usr/local/src && \
    cd openvas-libraries-* && \
    mkdir build && \
    cd build && \
    cmake .. > /dev/null && \
    make -j $(nproc) > /dev/null && \
    make install > /dev/null && \
      make rebuild_cache > /dev/null && \
    cd /usr/local/src && \
    cd openvas-scanner-* && \
    mkdir build && \
    cd build && \
    cmake .. > /dev/null && \
    make -j $(nproc) > /dev/null  && \
    make install > /dev/null && \
      make rebuild_cache > /dev/null && \
    cd /usr/local/src && \
    cd openvas-manager-* && \
    mkdir build && \
    cd build && \
    cmake .. > /dev/null && \
    make -j $(nproc) > /dev/null && \
    make install > /dev/null  && \
      make rebuild_cache > /dev/null && \
    cd /usr/local/src && \
    cd greenbone-security-assistant-* && \
    mkdir build && \
    cd build && \
    cmake .. > /dev/null && \
    make -j $(nproc) > /dev/null && \
    make install > /dev/null  && \
      make rebuild_cache > /dev/null && \
    cd /usr/local/src && \
    cd openvas-cli-* && \
    mkdir build && \
    cd build && \
    cmake .. > /dev/null && \
    make -j $(nproc) > /dev/null && \
    make install > /dev/null && \
      make rebuild_cache > /dev/null && \
  /openvas/setup.sh 


ENTRYPOINT ["/openvas/startup.sh"]

# Expose UI
EXPOSE 443 9390 9391


