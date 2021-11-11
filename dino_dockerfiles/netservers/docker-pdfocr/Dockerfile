FROM ubuntu:trusty

MAINTAINER John McEleney

RUN \
  apt-get update && apt-get -y install \
    build-essential \
    gcj-jdk \
    unzip \
    wget \
    tesseract-ocr \
    ruby \
    poppler-utils \
    exactimage \
    ghostscript \
    incron \
  && cd /usr/src \
  && wget http://www.pdflabs.com/tools/pdftk-the-pdf-toolkit/pdftk-2.02-src.zip \
  && unzip pdftk-2.02-src.zip \
  && sed -i 's/VERSUFF=-4.6/VERSUFF=-4.8/g' pdftk-2.02-dist/pdftk/Makefile.Debian \
  && cd pdftk-2.02-dist/pdftk \
  && make -f Makefile.Debian \
  && make -f Makefile.Debian install \
  && cd /usr/src \
  && rm -rf pdftk-2.02-dist pdftk-2.02-src.zip \
  && apt-get remove -y build-essential \
  && apt-get clean

COPY pdfocr.rb /usr/local/bin/pdfocr

RUN mkdir /inbox /outbox

VOLUME ["/inbox","/outbox"]

RUN echo 'pdfocr' >> /etc/incron.allow

ADD incron.pdfocr /var/spool/incron/pdfocr
ADD do_ocr /usr/local/bin/
ADD entrypoint.sh /entrypoint.sh

CMD ["/entrypoint.sh"]
