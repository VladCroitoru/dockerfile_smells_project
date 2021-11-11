FROM debian:stable-slim

RUN apt-get update && apt-get install -y \
  jq \
  libfontconfig \
  libssl1.0-dev \
  libxrender1 \
  libxtst6 \
  openssh-client \
  rsync \
  wget \
  xz-utils \
  && rm -rf /var/lib/apt/lists/*

RUN wget https://api.github.com/repos/jgm/pandoc/releases/latest -O - | jq -r '.assets[] | select(.name | index("amd64.deb")) | .browser_download_url' | wget -i - --quiet -O pandoc.deb \
    && dpkg -i pandoc.deb\
    && rm pandoc.deb
RUN wget https://api.github.com/repos/wkhtmltopdf/wkhtmltopdf/releases/latest -O - | jq -r '.assets[] | select(.name | index("amd64.tar.xz")) | .browser_download_url' | wget -i - --quiet -O wkhtmltox.tar.xz \
    && tar xf wkhtmltox.tar.xz\
    && rm wkhtmltox.tar.xz \
    && rsync --remove-source-files -a /wkhtmltox/ /usr/ \
    && rm -rf wkhtmltox


