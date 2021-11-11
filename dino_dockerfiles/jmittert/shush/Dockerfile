FROM haskell

RUN cabal update
ADD ./shush.cabal /opt/shush/shush.cabal
RUN cd /opt/shush && cabal install --only-dependencies -j5

ADD ./app /opt/shush/app
ADD ./src /opt/shush/src
ADD ./LICENSE /opt/shush/LICENSE
RUN cd /opt/shush && cabal install

ENV PATH /root/.cabal/bin:$PATH

EXPOSE 80
ENTRYPOINT ["shush"]
