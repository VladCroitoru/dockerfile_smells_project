FROM r-base:3.4.0

MAINTAINER kirillseva "https://github.com/kirillseva"

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libcurl4-openssl-dev \
    libxml2-dev \
    libpq-dev \
    postgresql \
    postgresql-contrib \
    libtiff5-dev \
    libgmp-dev \
    libssl-dev \
    s3cmd \
    git \
    curl \
    cmake \
    python2.7 \
    python-pip \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

RUN install2.r --error \
    --deps TRUE \
    curl \
    jsonlite \
    httr \
    yaml \
    digest \
    crayon \
    remotes

RUN installGithub.r \
    robertzk/lockbox@0.2.4.7

CMD ["R"]
