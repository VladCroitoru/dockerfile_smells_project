FROM stackbrew/ubuntu:14.04
MAINTAINER Changbum Hong hongiiv@gmail.com

# Setup a base system
RUN apt-get update && apt-get install -y build-essential zlib1g-dev wget curl python-setuptools git
RUN apt-get install -y openjdk-7-jdk openjdk-7-jre ruby libncurses5-dev libcurl4-openssl-dev libbz2-dev \
    unzip pigz bsdmainutils

# Fake a fuse install; openjdk pulls this in
# https://github.com/dotcloud/docker/issues/514
# https://gist.github.com/henrik-muehe/6155333
RUN mkdir -p /tmp/fuse-hack && cd /tmp/fuse-hack && \
    apt-get install libfuse2 && \
    apt-get download fuse && \
    dpkg-deb -x fuse_* . && \
    dpkg-deb -e fuse_* && \
    rm fuse_*.deb && \
    echo -en '#!/bin/bash\nexit 0\n' > DEBIAN/postinst && \
    dpkg-deb -b . /fuse.deb && \
    dpkg -i /fuse.deb && \
    rm -rf /tmp/fuse-hack

# bcbio-nextgen install (Automated)
RUN mkdir -p /tmp/bcbio-nextgen-install && cd /tmp/bcbio-nextgen-install && \
    wget --no-check-certificate \
      https://raw.githubusercontent.com/hongiiv/ngspipeline/master/bcbio_nextgen_install.py && \
    python bcbio_nextgen_install.py /usr/local/share/bcbio --nodata
RUN /usr/local/share/bcbio/anaconda/bin/bcbio_nextgen.py upgrade --sudo --tooldir=/usr/local --tools
RUN wget --no-check-certificat https://ssproxy.ucloudbiz.olleh.com/v1/AUTH_f1b97694-00cd-4e06-b9f3-30a0f9d01f66/bcbio/toolplus.tar.gz && \
    tar xvfz toolplus.tar.gz && \
    /usr/local/share/bcbio/anaconda/bin/bcbio_nextgen.py upgrade --tools \
    --toolplus gatk=./toolplus/gatk/3.2-2-gec30cee/GenomeAnalysisTK.jar \
    --toolplus mutect=./toolplus/mutect/1.1.7/muTect-1.1.7.jar

ENV PATH /usr/local/bin:/usr/local/share/bcbio-nextgen/anaconda/bin:${PATH}
ENV LD_LIBRARY_PATH /usr/local/lib:${LD_LIBRARY_PATH}
ENV PERL5LIB /usr/local/lib/perl5:/usr/local/lib/perl5/site_perl:${PERL5LIB}

RUN echo 'export PATH=/usr/local/bin:$PATH' >> /etc/profile.d/bcbio.sh && \
    echo 'export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH' >> /etc/profile.d/bcbio.sh && \
    echo 'export PERL5LIB=/usr/local/lib/perl5:/usr/local/lib/perl5/site_perl:${PERL5LIB}' >> /etc/profile.d/bcbio.sh && \
    echo '/usr/local/lib' >> /etc/ld.so.conf.d/bcbio.conf && ldconfig && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /var/tmp/* && \
    /usr/local/share/bcbio/anaconda/bin/conda remove --yes qt && \
    /usr/local/share/bcbio/anaconda/bin/conda clean --yes --tarballs && \
    rm -rf /usr/local/share/bcbio-nextgen/anaconda/pkgs/qt* && \
    rm -rf $(brew --cache) && \
    rm -rf /.cpanm && \
    rm -rf /tmp/bcbio-nextgen-install
RUN mkdir -p /bio/ && \
    mkdir -p /tmp/bcbio-nextgen && \
    mv /usr/local/share/bcbio/galaxy/bcbio_system.yaml /usr/local/share/bcbio/config && \
    ln -s /bio/galaxy /usr/local/share/bcbio/galaxy && \
    ln -s /bio/genomes /usr/local/share/bcbio/genomes && \
    chmod a+rwx /usr/local/share/bcbio && \
    chmod a+rwx /usr/local/share/bcbio/config && \
    chmod a+rwx /usr/local/share/bcbio/config/*.yaml
