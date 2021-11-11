
# Dockerfile adapted from https://github.com/docker-library/python
# for building python v3.8 some dependencies are not required and 
# can be removed when compiling python
#

FROM ubuntu:18.04

# ensure local python is preferred over distribution python
ENV PATH /usr/local/bin:$PATH

# runtime dependencies
RUN set -eux; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		ca-certificates \
		netbase \
	; \
	rm -rf /var/lib/apt/lists/*

ENV GPG_KEY E3FF2839C048B25C084DEBE9B26995E310250568
ENV PYTHON_VERSION 3.8.11

RUN set -ex \
	\
	&& savedAptMark="$(apt-mark showmanual)" \
	&& apt-get update \
  && DEBIAN_FRONTEND=noninteractive \
  apt-get install -y --no-install-recommends \
		dpkg-dev \
		gcc \
		libbluetooth-dev \
		libbz2-dev \
		libc6-dev \
		libexpat1-dev \
		libffi-dev \
		libgdbm-dev \
		liblzma-dev \
		libncursesw5-dev \
		libreadline-dev \
		libsqlite3-dev \
		libssl-dev \
		make \
		tk-dev \
		uuid-dev \
		wget \
		xz-utils \
		zlib1g-dev \
# as of Stretch, "gpg" is no longer included by default
		$(command -v gpg > /dev/null || echo 'gnupg dirmngr') \
	\
	&& wget -O python.tar.xz "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz" \
	&& wget -O python.tar.xz.asc "https://www.python.org/ftp/python/${PYTHON_VERSION%%[a-z]*}/Python-$PYTHON_VERSION.tar.xz.asc" \
	&& export GNUPGHOME="$(mktemp -d)" \
	&& gpg --batch --keyserver hkps://keys.openpgp.org --recv-keys "$GPG_KEY" \
	&& gpg --batch --verify python.tar.xz.asc python.tar.xz \
	&& { command -v gpgconf > /dev/null && gpgconf --kill all || :; } \
	&& rm -rf "$GNUPGHOME" python.tar.xz.asc \
	&& mkdir -p /usr/src/python \
	&& tar -xJC /usr/src/python --strip-components=1 -f python.tar.xz \
	&& rm python.tar.xz \
	\
	&& cd /usr/src/python \
	&& gnuArch="$(dpkg-architecture --query DEB_BUILD_GNU_TYPE)" \
	&& ./configure \
		--build="$gnuArch" \
		--enable-loadable-sqlite-extensions \
		--enable-optimizations \
		--enable-option-checking=fatal \
		--enable-shared \
		--with-system-expat \
		--with-system-ffi \
		--without-ensurepip \
	&& make -j "$(nproc)" \
		LDFLAGS="-Wl,--strip-all" \
	&& make install \
	&& rm -rf /usr/src/python \
	\
	&& find /usr/local -depth \
		\( \
			\( -type d -a \( -name test -o -name tests -o -name idle_test \) \) \
			-o \( -type f -a \( -name '*.pyc' -o -name '*.pyo' -o -name '*.a' \) \) \
			-o \( -type f -a -name 'wininst-*.exe' \) \
		\) -exec rm -rf '{}' + \
	\
	&& ldconfig \
	\
	&& apt-mark auto '.*' > /dev/null \
	&& apt-mark manual $savedAptMark \
	&& find /usr/local -type f -executable -not \( -name '*tkinter*' \) -exec ldd '{}' ';' \
		| awk '/=>/ { print $(NF-1) }' \
		| sort -u \
		| xargs -r dpkg-query --search \
		| cut -d: -f1 \
		| sort -u \
		| xargs -r apt-mark manual \
	&& apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
	&& rm -rf /var/lib/apt/lists/* \
	\
	&& python3 --version

RUN cd /usr/local/bin \
	&& ln -s idle3 idle \
	&& ln -s pydoc3 pydoc \
	&& ln -s python3 python \
	&& ln -s python3-config python-config

# if this is called "PIP_VERSION", pip explodes with "ValueError: invalid truth value '<VERSION>'"
ENV PYTHON_PIP_VERSION 21.1.3
# https://github.com/pypa/get-pip
ENV PYTHON_GET_PIP_URL https://github.com/pypa/get-pip/raw/a1675ab6c2bd898ed82b1f58c486097f763c74a9/public/get-pip.py
ENV PYTHON_GET_PIP_SHA256 6665659241292b2147b58922b9ffe11dda66b39d52d8a6f3aa310bc1d60ea6f7

RUN set -ex; \
	\
	savedAptMark="$(apt-mark showmanual)"; \
	apt-get update; \
	apt-get install -y --no-install-recommends wget; \
	\
	wget -O get-pip.py "$PYTHON_GET_PIP_URL"; \
	echo "$PYTHON_GET_PIP_SHA256 *get-pip.py" | sha256sum --check --strict -; \
	\
	apt-mark auto '.*' > /dev/null; \
	[ -z "$savedAptMark" ] || apt-mark manual $savedAptMark; \
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
	rm -rf /var/lib/apt/lists/*; \
	\
	python get-pip.py \
		--disable-pip-version-check \
		--no-cache-dir \
		"pip==$PYTHON_PIP_VERSION" \
	; \
	pip --version; \
	\
	find /usr/local -depth \
		\( \
			\( -type d -a \( -name test -o -name tests -o -name idle_test \) \) \
			-o \
			\( -type f -a \( -name '*.pyc' -o -name '*.pyo' \) \) \
		\) -exec rm -rf '{}' +; \
	rm -f get-pip.py

#ARG PLINK2_URL="https://s3.amazonaws.com/plink2-assets/alpha2/plink2_linux_x86_64.zip"
#ARG PLINK2_DEV_URL="https://s3.amazonaws.com/plink2-assets/plink2_linux_x86_64_20210701.zip"
#ARG PLINK_URL="https://s3.amazonaws.com/plink1-assets/plink_linux_x86_64_20210606.zip"
#ARG GCTA_URL="https://cnsgenomics.com/software/gcta/bin/gcta_1.93.2beta.zip"
# setup plink

## Freeze version of tools used
COPY bin/plink2_linux_x86_64_20210920.zip /root/plink2_linux_x86_64.zip
COPY bin/gcta_1.93.2beta.zip /root/gcta_1.93.2beta.zip
COPY bin/plink_linux_x86_64_20210606.zip /root/plink_linux_x86_64.zip

RUN set -ex; \
  \
  savedAptMark="$(apt-mark showmanual)"; \
  apt-get update; \
  apt-get install -y --no-install-recommends \
  unzip ;\
  \
  cd /root; \
  unzip plink2_linux_x86_64.zip; \
  unzip plink_linux_x86_64.zip; \
  unzip gcta_1.93.2beta.zip; \
 	\
  apt-mark auto '.*' > /dev/null; \
	[ -z "$savedAptMark" ] || apt-mark manual $savedAptMark; \
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
	rm -rf /var/lib/apt/lists/*; \
  \
  mv plink2 /usr/local/bin; \
  mv plink /usr/local/bin; \
  mv prettify /usr/local/bin; \
  mv gcta_1.93.2beta/gcta64 /usr/local/bin; \
  \
  rm -rf plink2_linux_x86_64.zip; \
  rm -rf plink_linux_x86_64.zip; \
  rm -rf gcta_1.93.2beta.zip

ARG BCFTOOLS_URL="https://github.com/samtools/bcftools/releases/download/1.11/bcftools-1.11.tar.bz2"
ENV BCFTOOLS_PLUGINS /usr/src/bcftools-1.11/plugins
# setup bcftools v1.11
RUN set -ex; \
  \
  apt-get update; \
  apt-get install -y --no-install-recommends \
  libc6-dev \
  zlib1g-dev \
  libbz2-dev \
  libgsl0-dev \
  libperl-dev \
  liblzma-dev \
  libcurl4-openssl-dev \
  tabix; \
  savedAptMark="$(apt-mark showmanual)"; \
  apt-get install -y --no-install-recommends wget \
  gcc \
  make; \
  wget -O bcftools-1.11.tar.bz2 "$BCFTOOLS_URL"; \
  tar -xjf bcftools-1.11.tar.bz2 -C /usr/src; \
  rm bcftools-1.11.tar.bz2; \
  cd /usr/src/bcftools-1.11; \
  ./configure --enable-libgsl --enable-perl-filters; \
  make; \
  make install; \
 	\
  apt-mark auto '.*' > /dev/null; \
	[ -z "$savedAptMark" ] || apt-mark manual $savedAptMark; \
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
	rm -rf /var/lib/apt/lists/*

ARG METAL_META_URL="https://github.com/statgen/METAL/archive/refs/tags/2020-05-05.tar.gz"

RUN set -ex; \
  \
  apt-get update; \
  apt-get install -y --no-install-recommends zlib1g-dev; \
  savedAptMark="$(apt-mark showmanual)"; \
  apt-get install -y --no-install-recommends wget \
  gcc \
  g++ \
  make \
  cmake; \
  wget -O metal_20200505.tar.gz "$METAL_META_URL"; \
  tar -xzf metal_20200505.tar.gz -C /usr/src/; \
  cd /usr/src/METAL-2020-05-05; \
  mkdir build && cd build; \
  cmake -DCMAKE_BUILD_TYPE=Release ..; \
  make; \
  make test; \
  make install; \ 
  ln -s /usr/src/METAL-2020-05-05/build/bin/metal /usr/local/bin/metal 


ARG LIFTOVER_URL="http://hgdownload.soe.ucsc.edu/admin/exe/linux.x86_64/liftOver"
# setup liftOver
RUN set -ex; \
   \
  savedAptMark="$(apt-mark showmanual)"; \
  apt-get update; \
  apt-get install -y --no-install-recommends wget; \
  \
  wget -O /usr/local/bin/liftOver "$LIFTOVER_URL"; \
  \
  apt-mark auto '.*' > /dev/null; \
	[ -z "$savedAptMark" ] || apt-mark manual $savedAptMark; \
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
	rm -rf /var/lib/apt/lists/*; \
  \
  chmod +x /usr/local/bin/liftOver

ARG UCSC_hg38_REF="https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz"
ARG UCSC_hg18_CHAIN="https://hgdownload.cse.ucsc.edu/goldenpath/hg18/liftOver/hg18ToHg38.over.chain.gz"
ARG UCSC_hg19_CHAIN="https://hgdownload.cse.ucsc.edu/goldenpath/hg19/liftOver/hg19ToHg38.over.chain.gz"
ENV GWAS_RESOURCE_DIR="/srv/GWAS-Pipeline"
ENV GWAS_OUTPUT_DIR="/mnt/gwas_results"
ENV ADDI_QC_PIPELINE="/usr/src/ADDI-GWAS-QC-pipeline/addi_qc_pipeline.py"

# download reference files
RUN set -ex; \
  \
  savedAptMark="$(apt-mark showmanual)"; \
  apt-get update; \
  apt-get install -y --no-install-recommends wget; \
  \
  mkdir -p $GWAS_RESOURCE_DIR/References/Genome; \
  mkdir -p $GWAS_RESOURCE_DIR/References/Scripts; \
  mkdir -p $GWAS_RESOURCE_DIR/References/liftOver; \
  mkdir -p $GWAS_RESOURCE_DIR/References/ref_panel; \
  \
  wget -O $GWAS_RESOURCE_DIR/References/Genome/hg38.fa.gz "$UCSC_hg38_REF"; \
  wget -O $GWAS_RESOURCE_DIR/References/liftOver/hg19ToHg38.over.chain.gz "$UCSC_hg19_CHAIN"; \
  wget -O $GWAS_RESOURCE_DIR/References/liftOver/hg18ToHg38.over.chain.gz "$UCSC_hg18_CHAIN"; \
  \
  apt-mark auto '.*' > /dev/null; \
	[ -z "$savedAptMark" ] || apt-mark manual $savedAptMark; \
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
	rm -rf /var/lib/apt/lists/*


ARG BUILD_VER=""

COPY References/ancestry_ref_panel.tar.gz /root
COPY Scripts/process1.sh $GWAS_RESOURCE_DIR/References/Scripts

RUN set -ex; \
  tar -xvzf /root/ancestry_ref_panel.tar.gz -C $GWAS_RESOURCE_DIR/References/ref_panel; \
  rm /root/ancestry_ref_panel.tar.gz; \
  chmod +x $GWAS_RESOURCE_DIR/References/Scripts/process1.sh

ENV IMAGE_BUILD_VER=$BUILD_VER
ARG PY_GALLOP_URL="https://github.com/michael-ta/GALLOP-Python"

# setup GALLOP-Python and install viz tools
RUN set -ex; \
  savedAptMark="$(apt-mark showmanual)"; \
  apt-get update; \
  apt-get install -y --no-install-recommends git \
  ca-certificates; \ 
  cd /usr/src; \
  git clone "$PY_GALLOP_URL"; \
  pip install -r GALLOP-Python/requirements.txt; \
  pip install qmplot; \
  pip install plotly; \
  pip install kaleido; \
  \
  apt-mark auto '.*' > /dev/null; \
	[ -z "$savedAptMark" ] || apt-mark manual $savedAptMark; \
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
	rm -rf /var/lib/apt/lists/*; \
  \
  chmod +x GALLOP-Python/gallop.py; \
  ln -s /usr/src/GALLOP-Python/gallop.py /usr/local/bin/gallop

ARG GENOTOOLS_URL="https://github.com/dvitale199/GenoTools"
ARG GWAS_QC_URL="https://github.com/dvitale199/ADDI-GWAS-QC-pipeline"

RUN set -ex; \
  savedAptMark="$(apt-mark showmanual)"; \
  apt-get update; \
  apt-get install -y --no-install-recommends git \
  ca-certificates; \ 
  cd /usr/src; \
  git clone "$GENOTOOLS_URL"; \
  git clone "$GWAS_QC_URL"; \
  cd GenoTools && pip install .;\
  \
  pip install tables; \
  \
  apt-mark auto '.*' > /dev/null; \
	[ -z "$savedAptMark" ] || apt-mark manual $savedAptMark; \
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
	rm -rf /var/lib/apt/lists/*
