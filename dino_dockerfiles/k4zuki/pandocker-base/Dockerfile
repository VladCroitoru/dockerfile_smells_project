FROM ubuntu:16.04

MAINTAINER k4zuki

ENV PLANTUML_VERSION 1.2018.12
ENV PLANTUML_DOWNLOAD_URL https://sourceforge.net/projects/plantuml/files/plantuml.$PLANTUML_VERSION.jar/download

ENV PANDOC_REPO https://github.com/jgm/pandoc
ENV PANDOC_VERSION 2.7.3
ENV PANDOC_DEB pandoc-$PANDOC_VERSION-1-amd64.deb
ENV PANDOC_DOWNLOAD_URL $PANDOC_REPO/releases/download/$PANDOC_VERSION/$PANDOC_DEB
ENV PANDOC_ROOT /usr/local/pandoc

ENV CROSSREF_REPO https://github.com/lierdakil/pandoc-crossref
ENV CROSSREF_VERSION v0.3.4.1
ENV CROSSREF_ARCHIVE linux-pandoc_2_7_2.tar.gz
ENV CROSSREF_DOWNLOAD_URL $CROSSREF_REPO/releases/download/$CROSSREF_VERSION/$CROSSREF_ARCHIVE

ENV LANG C.UTF-8

RUN echo "deb http://ftp.jaist.ac.jp/pub/Linux/ubuntu/ xenial main restricted universe multiverse" > /etc/apt/sources.list && \
    echo "deb http://ftp.jaist.ac.jp/pub/Linux/ubuntu/ xenial-updates main restricted universe multiverse" >> /etc/apt/sources.list && \
    echo "deb http://ftp.jaist.ac.jp/pub/Linux/ubuntu/ xenial-security main restricted universe multiverse" >> /etc/apt/sources.list && \
    apt-get -y update && \
    apt-get -y install wget curl unzip nano make && \
    apt-get -y --no-install-recommends install gpp \
      librsvg2-bin \
      git && \
    apt-get -y --no-install-recommends install graphviz default-jre-headless && \
    curl -fsSL "$PLANTUML_DOWNLOAD_URL" -o /usr/local/bin/plantuml.jar && \
    echo "#!/bin/bash" > /usr/local/bin/plantuml && \
    echo "java -jar /usr/local/bin/plantuml.jar -Djava.awt.headless=true \$@" >> /usr/local/bin/plantuml && \
    chmod +x /usr/local/bin/plantuml && \

    apt-get -y --no-install-recommends install python3-pip python3-setuptools \
      python3-yaml \
      python3-six \
      python3-cairosvg && \
    pip3 install -U setuptools pantable csv2table \
      setuptools_scm \
      pandoc-imagine \
      svgutils \
      wavedrom==1.8.0\
      git+https://github.com/daamien/pandoc-latex-barcode && \

    wget -c $PANDOC_DOWNLOAD_URL && \
      dpkg -i $PANDOC_DEB && \
      wget -c $CROSSREF_DOWNLOAD_URL && \
      tar zxf $CROSSREF_ARCHIVE && \
      mv pandoc-crossref /usr/local/bin/ && \

    apt-get -y install --no-install-recommends texlive-xetex xzdec lmodern fonts-ricty-diminished \
      texlive-fonts-recommended fonts-liberation texlive-generic-recommended texlive-lang-japanese texlive-math-extra && \
    mkdir -p /usr/share/texlive/texmf-dist/tex/latex/BXptool/ && \
      wget -c https://github.com/zr-tex8r/BXptool/archive/v0.4.zip && \
      unzip -e v0.4.zip && \
      cp BXptool-0.4/bx*.sty BXptool-0.4/bx*.def /usr/share/texlive/texmf-dist/tex/latex/BXptool/ && \
    # wget -c https://github.com/adobe-fonts/source-code-pro/archive/2.030R-ro/1.050R-it.zip && \
    #   unzip -e 1.050R-it.zip && cp source-code-pro-2.030R-ro-1.050R-it/TTF/SourceCodePro-*.ttf /usr/local/share/fonts/ && \
    # wget -c https://github.com/adobe-fonts/source-sans-pro/archive/2.020R-ro/1.075R-it.zip && \
    #   unzip -e 1.075R-it.zip && cp source-sans-pro-2.020R-ro-1.075R-it/TTF/SourceSansPro-*.ttf /usr/local/share/fonts/ && \
    wget -c https://github.com/adobe-fonts/source-han-sans/raw/release/OTF/SourceHanSansJ.zip && \
      unzip -e SourceHanSansJ.zip && cp SourceHanSansJ/SourceHanSans-*.otf /usr/local/share/fonts/ && \
    mktexlsr && \

    mkdir -p /workdir && \
    cd /workdir && \

      rm /$PANDOC_DEB && \
      rm /$CROSSREF_ARCHIVE && \
      rm -r ~/.cache/pip && \
      apt-get -y clean && \
    fc-cache -fv

WORKDIR /workdir

VOLUME ["/workdir"]

CMD ["bash"]
