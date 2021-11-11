FROM r-base:3.5.1
MAINTAINER Josef Eisl <zapster@zapster.cc>

RUN apt-get update -q && apt-get install -qy \
  curl \
  gnupg \
  imagemagick \
  libcurl4-openssl-dev \
  libmagick++-dev \
  libpoppler-cpp-dev \
  librsvg2-bin \
  libssl-dev=1.1.1-1 \
  libxml2-dev \
  make \
  poppler-utils \
  python-pygments \
  unzip \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# install fira font
# from https://github.com/matze/mtheme
ADD ./getFiraFont.sh ./getFiraFont.sh
RUN ./getFiraFont.sh

USER docker
# preinit bash history
ADD ./.bash_history /home/docker/.bash_history

# setup R local lib
ENV R_LIBS="/home/docker/R_libs"
RUN mkdir -p $R_LIBS

# install texlive
COPY ./medium.profile /tmp/
RUN mkdir -p /tmp/texlive \
  | curl -SL http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz \
  | tar -xzC /tmp/texlive \
  && /tmp/texlive/install-tl-*/install-tl -profile /tmp/medium.profile \
  && rm -rf /tmp/texlive
ENV PATH=/home/docker/usr/local/texlive/current/bin/x86_64-linux:$PATH \
    INFOPATH=/home/docker/usr/local/texlive/current/texmf-dist/doc/info:$INFOPATH \
    MANPATH=/home/docker/usr/local/texlive/current/texmf-dist/doc/man:$MANPATH

# install R packages
COPY ./R.packages /tmp/
RUN Rscript -e 'p <- readLines("/tmp/R.packages"); install.packages(p, repos="http://cran.rstudio.com/", clean=TRUE); for(x in p) { if (!require(x,character.only = TRUE)) {quit(1)}};devtools::install_github("jeremystan/tidyjson")'

# install texlive packages
COPY ./texlive.packages /tmp/
RUN tlmgr update --all \
  && /bin/bash -c 'tlmgr install $(cat /tmp/texlive.packages | tr "\n" " ")' \
  && tlmgr option repository http://mirror.ctan.org/systems/texlive/tlnet

# update lualatex font db
RUN luaotfload-tool --update

CMD ["bash"]
