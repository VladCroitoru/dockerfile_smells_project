FROM justincormack/luajit2.1
RUN \
  git clone https://github.com/sandstorm-io/capnproto.git && \
  cd capnproto && \
  cd c++ && \
  autoreconf -i && \
  ./configure && \
  make -j6 check && \
  make install && \
  luarocks install lua-capnproto && \
  cd / && curl http://www.kyne.com.au/~mark/software/download/lua-cjson-2.1.0.tar.gz | gunzip | tar xf - && \
  cd lua-cjson-2.1.0 && luarocks make && \
  cd / && git clone https://github.com/justincormack/ljsyscall.git && \
  mkdir -p /usr/local/share/lua/5.1 && cp -a ljsyscall/syscall.lua ljsyscall/syscall /usr/local/share/lua/5.1/
