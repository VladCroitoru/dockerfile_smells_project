FROM buildpack-deps:jessie
MAINTAINER Lionel Roche
ARG reposurgeonversion=3.42
RUN mkdir -p work

WORKDIR work 

RUN mkdir -p /usr/local/src/reposurgeon/ \
    && cd /usr/local/src/reposurgeon/ \
    && wget http://www.catb.org/~esr/reposurgeon/reposurgeon-$reposurgeonversion.tar.xz \
    && tar -xvf reposurgeon-$reposurgeonversion.tar.xz 
   

RUN apt-get update && \
  DEBIAN_FRONTEND=noninteractive apt-get install -yq \
    rsync

RUN bash /usr/local/src/reposurgeon/reposurgeon-$reposurgeonversion/ci/prepare.sh
# Package needed by hg-fastimport:
RUN pip install fastimport
RUN hg clone https://bitbucket.org/gward/hg-fastimport/ hg-fastimport
# Install mercurial extension 
RUN echo '[extensions]\nfastimport=/work/hg-fastimport/hgfastimport' >> /etc/mercurial/hgrc

RUN cd /usr/local/src/reposurgeon/reposurgeon-$reposurgeonversion && make install

RUN cd /work
COPY cvs2hg.sh .
RUN chmod +x cvs2hg.sh

ENTRYPOINT ["/work/cvs2hg.sh"]

