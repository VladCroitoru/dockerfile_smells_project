
FROM dtinth/kindle-k5-toolchain

# create /mnt/us, /uchi/dist
USER root
RUN mkdir /mnt/us && chown crosstool /mnt/us
USER crosstool
RUN mkdir /uchi/dist
ENV XT arm-kindle_k5-linux-gnueabi

# download and compile ncurses to link against ruby
RUN cd /uchi && wget http://ftp.gnu.org/pub/gnu/ncurses/ncurses-5.6.tar.gz && tar xvzf ncurses-5.6.tar.gz
RUN cd /uchi/ncurses-5.6 && CFLAGS=-fPIC CC=$XT-gcc CXX=$XT-g++ LD=$XT-ld AR=$XT-ar RANLIB=$XT-ranlib ./configure --host=arm-linux --prefix=/mnt/us/opt/ruby_deps
RUN cd /uchi/ncurses-5.6 && make && make install

# download and compile readline to link against ruby
RUN cd /uchi && wget http://ftp.gnu.org/gnu/readline/readline-5.2.tar.gz && tar xvzf readline-5.2.tar.gz
RUN cd /uchi/readline-5.2 && CFLAGS=-fPIC CC=$XT-gcc LD=$XT-ld AR=$XT-ar RANLIB=$XT-ranlib ./configure --host=arm-linux --prefix=/mnt/us/opt/ruby_deps
RUN cd /uchi/readline-5.2 && make && make install

# download and extract ruby
RUN cd /uchi && wget http://cache.ruby-lang.org/pub/ruby/2.1/ruby-2.1.2.tar.gz && tar xvzf ruby-2.1.2.tar.gz

# compile for build machine
WORKDIR /uchi/ruby-2.1.2
RUN ./configure --disable-install-doc && make
USER root
RUN make install
USER crosstool

# compile for kindle
ADD kindle_ruby_configure.sh /kindle_ruby_configure.sh
RUN make clean
RUN bash /kindle_ruby_configure.sh --prefix=/mnt/us/opt/ruby-2.1.2 --disable-install-doc --with-readline-dir=/mnt/us/opt/ruby_deps
RUN true
RUN make
USER root
RUN make install
USER crosstool
RUN cd /mnt/us/opt && tar cvzf /uchi/dist/ruby-2.1.2-kindle-k5.tar.gz ruby-2.1.2

