FROM sumdoc/texlive-2017

LABEL maintainer "Schuyler Eldridge <schuyler.eldridge@gmail.com>"

# we additionally need latexmk, python, java (because of pax), perl (because of pax), pdftk, ghostscript, and unzip (because of pax)
RUN apt-get update -qq && apt-get upgrade -qq && \
    apt-get install -y --no-install-recommends latexmk python2.7 openjdk-8-jre-headless libfile-which-perl pdftk ghostscript unzip && \
    apt-get install -y python-pip && \
    apt-get install -y ruby poppler-utils && \
    apt-get install -y graphviz && \
    apt-get install -y inkscape && \
    apt-get install -y autoconf && \
    apt-get install -y poppler-utils && \
    apt-get install -y procps && \
    apt-get install -y python3.6 && \
    apt-get install -y python3-matplotlib && \
    apt-get install -y python3-numpy && \
    apt-get install -y python3-scipy && \
    apt-get install -y fonts-inconsolata && \
    apt-get install -y fontconfig && \
    rm -rf /var/lib/apt/lists/*

# install IBM Plex fonts
RUN mkdir -p /tmp/fonts && \
    cd /tmp/fonts && \
    wget https://github.com/IBM/plex/releases/download/v1.0.2/OpenType.zip && \
    unzip OpenType.zip -x */LICENSE.txt */license.txt */CHANGELOG */.DS_Store && \
    cp -r OpenType/* /usr/local/share/fonts && \
    fc-cache -f -v

# install Ruby's bundler
RUN gem install bundler

# update texlive
RUN tlmgr update --self --all --reinstall-forcibly-removed

# Prepare usage of pax
RUN mkdir /root/.texlive2017 && perl `kpsewhich -var-value TEXMFDIST`/scripts/pax/pdfannotextractor.pl --install

# Enable using the scripts of https://github.com/gi-ev/LNI-proceedings
# Install pygments to enable minted
RUN pip install pyparsing && pip install python-docx && pip install pygments

WORKDIR /home
