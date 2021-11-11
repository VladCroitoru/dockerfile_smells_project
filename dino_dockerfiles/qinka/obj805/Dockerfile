FROM index.docker.io/library/haskell:7.10.2
MAINTAINER qinka
ADD . /src
RUN ls -a /src
RUN cd /src && cabal sandbox init
RUN cabal update
RUN cd /src && cabal install directory
RUN cd /src && cabal install yesod -j9
RUN cd /src && cabal install
RUN cp /src/.cabal-sandbox/bin/* /usr/bin
RUN rm -r src
EXPOSE 3000
CMD "Obj805"
