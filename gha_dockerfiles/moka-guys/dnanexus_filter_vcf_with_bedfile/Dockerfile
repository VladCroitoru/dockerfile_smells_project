FROM python:3.9

LABEL author="Rachel Duffin" \
      description="Bcftools v1.13" \
      maintainer="rachel.duffin2@nhs.net"

# Install dependencies
RUN apt update && apt install -y libgsl-dev=2.6+dfsg-2 libperl-dev=5.32.1-4+deb11u1 && \
    git clone --recurse-submodules git://github.com/samtools/htslib.git --branch 1.13 

# Install bcftools v1.13
RUN git clone https://github.com/samtools/bcftools.git --branch 1.13 && \
    cd bcftools && \
    autoheader && autoconf && ./configure --enable-libgsl --enable-perl-filters && \
    make && \
    make install

RUN mkdir -p /data
WORKDIR /data

ENTRYPOINT [ "bcftools" ]