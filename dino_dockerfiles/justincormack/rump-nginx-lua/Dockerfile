# Build nginx with Docker

FROM justincormack/frankenlibc

MAINTAINER Justin Cormack

COPY . /usr/src/rump-nginx-lua

WORKDIR /usr/src/rump-nginx-lua

ENV RUMPRUN_CC=rumprun-cc \
  CC=rumprun-cc \
  LUA_LIB=/usr/local/lib \
  LUA_INC=/usr/local/include \
  DEVEL_KIT_PATH=/usr/src/rump-nginx-lua/ngx_devel_kit-0.2.19 \
  LUA_MOD_PATH=/usr/src/rump-nginx-lua/lua-nginx-module-0.9.16 \
  PCRE_PATH=/usr/src/rump-nginx-lua/pcre-8.37

# make uname the NetBSD one
RUN cd /usr/local/bin && ln -s rump.uname uname

RUN \
  curl http://nginx.org/download/nginx-1.9.2.tar.gz | tar xfz - && \
  curl https://codeload.github.com/simpl/ngx_devel_kit/tar.gz/v0.2.19 | tar xzf - && \
  curl https://codeload.github.com/openresty/lua-nginx-module/tar.gz/v0.9.16 | tar xzf - && \
  curl ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.37.tar.gz | tar xzf - && \
  curl http://www.lua.org/ftp/lua-5.1.5.tar.gz | tar xzf - && \
  cd lua-5.1.5 && sed -i 's/CC= gcc//' src/Makefile && make bsd && make install && cp src/lua /usr/local/bin/rump.lua && cd .. && \
  cd nginx-1.9.2 && \
  ./configure \
  --conf-path=/data/conf/nginx.conf \
  --sbin-path=/none \
  --pid-path=/tmp/nginx.pid \
  --lock-path=/tmp/nginx.lock \
  --error-log-path=/tmp/error.log \
  --http-log-path=/tmp/access.log \
  --http-client-body-temp-path=/tmp/client-body \
  --http-proxy-temp-path=/tmp/proxy \
  --http-fastcgi-temp-path=/tmp/fastcgi \
  --http-scgi-temp-path=/tmp/scgi \
  --http-uwsgi-temp-path=/tmp/uwsgi \
  --with-ipv6 \
  --add-module=${DEVEL_KIT_PATH} \
  --add-module=${LUA_MOD_PATH} \
  --with-pcre=${PCRE_PATH} \
  && make && \
  cp objs/nginx /usr/local/bin && make clean && cd .. && \
  rm -rf ngx_devel_kit-0.2.19 lua-nginx-module-0.9.15 pcre-8.37

ENV SUDO_UID=1000

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

ENTRYPOINT ["rexec"]

CMD ["nginx", "-nx", "-ro", "fs.img", "-rw", "docker:eth0", "--", "-c", "/data/conf/nginx.conf"]
