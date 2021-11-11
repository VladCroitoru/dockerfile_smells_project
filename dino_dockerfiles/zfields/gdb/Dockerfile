# `build` Target

## Base Image
FROM alpine:latest as build

## Install Slicer Dependencies
RUN ["/bin/ash","-c","\
    apk --no-cache add \
     g++ \
     gcc \
     gfortran \
     gnupg \
     linux-headers \
     make \
     texinfo \
     wget \
 && rm -rf /var/cache/apk/* \
"]

## Install GNU GDB
RUN ["/bin/ash","-c","\
    mkdir gdb-build \
 && cd gdb-build \
 && wget https://ftp.gnu.org/gnu/gdb/gdb-8.1.tar.xz \
 && wget https://ftp.gnu.org/gnu/gdb/gdb-8.1.tar.xz.sig \
 && wget https://ftp.gnu.org/gnu/gnu-keyring.gpg \
 && gpg --import ./gnu-keyring.gpg \
 && gpg --verify --keyring ./gnu-keyring.gpg gdb-8.1.tar.xz.sig \
 && tar -xvf gdb-8.1.tar.xz \
 && cd gdb-8.1 \
 && ./configure --prefix=/usr \
 && make \
 && make -C gdb install \
 && cd .. \
 && rm -rf gdb-build/ \
"]

# `gdb` Target

## Base Image
FROM alpine:latest as gdb

## Set execution environment
COPY --from=build /usr/bin/gdb /usr/bin/gdb

## Install Slicer Dependencies
RUN ["/bin/ash","-c","\
    apk --no-cache add \
     libgcc \
     libstdc++ \
     musl \
     openssh \
 && rm -rf /var/cache/apk/* \
"]

ENTRYPOINT ["gdb"]
