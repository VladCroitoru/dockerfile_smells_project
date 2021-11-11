FROM million12/nginx:latest

ENV \
  # - APP_REPO, APP_BRANCH: the APP GitHub repository and related branch
  # for related branch or tag use e.g. master
  APP_REPO="https://github.com/janeczku/calibre-web" \
  APP_BRANCH="master" \
  # - AMAZON_KG_*: KindleGen is a command line tool which enables publishers to work
  # in an automated environment with a variety of source content including HTML, XHTML or EPUB
  AMAZON_KG_TAR="kindlegen_linux_2.6_i386_v2_9.tar.gz" \
  AMAZON_KG_URL="http://kindlegen.s3.amazonaws.com/kindlegen_linux_2.6_i386_v2_9.tar.gz"

RUN \
  # Install ImageMagick & libxml
  rpm --rebuilddb && yum update -y && \
  yum install -y ImageMagick-devel libevent libxml2 libxml2-devel libxml2-python libxslt libxslt-devel python-devel gcc && \
  # Install Gunicorn, Wand
  easy_install -O2 pip && \
  pip install --no-cache-dir Wand gunicorn lxml gevent google-api-python-client pydrive && \
  yum remove -y gcc libxslt-devel python-devel libxml2-devel && \
  yum autoremove -y && \
  yum clean all && rm -rf /tmp/yum*

ADD container-files /
ADD ${AMAZON_KG_URL} /tmp/${AMAZON_KG_TAR}
ADD ${APP_REPO}/archive/${APP_BRANCH}.tar.gz /tmp/calibre-cps.tar.gz

RUN \
  # Fix locale
  localedef -c -i en_US -f UTF-8 en_US.UTF-8 && \
  # Install calibre-web
  mkdir -p /opt/app && \
  tar zxf /tmp/calibre-cps.tar.gz -C /opt/app --strip-components=1 && \
  tar zxf /tmp/kindlegen_linux_2.6_i386_v2_9.tar.gz -C /opt/app/vendor && \
  pip install --no-cache-dir -r /opt/app/requirements.txt && \
  rm /tmp/calibre-cps.tar.gz && \
  rm /tmp/${AMAZON_KG_TAR} && \
  ln -s /data/app.db /opt/app/app.db && \
  ln -s /data/gdrive.db /opt/app/gdrive.db && \
  chown -R www:www /opt/app

ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8 LANGUAGE=en_US:en
