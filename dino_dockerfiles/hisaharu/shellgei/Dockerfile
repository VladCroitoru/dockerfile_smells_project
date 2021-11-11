FROM ubuntu:16.04
MAINTAINER Hisaharu Ishii <hisaharu@gmail.com>
WORKDIR /root
ENV \
  GOLANG_VERSION=1.6.2 \
  GOLANG_DOWNLOAD_SHA256=e40c36ae71756198478624ed1bb4ce17597b3c19d243f3f0899bb5740d56212a \
  GOPATH=/go \
  :=:
ENV \
  GOLANG_DOWNLOAD_URL=https://golang.org/dl/go$GOLANG_VERSION.linux-amd64.tar.gz \
  PATH=$GOPATH/bin:/usr/local/go/bin:/root/.cabal/bin:/root/.egison/bin:$PATH \
  :=:
RUN : \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
      openssh-server \
      ca-certificates \
      git \
      make \
      python \
      haskell-platform \
      libncurses-dev \
      g++ \
      gcc \
      libc6-dev \
      make \
      curl \
 && git clone https://github.com/ryuichiueda/ShellGeiData \
 && git clone https://github.com/usp-engineers-community/Open-usp-Tukubai \
 && git clone https://github.com/greymd/egzact.git \
 && ( cd Open-usp-Tukubai \
      && make install \
    ) \
 && cabal update \
 && cabal install egison egison-tutorial \
 && ( cd egzact \
      && make install \
    ) \
 && curl -fSL "$GOLANG_DOWNLOAD_URL" -o golang.tar.gz \
 && echo "$GOLANG_DOWNLOAD_SHA256  golang.tar.gz" | sha256sum -c - \
 && tar -C /usr/local -xzf golang.tar.gz \
 && rm golang.tar.gz \
 && mkdir -p "$GOPATH/src" "$GOPATH/bin" \
 && chmod -R a+rwx "$GOPATH" \
 && go get -v github.com/yudai/gotty \
 && :
EXPOSE 22 8080
CMD gotty -w bash
ADD sshd.sh /sshd.sh

