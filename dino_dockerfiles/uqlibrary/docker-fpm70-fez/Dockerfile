FROM uqlibrary/docker-fpm70:18

RUN rpm --import http://li.nux.ro/download/nux/RPM-GPG-KEY-nux.ro && \
  yum install -y http://li.nux.ro/download/nux/dextop/el7/x86_64/nux-dextop-release-0-5.el7.nux.noarch.rpm && \
  yum install -y file && \
  yum install -y mysql && \
  yum install -y poppler-utils && \
  yum install -y perl-Image-ExifTool --enablerepo=epel-testing && \
  yum install -y ffmpeg --enablerepo=nux-dextop && \
  yum install -y ImageMagick7 ImageMagick7 --enablerepo=remi --skip-broken && \
  wget -O /usr/local/src/jhove.tar.gz http://downloads.sourceforge.net/project/jhove/jhove/JHOVE%201.11/jhove-1_11.tar.gz && \
  wget -O /usr/local/src/yamdi.tar.gz http://downloads.sourceforge.net/project/yamdi/yamdi/1.9/yamdi-1.9.tar.gz && \
  wget -O /usr/local/src/graphviz.tar.gz http://www.graphviz.org/pub/graphviz/stable/SOURCES/graphviz-2.38.0.tar.gz && \
  cd /usr/local/src && tar xvzf yamdi.tar.gz && \
  cd /usr/local/src && tar xvzf jhove.tar.gz && \
  cd /usr/local/src && tar xvzf graphviz.tar.gz && \
  yum group install -y "Development Tools" && \
  cd /usr/local/src/yamdi-1.9 && gcc yamdi.c -o yamdi -O2 -Wall && mv yamdi /usr/bin/yamdi && chmod +x /usr/bin/yamdi && cd .. && rm -rf yamdi-1.9 && rm -f yamdi.tar.gz && \
  yum install -y cairo-devel expat-devel freetype-devel gd-devel fontconfig-devel glib libpng zlib pango-devel pango && \
  cd /usr/local/src/graphviz-2.38.0 && ./configure && make && make install && \
  yum install -y java-1.8.0-openjdk-headless && \
  mv /usr/local/src/jhove /usr/local/jhove && rm -f /usr/local/src/jhove.tar.gz && \
  yum group remove -y "Development Tools" && \
  yum autoremove -y && yum clean all

COPY jhove /usr/local/jhove/
RUN chmod +x /usr/local/jhove/jhove && sed -i 's/\#JHOVE_HOME=\[fill in path to jhove directory\]/JHOVE_HOME=\/usr\/local\/jhove\//' /usr/local/jhove/jhove

COPY etc/php-fpm.d/www.conf /etc/opt/remi/php70/php-fpm.d/www.conf

RUN mkdir -p /espace/data && \
  mkdir -p /espace_san/incoming && \
  sed -i "s/memory_limit = 128M/memory_limit = 800M/" /etc/php.ini && \
  sed -i "s/post_max_size = 8M/post_max_size = 800M/" /etc/php.ini && \
  sed -i "s/upload_max_filesize = 30M/upload_max_filesize = 800M/" /etc/php.ini && \
  sed -i "s/session.gc_maxlifetime = 1440/session.gc_maxlifetime = 10800/" /etc/php.ini && \
  sed -i "s/; max_input_vars = 1000/max_input_vars = 5000/" /etc/php.ini
