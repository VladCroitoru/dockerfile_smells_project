FROM ubuntu:disco
MAINTAINER Hagen Fritsch <rumpeltux-songbookdocker@irgendwo.org>
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update -q && \
    apt-get install -qy texlive-full wget make && \
    apt-get remove -qy texlive*doc

# Install MuseJazz font
RUN mkdir -p /usr/share/fonts/truetype/music && \
    wget 'https://github.com/musescore/MuseScore/blob/3c87ca4dc4a72662c876ee84568c52d064c74753/fonts/MuseJazz.ttf?raw=true' \
         -O /usr/share/fonts/truetype/music/MuseJazz.ttf && \
    fc-cache -f -v

# Install more packages that are needed now that the songbook evolved.
RUN apt-get update -q && apt-get install -qy --no-install-recommends \
    git python-pyparsing lilypond

# leadsheets bugfix (https://github.com/cgnieder/leadsheets/pull/18)
RUN sed -i 's/prop_gput:cnn/prop_gput:cnV/' /usr/share/texlive/texmf-dist/tex/latex/leadsheets/leadsheets.library.properties.code.tex

# Update lilypond to experimental version from debian (not yet available in Ubuntu)
RUN cd /tmp; \
    wget http://ftp.de.debian.org/debian/pool/main/l/lilypond/lilypond_2.19.83-1~exp1_amd64.deb \
         http://ftp.de.debian.org/debian/pool/main/l/lilypond/lilypond-data_2.19.83-1~exp1_all.deb && \
    dpkg -i *.deb && \
    rm *.deb

# Install pdfsizeopt
RUN mkdir -p /usr/local/pdfsizeopt; \
    cd /usr/local/pdfsizeopt; \
    wget -q -O - https://github.com/pts/pdfsizeopt/releases/download/2017-01-24/pdfsizeopt_libexec_linux-v3.tar.gz | tar xzo; \
    wget -q -O pdfsizeopt https://raw.githubusercontent.com/pts/pdfsizeopt/master/pdfsizeopt.single; \
    chmod -R 755 .

WORKDIR /data
VOLUME ["/data"]
