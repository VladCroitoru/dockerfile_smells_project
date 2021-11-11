FROM mchakravarty/ghc-7.10.2
RUN apt-get update
RUN apt-get install -y --no-install-recommends alex happy 
RUN apt-get install -y --no-install-recommends zlib1g-dev build-essential git ca-certificates libtinfo-dev libgmp-dev autoconf curl vim
RUN git clone https://github.com/ghcjs/ghcjs.git
RUN cabal update
RUN curl -sL https://deb.nodesource.com/setup | bash -
RUN apt-get install -y nodejs
RUN cabal install --reorder-goals --max-backjumps=-1 ./ghcjs
ENV PATH /root/.cabal/bin:$PATH
RUN apt-get install -y automake
RUN ghcjs-boot --dev
WORKDIR /root
RUN git clone https://github.com/xpika/ghcjs-dom.git && cd ghcjs-dom && cabal install --ghcjs
RUN git clone https://github.com/ghcjs/ghcjs-jquery.git && cd ghcjs-jquery && cabal install --ghcjs
RUN git clone https://github.com/ghcjs/diagrams-ghcjs.git && cd diagrams-ghcjs && cabal install --ghcjs

WORKDIR /root/diagrams-ghcjs/test
RUN make
WORKDIR /root/
RUN cabal install snap-server
RUN echo 'ghc -e "Snap.Http.Server.httpServe (Snap.Http.Server.Config.setPort 80 mempty) $ Snap.Util.FileServe.serveDirectoryWith Snap.Util.FileServe.fancyDirectoryConfig  \".\""' > server.sh
ENTRYPOINT ["sh","-c","cd /root/diagrams-ghcjs/test; sh -c 'sh /root/server.sh > /root/log 2>&1 &' ; /bin/bash"]
