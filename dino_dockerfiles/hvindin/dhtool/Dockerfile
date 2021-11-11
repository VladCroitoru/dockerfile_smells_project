FROM docker.io/alpine:3.6
ENV FASM_VERSION=1.72 HEAVY_THING_VERSION=1.20
RUN apk add --no-cache curl binutils && \
    mkdir /usr/share/fasm  && \
  curl -Ss https://flatassembler.net/fasm-${FASM_VERSION}.tgz | \
    tar xzC /usr/share/fasm --strip-components=1 --exclude=fasm/tools --exclude=fasm/source --exclude=fasm/examples --exclude=fasm/whatsnew.txt --exclude=fasm/fasm --exclude=fasm/fasm.txt && \
  mkdir /usr/share/heavything && \
  curl -Ss https://2ton.com.au/HeavyThing-${HEAVY_THING_VERSION}.tar.gz | \
    tar xzC /usr/share/heavything --strip-components=1 && \
  cd /usr/share/heavything/dhtool && \
  /usr/share/fasm/fasm.x64 -m 524288 dhtool.asm && \
  ld -o dhtool dhtool.o && \
  find /usr/share/heavything/ -not -iname 'dhtool' -and -not -iname 'LICENSE' -and -not -iname heavything -delete && \
  ln -s /usr/share/heavything/dhtool/dhtool /usr/bin/dhtool && \
  rm -rf /usr/share/fasm && \
  apk del --no-cache curl binutils binutils-libs ca-certificates libssh2 libcurl
COPY dhtool-wrapper.sh /usr/bin/dhtool-wrapper.sh
ENTRYPOINT ["/usr/bin/dhtool-wrapper.sh"]
