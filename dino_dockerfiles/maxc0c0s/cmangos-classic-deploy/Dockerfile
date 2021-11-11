FROM maxc0c0s/cmangos-classic-base:latest

ENV CUSTOM_SCRIPTS_DIR=/custom-scripts.d

RUN apt-get update

RUN apt-get install -y build-essential gcc g++ automake autoconf make patch mysql-server libtool libssl-dev grep binutils zlibc libc6 libbz2-dev cmake subversion

RUN mkdir -p $CUSTOM_SCRIPTS_DIR

RUN useradd -r compiler

USER compiler

COPY entrypoint.sh /usr/local/bin

ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]
