FROM ubuntu:focal

MAINTAINER Daniel Mulholland <dan.mulholland@gmail.com>

ENV JAVA_HOME /jdk1.8.0_112
ENV PATH $PATH:$JAVA_HOME/bin:/fopub/bin
ENV BACKENDS /asciidoctor-backends
ENV GVM_AUTO_ANSWER true
ENV ASCIIDOCTOR_VERSION "2.0.10"

# Set the locale
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y locales tzdata

RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales && \
    update-locale LANG=en_US.UTF-8

ENV LANG en_US.UTF-8

# Now let's get cracking

RUN apt-get update && apt-get install -y --no-install-recommends \
    bison \
    build-essential \
    cmake \
    curl \
    findutils \
    fonts-lyx \
    flex \
    gcc \
    git \
    git-lfs \
    gnupg2 \
    graphviz \
    imagemagick \
    inkscape \
    libcairo2-dev \
    libffi-dev \
    libgdk-pixbuf2.0-dev \
    libgif-dev \
    libgit2-dev \
    libjpeg-dev \
    libpango1.0-dev \
    libssl-dev \
    libtool \
    libxml2-dev \
    make \
    nano \
    openjdk-8-jdk \
    pkg-config \
    pandoc \
    patch \
    plantuml \
    python3 \
    python3-pip \
    python-all-dev \
    python-setuptools \
    python3-setuptools \
    ruby \
    ruby-all-dev \
    rubygems \
    ruby-nokogiri \
    sudo \
    tar \
    unzip \
    zip \
    wget \
    zlib1g-dev

RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list' \
    && apt-get update \
    && apt-get install -y google-chrome-unstable fonts-ipafont-gothic fonts-wqy-zenhei fonts-thai-tlwg fonts-kacst fonts-freefont-ttf \
      --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -

RUN apt-get update && apt-get install -y --no-install-recommends \
    nodejs \
    && rm -rf /var/lib/apt/lists/*

RUN  gem install --no-document asciidoctor --version $ASCIIDOCTOR_VERSION \
  && gem install --no-document asciidoctor-pdf --version 1.5.3 \
  && gem install --no-document asciidoctor-diagram \
  && gem install --no-document asciidoctor-katex \
  && gem install --no-document asciidoctor-mathematical \
  && gem install --no-document asciidoctor-epub3 --version 1.5.0.alpha.9 \
  && gem install --no-document rake \
  && gem install --no-document epubcheck --version 3.0.1 \
  && gem install --no-document kindlegen --version 3.0.1 \
  && gem install --no-document asciidoctor-confluence \
  && gem install --no-document bundler \
  && gem install --no-document rouge coderay pygments.rb thread_safe epubcheck kindlegen \
  && gem install --no-document slim \
  && gem install --no-document haml tilt \
  && gem install --no-document asciidoctor-revealjs \
  && gem install --no-document rugged \
  && gem install --no-document asciidoctor-rouge \
  && gem install --no-document fastimage \
  && gem install --no-document html-proofer \
  && gem install --no-document asciidoctor-question \
  && gem install --no-document specific_install



ARG TEST=STARTFROMHERE1

RUN gem specific_install -l https://gitlab.com/danyill/pdf-hyperlinking-play -b release_v0.3.0

RUN pip3 install actdiag blockdiag seqdiag nwdiag

RUN git clone https://github.com/danyill/htmldiff \
    && cd htmldiff \
    && python3 setup.py sdist \
    && python3 setup.py install

# Install puppeteer so it's available in the container.
RUN npm config set user 0 \
    && npm config set unsafe-perm true \
    && npm install -g yarn  \
    && npm install -g puppeteer \
    && npm install -g --force @asciidoctor/core @asciidoctor/cli asciidoctor asciidoctor-pdf asciidoctor-katex asciidoctor-kroki gulp-cli vega vega-cli vega-lite vega-embed

WORKDIR /documents
VOLUME /documents

CMD ["/bin/bash"]
