from comics/augustus:3.2.2

LABEL maintainer "erik.kastman@gmail.com"

ENV APP_NAME=busco
ARG BUSCO_VERSION=3.0.0
ENV BUSCO_VERSION_SHORTHASH=2f3dd7b4
ENV APP_PATH=/software/applications
ENV DEST=$APP_PATH/$APP_NAME/
ENV PATH=$DEST/$BUSCO_VERSION/scripts:$PATH
ENV BLAST_VERSION=2.2.31
ENV AUGUSTUS_CONFIG_PATH=/software/augustus/3.2.2/config

RUN yum install -y \
  python \
  emboss \
  git \
  perl-Archive-Tar \
  perl-List-MoreUtils \
  perl-Digest-MD5 \
  && yum clean all;

RUN rpm -ivh ftp://ftp.ncbi.nlm.nih.gov/blast/executables/blast+/$BLAST_VERSION/ncbi-blast-${BLAST_VERSION}+-2.x86_64.rpm

RUN cd $APP_PATH; \
  wget http://eddylab.org/software/hmmer3/3.1b2/hmmer-3.1b2-linux-intel-x86_64.tar.gz && \
  tar -xzf hmmer-3.1b2-linux-intel-x86_64.tar.gz && \
  rm hmmer-3.1b2-linux-intel-x86_64.tar.gz

# n.b. Downloading with Git is *not* preferred by Docker developers,
# but BUSCO distributes using gitlab which does not provide automatic zips
# of tags, so this seems to be the cleanest way to grab versions from upstream.
RUN git clone https://gitlab.com/ezlab/busco.git $DEST/$BUSCO_VERSION && \
  cd $DEST/$BUSCO_VERSION && \
  git checkout $BUSCO_VERSION_SHORTHASH && \
  python setup.py install

WORKDIR $DEST/$BUSCO_VERSION

COPY config.ini $DEST/$BUSCO_VERSION/config

ENTRYPOINT ["/software/applications/busco/3.0.0/scripts/run_BUSCO.py"]
CMD ["-h"]
