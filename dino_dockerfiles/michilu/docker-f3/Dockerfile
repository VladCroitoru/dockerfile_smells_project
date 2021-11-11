FROM debian:jessie AS build

RUN apt-get -q update && apt-get install --no-install-recommends -y -q \
  libparted2 \
  libudev1 \
  ;

ARG \
  f3=v7.0

RUN apt-get -q update && apt-get install --no-install-recommends -y -q \
  ca-certificates \
  curl \
  g++ \
  libparted-dev \
  libudev-dev \
  make \
  && mkdir src \
  && (cd src \
    && curl -sL https://github.com/AltraMayor/f3/archive/${f3}.tar.gz \
    | tar xzf - --strip-components 1 \
    && make \
    && make install \
    && make extra \
    && make install-extra \
  ) \
  && rm -rf src \
  && apt-get purge --auto-remove -y -q \
  ca-certificates \
  curl \
  g++ \
  libparted-dev \
  libudev-dev \
  make \
  ;


FROM busybox

COPY --from=build /usr/local/bin/f3* /usr/local/bin/
COPY --from=build /usr/local/share/man/man1/f3* /usr/local/share/man/man1/

COPY --from=build /lib/x86_64-linux-gnu/libblkid.so.1          /lib/x86_64-linux-gnu/
COPY --from=build /lib/x86_64-linux-gnu/libc.so.6              /lib/x86_64-linux-gnu/
COPY --from=build /lib/x86_64-linux-gnu/libdevmapper.so.1.02.1 /lib/x86_64-linux-gnu/
COPY --from=build /lib/x86_64-linux-gnu/libdl.so.2             /lib/x86_64-linux-gnu/
COPY --from=build /lib/x86_64-linux-gnu/libm.so.6              /lib/x86_64-linux-gnu/
COPY --from=build /lib/x86_64-linux-gnu/libparted.so.2         /lib/x86_64-linux-gnu/
COPY --from=build /lib/x86_64-linux-gnu/libpcre.so.3           /lib/x86_64-linux-gnu/
COPY --from=build /lib/x86_64-linux-gnu/libpthread.so.0        /lib/x86_64-linux-gnu/
COPY --from=build /lib/x86_64-linux-gnu/librt.so.1             /lib/x86_64-linux-gnu/
COPY --from=build /lib/x86_64-linux-gnu/libselinux.so.1        /lib/x86_64-linux-gnu/
COPY --from=build /lib/x86_64-linux-gnu/libudev.so.1           /lib/x86_64-linux-gnu/
COPY --from=build /lib/x86_64-linux-gnu/libuuid.so.1           /lib/x86_64-linux-gnu/
COPY --from=build /lib64/ld-linux-x86-64.so.2                  /lib64/

RUN ls -1 /usr/local/bin/f3*|xargs -I @ @ --version

CMD ls -1 /usr/local/bin/f3*|xargs -I @ @ --version

WORKDIR /root
