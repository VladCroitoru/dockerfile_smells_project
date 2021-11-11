FROM centos:7

RUN \
  yum install -y epel-release

RUN \
  yum install -y git python34 python34-devel libpng-devel libjpeg-devel gcc gcc-c++ make libffi-devel openssl-devel

RUN \
  yum -y install fontconfig libfontenc fontconfig-devel \
  libXfont ghostscript-fonts xorg-x11-font-utils urw-fonts

RUN \
  curl -O https://bootstrap.pypa.io/get-pip.py && \
  python3 get-pip.py && \
  pip install requests[security] Pillow gunicorn flask gevent

RUN \
  yum -y install wget bzip2 && \
  curl -O -L -k https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 && \
  bunzip2 phantomjs-2.1.1-linux-x86_64.tar.bz2 && tar xf phantomjs-2.1.1-linux-x86_64.tar && \
  mv phantomjs-2.1.1-linux-x86_64 /opt/phantomjs

ENV PHANTOMJS_BINARY /opt/phantomjs/bin/phantomjs

# Building from source is also an option.
#RUN \
#  yum -y install git && \
#  git clone https://github.com/ariya/phantomjs.git && \
#  cd phantomjs && git checkout 2.1 && ./build.sh --confirm --jobs 1 

COPY . /webrender

WORKDIR webrender

EXPOSE 8010

CMD gunicorn -c gunicorn.ini wrengine:app

# Note on Ubuntu 14.04 font packages include:
# xfonts-base ttf-mscorefonts-installer fonts-arphic-bkai00mp fonts-arphic-bsmi00lp fonts-arphic-gbsn00lp fonts-arphic-gkai00mp fonts-arphic-ukai fonts-farsiweb fonts-nafees fonts-sil-abyssinica fonts-sil-ezra fonts-sil-padauk fonts-unfonts-extra fonts-unfonts-core ttf-indic-fonts fonts-thai-tlwg fonts-lklug-sinhala
