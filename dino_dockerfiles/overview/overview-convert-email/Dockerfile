FROM overview/overview-convert-framework:0.0.17 as framework


FROM alpine:3.10 AS os
RUN apk add --update --no-cache ca-certificates


FROM alpine:3.10 AS test-base
RUN apk add --update --no-cache bats
WORKDIR /app


# alpine's gmime+json-glib packages don't have static variants. We'll need
# to compile them ourselves. (Debian doesn't have json-glib, either, and it
# uses glibc, which shouldn't be statically linked.)
#
# Note the icky hack for mesontest. Newer versions of meson use "meson test";
# older ones allowed "mesontest". json-glib still uses "mesontest".
FROM os AS build
RUN true \
    && apk add --update --no-cache \
        ca-certificates \
        curl \
        bash \
        meson \
        glib-dev \
        glib-static \
        libidn-dev \
        musl-dev \
        util-linux-dev \
        gcc \
        gnu-libiconv \
        gnu-libiconv-dev \
        make \
        tar \
        xz \
    && mkdir -p /build && cd /build \
    && curl -o - --location https://download.gnome.org/sources/gmime/3.2/gmime-3.2.3.tar.xz | tar -Jx \
    && cd gmime-* \
    && ./configure && make -j4 install \
    && cd /build \
    && curl -o - --location https://download.gnome.org/sources/json-glib/1.4/json-glib-1.4.4.tar.xz | tar -Jx \
    && cd json-glib-* \
    && sed -ie 's/json_lib = library/json_lib = static_library/' json-glib/meson.build \
    && echo "#!/bin/sh\nexec meson test \"$@\"" >/usr/bin/mesontest \
    && chmod +x /usr/bin/mesontest \
    && ./configure && make install
WORKDIR /build/convert-email
COPY Makefile Makefile
COPY src/ src/
RUN make


FROM os AS base
WORKDIR /app
COPY --from=framework /app/run /app/
COPY --from=framework /app/convert-stream-to-mime-multipart /app/convert
COPY --from=build /build/convert-email/do-convert-stream-to-mime-multipart /app/
CMD [ "/app/run" ]


FROM base AS dev


# The "test" image is special: we integration-test on Docker Hub by actually
# _running_ the tests as part of the build.
FROM test-base AS test
COPY --from=framework /app/convert-stream-to-mime-multipart /app/convert
COPY --from=build /build/convert-email/do-convert-stream-to-mime-multipart /app/
COPY /test/ /app/test/
RUN ./test/suite.bats
CMD [ "true" ]


FROM base AS production
