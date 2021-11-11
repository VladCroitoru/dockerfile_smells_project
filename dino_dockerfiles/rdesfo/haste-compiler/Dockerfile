FROM haskell:7.10.3

RUN apt-get update \
    && apt-get -y install zlib1g-dev \
                          libtinfo-dev \
                          libgmp-dev \
                          libbz2-dev \
    --no-install-recommends \ 
    && rm -rf /var/lib/apt/lists/*

RUN groupadd -g 1000 user \
    && useradd --create-home -d /home/user -g user -u 1000 user 

COPY . /home/user/app
RUN  chown -R user:user /home/user/app

USER user
WORKDIR /home/user/app

ENV PATH /home/user/.cabal/bin:$PATH

RUN cabal update && \
    cabal install

RUN haste-boot --force --local
ENTRYPOINT ["hastec"]
