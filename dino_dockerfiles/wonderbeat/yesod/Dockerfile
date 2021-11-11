FROM darinmorrison/haskell:0.2.3
MAINTAINER Denis Golovachev <borov.htid@gmail.com>
 
RUN apt-get install -qy zlib1g-dev git
RUN cabal update
RUN cabal install yesod-platform==1.2.* yesod-bin==1.2.*
