FROM heroku/cedar:14

ENV LANG en_US.UTF-8
# Cabal and ghc binaries
ENV PATH /root/.cabal/bin:/opt/cabal/1.22/bin:/opt/ghc/7.10.3/bin:$PATH

# Heroku assumes we'll put everything in /app/user
RUN mkdir -p /app/user
WORKDIR /app/user

# Install the Haskell platform
RUN if [ $(dpkg-query -W -f='${Status}' ghc-7.10.3 2>/dev/null | grep -c "ok installed") -eq 0 ]; then \
    apt-get update; \
    apt-get install -y software-properties-common; \
    add-apt-repository -y ppa:hvr/ghc; \
    apt-get update; \
    apt-get install -y cabal-install-1.22 ghc-7.10.3; \
    apt-get clean; \
  fi

# Install application framework in a separate layer for caching
ONBUILD COPY ./cabal-bootstrap .
ONBUILD RUN cabal update \
  && cabal install $(cat cabal-bootstrap)

# Copy over configuration for building the app, including frozen cabal config
ONBUILD COPY cabal.config .
ONBUILD COPY *.cabal .

# Build dependencies so that if we change something later we'll have a Docker
# cache of up to this point.
ONBUILD RUN cabal sandbox init\
  && cabal install --only-dependencies -j3 -O1

ONBUILD COPY . /app/user

# Run pre-build script if it exists (compile CSS, etc)
ONBUILD RUN if [ -x bin/pre-build ]; then bin/pre-build; fi

# Configure the build
ONBUILD RUN cabal configure -O1 --enable-executable-stripping

# Build and copy the executables into the app
ONBUILD RUN cabal install --prefix=$(pwd) --bindir=$(pwd)

# Clean up
ONBUILD RUN cabal clean

# Run post-build script if it exists (further cleaning tasks, etc.)
ONBUILD RUN if [ -x bin/post-build ]; then bin/post-build; fi
