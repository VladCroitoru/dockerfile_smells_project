FROM ubuntu:20.04 AS builder

ENV DEBIAN_FRONTEND noninteractive

COPY --from=dceoy/samtools:latest /usr/local/src/samtools /usr/local/src/samtools
COPY --from=dceoy/bwa:latest /usr/local/src/bwa /usr/local/src/bwa
COPY --from=dceoy/bwa-mem2:latest /usr/local/src/bwa-mem2 /usr/local/src/bwa-mem2
COPY --from=dceoy/trim_galore:latest /usr/local/src/FastQC /usr/local/src/FastQC
COPY --from=dceoy/trim_galore:latest /usr/local/src/TrimGalore /usr/local/src/TrimGalore
COPY --from=dceoy/bcftools:latest /usr/local/src/bcftools /usr/local/src/bcftools
COPY --from=dceoy/bedtools:latest /usr/local/src/bedtools2 /usr/local/src/bedtools2
COPY --from=dceoy/gatk:latest /opt/conda /opt/conda
COPY --from=dceoy/gatk:latest /opt/gatk /opt/gatk
COPY --from=dceoy/manta:latest /opt/manta /opt/manta
COPY --from=dceoy/strelka:latest /opt/strelka /opt/strelka
COPY --from=dceoy/delly:latest /usr/local/bin/delly /usr/local/bin/delly
COPY --from=dceoy/msisensor:latest /usr/local/bin/msisensor /usr/local/bin/msisensor
COPY --from=dceoy/snpeff:latest /opt/snpEff /opt/snpEff
COPY --from=dceoy/vep:latest /usr/local/src/kent /usr/local/src/kent
COPY --from=dceoy/vep:latest /usr/local/src/bioperl-ext /usr/local/src/bioperl-ext
COPY --from=dceoy/vep:latest /usr/local/src/ensembl-xs /usr/local/src/ensembl-xs
COPY --from=dceoy/vep:latest /usr/local/src/ensembl-vep /usr/local/src/ensembl-vep
ADD https://bootstrap.pypa.io/get-pip.py /tmp/get-pip.py
ADD . /tmp/vcline

RUN set -e \
      && ln -sf bash /bin/sh

RUN set -e \
      && apt-get -y update \
      && apt-get -y dist-upgrade \
      && apt-get -y install --no-install-recommends --no-install-suggests \
        cpanminus g++ gcc git libbz2-dev libcurl4-gnutls-dev libgsl-dev \
        libperl-dev liblzma-dev libmysqlclient-dev libncurses5-dev libpng-dev \
        libssl-dev libxml-dom-xpath-perl libxml-parser-perl libxml2 libz-dev \
        make perl pkg-config unzip \
      && apt-get -y autoremove \
      && apt-get clean \
      && rm -rf /var/lib/apt/lists/*

ENV PATH /opt/gatk/bin:/opt/conda/envs/gatk/bin:/opt/conda/bin:${PATH}

RUN set -e \
      && source /opt/gatk/gatkenv.rc \
      && /opt/conda/bin/conda update -n base -c defaults conda \
      && source deactivate \
      && /opt/conda/bin/python3 /tmp/get-pip.py \
      && /opt/conda/bin/python3 -m pip install -U --no-cache-dir \
        cython pip setuptools==57.5.0 \
      && /opt/conda/bin/python3 -m pip install -U --no-cache-dir \
        cnvkit cutadapt https://github.com/dceoy/ftarc/archive/main.tar.gz \
        https://github.com/dceoy/vanqc/archive/main.tar.gz /tmp/vcline \
      && echo >> /opt/gatk/gatkcondaenv.yml \
      && echo -e '# CNVkit' >> /opt/gatk/gatkcondaenv.yml \
      && echo -e '- bioconductor-dnacopy' >> /opt/gatk/gatkcondaenv.yml \
      && /opt/conda/bin/conda env update -n gatk -f /opt/gatk/gatkcondaenv.yml \
      && /opt/conda/bin/conda clean -yaf \
      && find /opt/conda -follow -type f -name '*.a' -delete \
      && find /opt/conda -follow -type f -name '*.pyc' -delete \
      && rm -rf /root/.cache/pip /tmp/get-pip.py

RUN set -e \
      && cd /usr/local/src/bwa \
      && make clean \
      && make \
      && cd /usr/local/src/samtools/htslib-* \
      && make clean \
      && ./configure \
      && make \
      && make install \
      && cd /usr/local/src/samtools \
      && make clean \
      && ./configure \
      && make \
      && make install \
      && cd /usr/local/src/bcftools/htslib-* \
      && make clean \
      && ./configure \
      && make \
      && cd /usr/local/src/bcftools \
      && make clean \
      && ./configure --enable-libgsl --enable-perl-filters \
      && make \
      && make install \
      && cd /usr/local/src/bedtools2 \
      && make clean \
      && make \
      && make install \
      && find \
        /usr/local/src/bwa /usr/local/src/bwa-mem2 /usr/local/src/FastQC \
        /usr/local/src/TrimGalore -maxdepth 1 -type f -executable \
        -exec ln -s {} /usr/local/bin \;

RUN set -e \
      && cd /usr/local/src/kent/src/lib \
      && make clean \
      && export KENT_SRC=/usr/local/src/kent/src \
      && export MACHTYPE=$(uname -m) \
      && export CFLAGS='-fPIC' \
      && export MYSQLINC=`mysql_config --include | sed -e 's/^-I//g'` \
      && export MYSQLLIBS=`mysql_config --libs` \
      && echo 'CFLAGS="-fPIC"' > ../inc/localEnvironment.mk \
      && make \
      && cd ../jkOwnLib \
      && make clean \
      && make \
      && cpanm Bio::DB::BigFile Test::Warnings \
      && cd /usr/local/src/bioperl-ext/Bio/Ext/Align \
      && make clean \
      && perl -pi -e "s|(cd libs.+)CFLAGS=\\\'|\$1CFLAGS=\\\'-fPIC |" \
        Makefile.PL \
      && perl Makefile.PL \
      && make \
      && make install \
      && cd /usr/local/src/ensembl-xs \
      && make clean \
      && cpanm --installdeps --with-recommends . \
      && perl Makefile.PL \
      && make \
      && make install \
      && cd /usr/local/src/ensembl-vep \
      && cpanm --installdeps --with-recommends . \
      && cpanm Bio::DB::HTS::Tabix \
      && yes | perl INSTALL.pl --AUTO a \
      && find \
        /usr/local/src/ensembl-vep -maxdepth 1 -type f -executable \
        -exec ln -s {} /usr/local/bin \;

FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

COPY --from=builder /usr/local /usr/local
COPY --from=builder /opt /opt

RUN set -e \
      && ln -sf bash /bin/sh \
      && echo '. /opt/conda/etc/profile.d/conda.sh' >> /etc/profile \
      && echo 'source activate gatk' >> /etc/profile \
      && echo 'source /opt/gatk/gatk-completion.sh' >> /etc/profile

RUN set -e \
      && apt-get -y update \
      && apt-get -y dist-upgrade \
      && apt-get -y install --no-install-recommends --no-install-suggests \
        apt-transport-https apt-utils ca-certificates curl gnupg gnuplot \
        libcurl3-gnutls libgsl23 libgkl-jni libncurses5 libmysqlclient21 \
        libxml-dom-xpath-perl libxml-parser-perl openjdk-8-jre pbzip2 perl \
        pigz python texlive-fonts-extra texlive-fonts-recommended \
        texlive-latex-base texlive-latex-extra wget

RUN set -eo pipefail \
      && echo 'deb http://packages.cloud.google.com/apt cloud-sdk-bionic main' \
        | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
      && curl https://packages.cloud.google.com/apt/doc/apt-key.gpg \
        | apt-key add - \
      && apt-get -y update \
      && apt-get -y install --no-install-recommends --no-install-suggests \
        google-cloud-sdk \
      && apt-get -y autoremove \
      && apt-get clean \
      && rm -rf /var/lib/apt/lists/*

RUN set -eo pipefail \
      && unlink /usr/lib/ssl/openssl.cnf \
      && echo -e 'openssl_conf = default_conf' > /usr/lib/ssl/openssl.cnf \
      && echo >> /usr/lib/ssl/openssl.cnf \
      && cat /etc/ssl/openssl.cnf >> /usr/lib/ssl/openssl.cnf \
      && echo >> /usr/lib/ssl/openssl.cnf \
      && echo -e '[default_conf]' >> /usr/lib/ssl/openssl.cnf \
      && echo -e 'ssl_conf = ssl_sect' >> /usr/lib/ssl/openssl.cnf \
      && echo >> /usr/lib/ssl/openssl.cnf \
      && echo -e '[ssl_sect]' >> /usr/lib/ssl/openssl.cnf \
      && echo -e 'system_default = system_default_sect' >> /usr/lib/ssl/openssl.cnf \
      && echo >> /usr/lib/ssl/openssl.cnf \
      && echo -e '[system_default_sect]' >> /usr/lib/ssl/openssl.cnf \
      && echo -e 'MinProtocol = TLSv1.2' >> /usr/lib/ssl/openssl.cnf \
      && echo -e 'CipherString = DEFAULT:@SECLEVEL=1' >> /usr/lib/ssl/openssl.cnf

ENV JAVA_LIBRARY_PATH /usr/lib/jni
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
ENV CLASSPATH /opt/gatk/gatk.jar:${CLASSPATH}
ENV BCFTOOLS_PLUGINS /usr/local/src/bcftools/plugins
ENV PYTHONPATH /opt/manta/lib/python:/opt/strelka/lib/python:${PYTHONPATH}
ENV PATH /opt/gatk/bin:/opt/conda/envs/gatk/bin:/opt/conda/bin:/opt/manta/bin:/opt/strelka/bin:/opt/snpEff/bin:${PATH}
ENV MPLCONFIGDIR /tmp/cnvkit

ENTRYPOINT ["/opt/conda/bin/vcline"]
