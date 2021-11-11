FROM google/dart:1.13.0

RUN curl -sL https://deb.nodesource.com/setup | bash -
RUN apt-get install -y wget curl gcc libxml2-dev libxslt-dev libcurl4-openssl-dev libreadline6-dev libc6-dev libssl-dev make build-essential zlib1g-dev openssh-server git-core libyaml-dev postfix libpq-dev libicu-dev xvfb unzip chromium nodejs build-essential

# Enable contrib and non-free packages.
RUN echo "deb http://gce_debian_mirror.storage.googleapis.com wheezy contrib non-free" >> /etc/apt/sources.list \
  && echo "deb http://gce_debian_mirror.storage.googleapis.com wheezy-updates contrib non-free" >> /etc/apt/sources.list \
  && echo "deb http://security.debian.org/ wheezy/updates contrib non-free" >> /etc/apt/sources.list
RUN apt-get update

# Install Chromium, required fonts and needed tools.
RUN echo ttf-mscorefonts-installer msttcorefonts/accepted-mscorefonts-eula \
    select true | debconf-set-selections
RUN apt-get install --no-install-recommends -y -q chromium-browser \
    tar wget unzip xvfb xauth \
    ttf-kochi-gothic ttf-kochi-mincho ttf-mscorefonts-installer \
    ttf-indic-fonts ttf-dejavu-core fonts-thai-tlwg

# Install libc6-dev from testing cource.
RUN echo "deb http://ftp.debian.org/debian/ testing main contrib non-free" >> /etc/apt/sources.list
RUN apt-get update
RUN apt-get install --no-install-recommends -y -q libc6-dev
RUN apt-get clean

# Trick to have ttf-indic-fonts-core since ttf-indic-fonts is transitional.
WORKDIR /usr/share/fonts/truetype/ttf-indic-fonts-core
RUN ln -s ../lohit-punjabi/Lohit-Punjabi.ttf lohit_hi.ttf \
  && ln -s ../lohit-tamil/Lohit-Tamil.ttf lohit_ta.ttf \
  && ln -s ../fonts-beng-extra/MuktiNarrow.ttf \
  && ln -s ../lohit-punjabi/Lohit-Punjabi.ttf lohit_pa.ttf

# Install Dartium Content Shell.

WORKDIR /usr/local/content_shell
RUN wget https://storage.googleapis.com/dart-archive/channels/stable/release/latest/dartium/content_shell-linux-x64-release.zip
RUN unzip content_shell-linux-x64-release.zip \
  && rm content_shell-linux-x64-release.zip \
  && mv $(ls) latest
ENV PATH /usr/local/content_shell/latest:$PATH

WORKDIR /
