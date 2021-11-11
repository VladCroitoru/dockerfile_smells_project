FROM  haskell

# create our src and bin directories and 
# setup src to be our working directory
RUN mkdir -p /opt/game-of-haskell/src
RUN mkdir -p /opt/game-of-haskell/bin
WORKDIR /opt/game-of-haskell/src

# setup our PATH for the bin directory
ENV PATH "$PATH:/opt/game-of-haskell/bin"

# Install GHC using stack, based on the stack.yaml file.
COPY ./stack.yaml /opt/game-of-haskell/src/stack.yaml
RUN stack --no-terminal setup

# Install all dependencies in the .cabal file.
COPY ./game-of-haskell.cabal /opt/game-of-haskell/src/game-of-haskell.cabal
RUN stack --no-terminal test --only-dependencies

# Build application
COPY . /opt/game-of-haskell/src
RUN stack --no-terminal build

# Install application binaries to /opt/game-of-haskell/bin.
RUN stack --no-terminal --local-bin-path /opt/game-of-haskell/bin install

CMD /opt/game-of-haskell/bin/game-of-haskell -p $PORT