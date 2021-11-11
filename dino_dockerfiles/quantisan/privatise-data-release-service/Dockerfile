FROM ubuntu:trusty

RUN apt-get update \
  && apt-get install -y --no-install-recommends ca-certificates git \
  && rm -rf /var/lib/apt/lists/*

# Install Julia

ENV JULIA_PATH /usr/local/julia
ENV JULIA_VERSION 0.3.9

RUN mkdir $JULIA_PATH \
  && apt-get update && apt-get install -y \
  curl \
  wget \
  build-essential \
  libgnutls28 \
  && curl -sSL "https://julialang.s3.amazonaws.com/bin/linux/x64/${JULIA_VERSION%[.-]*}/julia-${JULIA_VERSION}-linux-x86_64.tar.gz" \
    | tar -xz -C $JULIA_PATH --strip-components 1 \
  && apt-get purge -y --auto-remove \
    -o APT::AutoRemove::RecommendsImportant=false \
    -o APT::AutoRemove::SuggestsImportant=false \
    curl \
  && rm -rf /var/lib/apt/lists/*

ENV PATH $JULIA_PATH/bin:$PATH

# Install App

ENV JULIA_VER=0.3
ENV JULIA_PKGDIR=/usr/local/.julia/

RUN julia -e 'Pkg.init()'

COPY REQUIRE $JULIA_PKGDIR/v$JULIA_VER/
RUN julia -e 'Pkg.resolve();' \
  # TODO this should be in package manager but Pkg.resolve can't clone a repo
  && julia -e 'Pkg.clone("https://github.com/mrtzh/PrivateMultiplicativeWeights.jl.git")'

WORKDIR /usr/src/app
ADD . /usr/src/app

CMD julia src/main.jl
EXPOSE 8000

