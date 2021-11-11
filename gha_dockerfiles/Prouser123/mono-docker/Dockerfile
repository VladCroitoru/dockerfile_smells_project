# Mono alpine dockerfile (work in progress)
# Parts of this dockerfile are taken from the mono package APKBUILD <https://git.alpinelinux.org/aports/tree/testing/mono/APKBUILD>

FROM alpine:3.14 as builder

ENV MONO_VERSION=6.12.0.122

COPY runtime-makefile-am.patch /src/runtime-makefile-am.patch

RUN cd /src && \
    wget -O mono.tar.xz https://download.mono-project.com/sources/mono/mono-$MONO_VERSION.tar.xz && \
    echo "Extracting mono.tar.xz (verbose disabled).." && \
	tar xf mono.tar.xz && \
    cd mono-$MONO_VERSION && \
    # Install build deps
    echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories && \
    apk add --no-cache libgdiplus-dev@testing zlib-dev linux-headers git autoconf libtool automake build-base gettext cmake python3 curl && \
	# Patch runtime/Makefile.am to ignore output 
	git apply ../runtime-makefile-am.patch && \
	# Set env variables (from APKBUILD)
	# Based on Fedora and SUSE package.
	export CFLAGS="$CFLAGS -fno-strict-aliasing" && \
    # Run autogen (from APKBUILD)
	# Run autogen to fix supplied configure linker issues with make install.
	./autogen.sh \
		--build=$CBUILD \
		--host=$CHOST \
		--prefix=/usr \
		--sysconfdir=/etc \
		--mandir=/usr/share/man \
		--infodir=/usr/share/info \
		--localstatedir=/var \
		--disable-rpath \
		--disable-boehm \
		--enable-parallel-mark \
		--with-mcs-docs=no \
		--without-sigaltstack && \
	make -j$(nproc) && \
	# Run make install (from APKBUILD)
	make -j$(nproc) DESTDIR="/src/build/" install && \
	# cd into build dir and remove unnecessary files (from APKBUILD)
	cd /src/build && \
	# > Remove .la files.
	rm ./usr/lib/*.la; \
	# > Remove Windows-only stuff.
	rm -r ./usr/lib/mono/*/Mono.Security.Win32* || echo "rm likely errored, continuing"; \
	rm ./usr/lib/libMonoSupportW.* || echo "rm likely errored, continuing";

# Second stage: Create a docker image with only the mono runtime + runtime deps (fresh image)
FROM alpine:3.14

COPY --from=builder /src/build/ /

# Runtime deps from mono edge/testing package
RUN apk add --no-cache libgcc python3 zlib && \
	# Sanity check, can we get the mono version?
	mono -V