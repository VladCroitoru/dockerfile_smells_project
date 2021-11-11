FROM haskell:7.10

# update packages
RUN apt-get update
RUN cabal update

# Install Dependencies into sandbox. Each command is cached by Docker
# so we don't have to reinstall everything unless we make changes to 
# our .cabal file.
ADD ./site.cabal /opt/server/site.cabal
RUN cd /opt/server && cabal install --only-dependencies -j4

# Add Application Code
ADD ./src /opt/server/src
# Install Application
RUN cd /opt/server && cabal install

# Add production assets and run application

ADD ./static /opt/server/static
ADD ./.ghci /opt/server/.ghci

WORKDIR /opt/server

# put logs somewhere
RUN mkdir /var/log/barebones

# default command to run
CMD ["/opt/server/dist/build/site/site", "--access-log", "/var/log/barebones/access.log", "--error-log", "/var/log/barebones/error.log"]
