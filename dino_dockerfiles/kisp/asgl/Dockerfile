FROM ubuntu

RUN apt-get update

RUN apt-get -y install git build-essential curl autoconf m4 libgmp-dev ragel bundler rlwrap

RUN curl --no-progress-bar --retry 10 -o "gecode-4.3.3.tar.gz" \
  -L "http://www.gecode.org/download/gecode-4.3.3.tar.gz"

RUN curl --no-progress-bar --retry 10 -o "ecl-16.1.2.tgz" \
  -L "https://common-lisp.net/project/ecl/static/files/release/ecl-16.1.2.tgz"

### gecode
RUN tar xfz gecode-4.3.3.tar.gz

ENV GECODEFLAGS "-O3 -pipe -fomit-frame-pointer"

RUN cd gecode-4.3.3 && env CFLAGS="$GECODEFLAGS" CXXFLAGS="$GECODEFLAGS" ./configure \
  --disable-gist --disable-qt --disable-examples --disable-flatzinc --disable-float-vars \
  --prefix=/usr/local

RUN cd gecode-4.3.3 && make && make install
RUN rm -rf gecode-4.3.3*

### ecl
RUN tar xfz ecl-16.1.2.tgz

ENV ECLFLAGS "-O2 -pipe -fomit-frame-pointer"

RUN cd ecl-16.1.2 && env CFLAGS="$ECLFLAGS" CXXFLAGS="$ECLFLAGS" ./configure \
  --enable-threads --with-cxx --with-dffi=included --enable-boehm=included \
  --with-system-gmp \
  --enable-libatomic=included --enable-unicode --prefix=/usr/local

RUN cd ecl-16.1.2 && make && make install
RUN rm -rf ecl-16.1.2*

### asgl
RUN git clone https://github.com/kisp/asgl.git

WORKDIR /asgl

# install cucumber
RUN bundle

RUN autoconf && ./configure --without-gist

ENV ASGL_HOME "/asgl"

RUN bash scripts/generate-make-mk.sh && make

RUN make test

ENV PATH $ASGL_HOME/bin:$PATH
