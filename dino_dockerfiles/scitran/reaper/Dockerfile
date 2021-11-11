FROM buildpack-deps:xenial

RUN apt-get update && apt-get install -y \
    python-pip \
 && rm -rf /var/lib/apt/lists/* \
 && pip install --upgrade pip setuptools wheel

COPY movescu.cc.patch /tmp
RUN cd /tmp \
 && curl http://support.dcmtk.org/redmine/attachments/download/87/dcmtk-3.6.1_20150924.tar.gz | tar xz \
 && cd dcmtk-* \
 && patch --strip 1 </tmp/movescu.cc.patch \
 && ./configure \
 && make config-all ofstd-all oflog-all dcmdata-all dcmimgle-all dcmimage-all dcmjpeg-all dcmjpls-all dcmtls-all dcmnet-all \
 && make dcmnet-install dcmdata-install \
 && rm -rf /tmp/movescu.cc.patch /tmp/dcmtk-*

COPY . /src/reaper

ENV LC_ALL="C.UTF-8"
RUN pip install -e /src/reaper
