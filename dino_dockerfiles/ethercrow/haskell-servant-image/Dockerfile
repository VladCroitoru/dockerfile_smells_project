FROM ubuntu:18.04
ENV LANG C.UTF-8

RUN apt-get update
RUN  apt-get update && \
    apt-get install -y libsdl2-dev libsdl2-image-dev pkg-config && \
    apt-get install -y --no-install-recommends \
            zlib1g-dev libtinfo-dev libsqlite3-0 libsqlite3-dev ca-certificates g++ git curl gnupg2 && \
    (curl -sSL https://get.haskellstack.org/ | sh) && \
    apt-get purge -y --auto-remove curl && \
    rm -rf /var/lib/apt/lists/* /stack.tar.gz

ENV PATH /root/.local/bin:$PATH
ENV RESOLVER lts-11.10

RUN stack install --resolver=$RESOLVER servant-server lucid clay lens

CMD ["stack"]
