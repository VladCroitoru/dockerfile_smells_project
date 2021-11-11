FROM rocker/geospatial:4.1.2@sha256:40079817dada185ae197b08096fd4fda5236ea1717a4fa28ee6ad76456348787

# Enabled to non-ASCII font (especially Japanese) embed in PDF
RUN set -x && \
  apt-get update && \
  apt-get install -y --no-install-recommends \
    cmake \
    curl \ 
    fonts-ipaexfont \
    libmagick++-dev \
    libsecret-1-dev \
    libsodium-dev \
    libssl-dev \
    libzmq3-dev \
    imagemagick \
    libpython3.5 \
    python3-dev \
    python3-setuptools \
    python3-pip \
    unar && \
  apt-get install -y \
    r-cran-bit64 \
    r-cran-data.table \
    r-cran-ggforce \
    r-cran-lwgeom \
    r-cran-reprex \
    r-cran-sf \
    r-cran-usethis && \
  apt-get clean && \
  : "日本語のロケールを有効にする" && \
  localedef -f UTF-8 -i ja_JP ja_JP.UTF-8 && \
  rm -rf /var/lib/apt/lists/*

RUN set -x && \
  : "rust environment" && \
  curl https://sh.rustup.rs -sSf | sh -s -- -y

RUN set -x && \
  ~/.cargo/bin/cargo install gifski
  
ARG GITHUB_PAT

RUN set -x && \
  echo "GITHUB_PAT=$GITHUB_PAT" >> /usr/local/lib/R/etc/Renviron

RUN set -x && \
  : "CRAN経由でのパッケージのインストール" && \
  install2.r --error --ncpus -1 --repos 'https://cran.microsoft.com/snapshot/2021-07-18/' \
    assertr \
    bench \
    classInt \
    colormap \
    config \
    conflicted \
    cowplot \
    cptcity \
    drake \
    dtplyr \
    ensurer \
    furrr \
    gganimate \
    here \
    hrbrthemes \
    naniar \
    patchwork \
    progressr \
    rdrop2 \
    reticulate \
    rnaturalearth \
    roxygen2md \
    scico \
    targets \
    tictoc \
    whoami && \
  rm -rf /tmp/downloaded_packages/ /tmp/*.rds

RUN set -x && \
  : "GitHub経由でのパッケージのインストール" && \
  installGithub.r \
    'ropenscilabs/rnaturalearthhires' && \
  rm -rf /tmp/downloaded_packages/ /tmp/*.rds

USER rstudio

RUN set -x && \
  Rscript -e 'reticulate::install_miniconda(path = "/home/rstudio/.local/share/r-miniconda")'

USER root
