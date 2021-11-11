FROM centos:6
MAINTAINER NASU,Tatsuya <tatu.nasu@gmail.com>
# env
ENV HOME /root
ENV SHELL /bin/bash
ENV PERLVERSION 5.16.3

# yum
RUN yum -y -q update
RUN yum -y -q install perl
RUN yum -y -q install tar bzip2
RUN yum -y -q install gcc
RUN yum -y -q install man
RUN yum clean all

# perlbrew
ENV PERLBREW_ROOT ${HOME}/perl5/perlbrew
ENV PERLBREW_HOME ${HOME}/.perlbrew
ENV PERLBREW_PATH ${HOME}/perl5/perlbrew/bin
RUN curl -L http://install.perlbrew.pl | bash
ENV PATH ${HOME}/bin:${PERLBREW_PATH}:${PATH}
RUN perlbrew install --notest ${PERLVERSION}

# perl alias
RUN mkdir -p ${HOME}/bin
RUN echo "source ${PERLBREW_ROOT}/etc/bashrc &&\
    perlbrew use ${PERLVERSION} &&\
    perl \$@\
    " > ${HOME}/bin/perl
RUN chmod +x ${HOME}/bin/perl
RUN echo "source ${PERLBREW_ROOT}/etc/bashrc &&\
    perlbrew use ${PERLVERSION} &&\
    cpanm \$@\
    " > ${HOME}/bin/cpanm
RUN chmod +x ${HOME}/bin/cpanm
RUN echo "source ${PERLBREW_ROOT}/etc/bashrc &&\
    perlbrew use ${PERLVERSION} &&\
    perlbrew \$@\
    " > ${HOME}/bin/perlbrew
RUN chmod +x ${HOME}/bin/cpanm

# cpanm
RUN perlbrew install-cpanm
RUN cpanm -nq Carton
RUN cpanm -nq Plack
RUN echo "source ${PERLBREW_ROOT}/etc/bashrc &&\
    perlbrew use ${PERLVERSION} &&\
    carton \$@\
    " > ${HOME}/bin/carton
RUN chmod +x ${HOME}/bin/carton
RUN echo "source ${PERLBREW_ROOT}/etc/bashrc &&\
    perlbrew use ${PERLVERSION} &&\
    plackup \$@\
    " > ${HOME}/bin/plackup
RUN chmod +x ${HOME}/bin/plackup
CMD perl -v; plackup -v
