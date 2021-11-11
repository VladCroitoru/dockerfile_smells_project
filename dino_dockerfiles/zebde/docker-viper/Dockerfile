FROM python:3
LABEL version="0.3"

RUN sed -i "s/jessie main/jessie main contrib non-free/" /etc/apt/sources.list

RUN apt-get update -qq && \
  apt-get -y --no-install-recommends install flex bison libjansson-dev libmagic-dev unrar exiftool gcc python-socksipy libssl-dev swig p7zip-full ssdeep libfuzzy-dev tor clamav-daemon -qq && \
  apt-get clean && \
  rm -rf /var/lib/apt/lists/* /var/tmp/*

WORKDIR /tmp

RUN git clone --recursive --branch v3.7.1 https://github.com/VirusTotal/yara.git && \
  cd /tmp/yara && \
  ./bootstrap.sh && \
  sync && \
  ./configure --with-crypto --enable-magic --enable-cuckoo --enable-dotnet && \
  make && \
  make install && \
  echo "/usr/local/lib" >> /etc/ld.so.conf && \
  ldconfig && \
  cd /tmp/ && \
  git clone --recursive --branch v3.7.0 https://github.com/VirusTotal/yara-python && \
  cd yara-python && \
  python setup.py build --dynamic-linking && \
  python setup.py install && \
  rm -rf /tmp/*

WORKDIR /usr/local

RUN git clone https://github.com/viper-framework/viper.git && \
  mv viper/viper.conf.sample viper/viper.conf && \
  sed -i 's/storage_path =/storage_path =\/etc\/viper\/workdir/' viper/viper.conf && \
  mkdir -p /etc/viper/workdir

WORKDIR /usr/local/viper

RUN git checkout master && \
  pip install -r requirements.txt && \
  git submodule init && \
  git submodule update && \
  rm -rf /tmp/*

EXPOSE 8080
HEALTHCHECK --interval=5s --timeout=3s --retries=3 CMD curl -f / http://localhost:8080 || exit 1

CMD ./viper-web -H $HOSTNAME
