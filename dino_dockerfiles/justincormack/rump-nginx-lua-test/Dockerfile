# Simple example with rump-nginx-lua

FROM justincormack/rump-nginx-lua

MAINTAINER Justin Cormack

COPY . /usr/src/rump-nginx-lua-test

WORKDIR /usr/src/rump-nginx-lua-test

ENV SUDO_UID=1000

ENV RUMP_VERBOSE=0

RUN \
  tar cf root.tar etc data && \
  rump.tar c -f - /dev > dev.tar && \
  dd if=/dev/zero of=fs.img bs=1k count=10k && \
  chmod a+rw fs.img && \
  rexec rump.newfs fs.img -- /dev/rblock0 && \
  cat dev.tar | rexec rump.dd fs.img -- of=dev.tar && \
  cat root.tar | rexec rump.dd fs.img -- of=root.tar && \
  rexec rump.tar fs.img -- xf dev.tar && \
  rexec rump.tar fs.img -- xf root.tar && \
  rexec rump.rm fs.img -- dev.tar root.tar

ENV RUMP_VERBOSE=1

EXPOSE 80

CMD ["rexec", "nginx", "-nx", "-ro", "fs.img", "-rw", "docker:eth0", "--", "-c", "/data/conf/nginx.conf"]
