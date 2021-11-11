FROM lennart/tida1vm:0.8


RUN apt-get update -q && apt-get install -yq git-core --no-install-recommends

RUN git clone https://github.com/tidalcycles/Tidal $HOME/Tidal

###
RUN ghc-pkg unregister tidal-midi \
    && ghc-pkg unregister tidal \
    && cd $HOME/Tidal \
    && cabal install


