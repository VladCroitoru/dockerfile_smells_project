FROM alpine:3.13 AS dev

RUN apk add --no-cache gcc git libressl-dev linux-headers make musl-dev perl sqlite-libs

# Install Perl 6
RUN git clone git://github.com/rakudo/rakudo \
 && cd rakudo                                \
 && git checkout 2021.05                     \
 && CFLAGS=-flto ./Configure.pl              \
    --gen-moar                               \
    --moar-option=--ar=gcc-ar                \
    --prefix=/usr                            \
 && make -j`nproc` install                   \
 && strip /usr/bin/perl6

# Install zef
RUN git clone git://github.com/ugexe/zef \
 && cd zef                               \
 && perl6 -Ilib bin/zef install --/test .

WORKDIR /app

COPY META6.json .

RUN /usr/share/perl6/site/bin/zef install --deps-only --/test .

FROM dev

# Avoid having "binaries" in the final image
RUN rm -r /usr/share/perl6/site/bin

FROM scratch

COPY --from=0 /lib/ld-musl-x86_64.so.1 \
              /lib/libz.*              /lib/
COPY --from=0 /usr/bin/perl6           /usr/bin/
COPY --from=0 /usr/bin/rakudo          /usr/bin/
COPY --from=0 /usr/bin/rakudo-m        /usr/bin/ 
COPY --from=0 /usr/lib/libmoar.so      \
              /usr/lib/libcrypto.*     \
              /usr/lib/libsqlite3.*    \
              /usr/lib/libssl.*        /usr/lib/
COPY --from=0 /usr/share/nqp           /usr/share/nqp
COPY --from=0 /usr/share/perl6         /usr/share/perl6


WORKDIR /app

COPY . /app

CMD ["perl6", "-Ilib", "service.p6"]
