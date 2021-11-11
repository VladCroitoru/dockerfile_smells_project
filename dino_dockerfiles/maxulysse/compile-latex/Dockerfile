FROM debian:stretch-slim

LABEL \
  author="Maxime Garcia" \
  description="Image for compile-latex" \
  maintainer="max.u.garcia@gmail.com"

# Set up ENV
ENV LANG=C.UTF-8

# Install pre-requistes
ARG DEBIAN_FRONTEND=noninteractive
RUN \
  apt-get update && apt-get install -y --no-install-recommends \
    ca-certificates \
    fontconfig \
    git \
    lmodern \
    procps \
    python-pygments \
    wget \
  && rm -rf /var/lib/apt/lists/*

# Setup ENV variables
ENV \
  TL_BIN="install-tl-unx.tar.gz" \
  PATH="$PATH:/usr/local/texlive/2018/bin/x86_64-linux"

COPY texlive.profile /opt/

# Install TeX Live
RUN \
  wget -q http://mirror.ctan.org/systems/texlive/tlnet/$TL_BIN \
  -O /opt/$TL_BIN \
  && tar xzf /opt/$TL_BIN -C /opt/ \
  && mv /opt/install-tl-2* /opt/install-tl/ \
  && mv /opt/texlive.profile /opt/install-tl/ \
  && cd /opt/install-tl \
  && ./install-tl --profile=texlive.profile \
  && rm -rf /opt/$TL_BIN /opt/$TL_DIR

# Install Fonts, mtheme, modernCV
RUN \
  mkdir -p \
    /usr/share/fonts/truetype/academicons \
  && tlmgr update --self \
  && tlmgr init-usertree \
  && tlmgr install academicons \
  && tlmgr install beamertheme-metropolis \
  && tlmgr install biber \
  && tlmgr install biblatex \
  && tlmgr install ccicons \
  && tlmgr install collection-fontsrecommended \
  && tlmgr install collection-xetex \
  && tlmgr install contour \
  && tlmgr install csquotes \
  && tlmgr install fontawesome5 \
  && tlmgr install framed \
  && tlmgr install fvextra \
  && tlmgr install ifplatform \
  && tlmgr install import \
  && tlmgr install logreq \
  && tlmgr install minted \
  && tlmgr install moderncv \
  && tlmgr install pgfopts \
  && tlmgr install ulem \
  && tlmgr install upquote \
  && tlmgr install xstring \
  && git clone https://github.com/jpswalsh/academicons.git \
    academicons \
	&& find academicons/ -name "*.ttf" -exec install -m644 {} /usr/share/fonts/truetype/academicons/ \; || return 1 \
  && rm -rf \
    academicons* \
  && texhash \
  && fc-cache -fsv
