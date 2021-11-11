FROM alpine:3.14

RUN \
  apk add \
      --no-cache \
    bash \
    build-base \
    curl \
    curl-dev \
    expat-dev \
    libgit2-dev \
    libsodium-dev \
    libxml2-dev \
    linux-headers \
    openssl-dev \
    R \
    R-dev \
    R-doc

# Specific old package versions required by R `httpuv` package, which is a
# dependency of `beakr`.
# See <https://github.com/rstudio/httpuv/issues/280#issuecomment-713060805>
RUN \
  apk add \
      --no-cache \
      --repository=http://dl-cdn.alpinelinux.org/alpine/v3.11/main \
    autoconf=2.69-r2 \
    automake=1.16.1-r0

# Install udunits package and database from source.
ENV UDUNITS_VERSION='2.2.28'
WORKDIR "/tmp"
RUN \
  curl \
    --output "udunits-${UDUNITS_VERSION}.tar.gz" \
    "https://artifacts.unidata.ucar.edu/repository/downloads-udunits/udunits-${UDUNITS_VERSION}.tar.gz" \
    && \
  tar -xzf "udunits-${UDUNITS_VERSION}.tar.gz" \
    && \
  cd "udunits-${UDUNITS_VERSION}" \
    && \
  ./configure \
    --prefix=/usr \
    && \
  make install \
    && \
  cd '/tmp' \
    && \
  rm -rf \
    "/tmp/udunits-${UDUNITS_VERSION}.tar.gz" \
    "/tmp/udunits-${UDUNITS_VERSION}"

RUN \
  Rscript -e \
    'install.packages("devtools", repos = "https://mirror.las.iastate.edu/CRAN/")' \
        && \
  Rscript -e \
    'remotes::install_github("tidyverse/readxl@649982ab3769e5b41753b9e543887f95c487425b")' \
        && \
  Rscript -e \
    'install.packages(c("PKI", "anthro", "beakr", "here", "progress", "sodium", "tidyverse", "units"), repos = "https://mirror.las.iastate.edu/CRAN/")'

WORKDIR /app
COPY . /app

CMD ["./run.R"]
