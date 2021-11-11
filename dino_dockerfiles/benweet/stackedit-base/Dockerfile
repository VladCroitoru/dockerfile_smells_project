FROM node:8

# Update existing packages and install required ones
RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get update -y \
  && apt-get install -y --no-install-recommends \
  	curl \
    unzip \
    fontconfig \
    xorg \
    libssl-dev \
    libxrender-dev \
    wget gdebi \
  && rm -rf /var/lib/apt/lists/*

# Install texlive
RUN curl -SLO "http://mirror.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz" \
  && tar -xzf "install-tl-unx.tar.gz" \
  && cd install-tl-* \
  && (printf "O\nD\nS\nR\nI\n" | ./install-tl) \
  && cd .. \
  && rm -rf install-tl* /usr/local/texlive/2017/texmf-dist/doc
ENV PATH /usr/local/texlive/2017/bin/x86_64-linux:$PATH

# install fonts
RUN mkdir -p ~/.fonts \
  && cd ~/.fonts \
  && curl -SLO https://noto-website-2.storage.googleapis.com/pkgs/NotoSansCJKsc-hinted.zip \
  && unzip *.zip \
  && rm *.zip \
  && cd - \
  && fc-cache -fv

# Install wkhtmltopdf
RUN cd / \
  && curl -SLO https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
  && tar xJf wkhtmltox-0.12.4_linux-generic-amd64.tar.xz \
  && rm *.tar.xz
ENV WKHTMLTOPDF_PATH /wkhtmltox/bin/wkhtmltopdf

# Install pandoc
ENV PANDOC_VERSION 1.17.0.2
RUN curl -SLO "https://github.com/jgm/pandoc/releases/download/$PANDOC_VERSION/pandoc-$PANDOC_VERSION-1-amd64.deb" \
  && dpkg -i pandoc-$PANDOC_VERSION-1-amd64.deb \
  && rm pandoc-$PANDOC_VERSION-1-amd64.deb

ENV NPM_CONFIG_LOGLEVEL warn
RUN npm install -g yarn


