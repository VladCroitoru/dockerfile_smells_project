FROM haskell:7.10

# update package repository
RUN apt-get update && \
    apt-get install -y libpq-dev
RUN cabal update

# Make sure our app directory exists
RUN mkdir -p /opt/pulsar

# Set the base directory of the following RUN statements
WORKDIR /opt/pulsar

# Make sure log directories exist
RUN mkdir -p /var/log/pulsar

# Create Sandbox
RUN cabal sandbox init

# Install Dependencies into sandbox. Each command is cached by Docker
# so we don't have to reinstall everything unless we make changes to 
# our .cabal file.
COPY ./pulsar.cabal /opt/pulsar/pulsar.cabal
RUN cabal install --only-dependencies -j4 --allow-newer

# Add Application Code
COPY ./src /opt/pulsar/src

# Build Application
RUN cabal build

# COPY assets and misc files into image
COPY ./snaplets /opt/pulsar/snaplets
COPY ./static /opt/pulsar/static
COPY ./.ghci /opt/pulsar/.ghci

# By default, run our application when running a container based on
# this image. Use command line flags to specify log directories.
CMD ["/opt/pulsar/dist/build/pulsar/pulsar",\
     "--access-log", "/var/log/pulsar/access.log",\
     "--error-log", "/var/log/pulsar/error.log"]

