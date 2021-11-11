FROM swift:5.4.0-focal

ENV WORK_DIR /
WORKDIR ${WORK_DIR}

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y \
  curl \
  dirmngr \
  git \
  libcurl4-openssl-dev \
  libsqlite3-dev \
  sqlite3 \
  libssl-dev \
  libxml2 \
  openssl \
  pkg-config \
  tzdata \
  xz-utils \
  zlib1g-dev \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* 

RUN swift --version
