#
# jbliesener/sphinx-doc-portuguese
#
# A Docker image for the Sphinx documentation builder (http://sphinx-doc.org).
#
# docker build -t jbliesener/sphinx-doc-portuguese .

FROM       python:2.7.13
MAINTAINER Jorg Neves Bliesener

RUN export DEBIAN_FRONTEND=noninteractive \
 && echo "deb     http://httpredir.debian.org/debian jessie contrib non-free"   >> /etc/apt/sources.list \
 && echo "deb-src http://httpredir.debian.org/debian jessie contrib non-free"   >> /etc/apt/sources.list \
 && echo "deb     http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >> /etc/apt/sources.list.d/webupd8team-java.list \
 && echo "deb-src http://ppa.launchpad.net/webupd8team/java/ubuntu trusty main" >> /etc/apt/sources.list.d/webupd8team-java.list \
 && echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections \
 && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 7B2C3B0889BF5709A105D03AC2518248EEA14886 \
 && apt-get update

RUN apt-get install -y --no-install-recommends dvipng graphviz oracle-java8-installer sudo texlive texlive-lang-french texlive-latex-extra

RUN gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
 && curl -o /usr/local/bin/gosu     -SL "https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-architecture)" \
 && curl -o /usr/local/bin/gosu.asc -SL "https://github.com/tianon/gosu/releases/download/1.10/gosu-$(dpkg --print-architecture).asc" \
 && gpg --verify /usr/local/bin/gosu.asc \
 && rm /usr/local/bin/gosu.asc \
 && chmod +x /usr/local/bin/gosu \
 && apt-get autoremove -y

RUN apt-get upgrade -y
RUN apt-get install -y texlive-lang-portuguese latexmk

RUN rm -rf /var/cache/* \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
 && pip install 'Sphinx                        == 1.6.2'  \
                'alabaster                     == 0.7.10' \
                'recommonmark                  == 0.4.0'  \
                'sphinx-autobuild              == 0.6.0'  \
                'sphinx-bootstrap-theme        == 0.5.3'  \
                'sphinx-prompt                 == 1.0.0'  \
                'sphinx_rtd_theme              == 0.2.4'  \
                'sphinxcontrib-actdiag         == 0.8.5'  \
                'sphinxcontrib-blockdiag       == 1.5.5'  \
                'sphinxcontrib-exceltable      == 0.2.2'  \
                'sphinxcontrib-googleanalytics == 0.1'    \
                'sphinxcontrib-googlechart     == 0.2.1'  \
                'sphinxcontrib-googlemaps      == 0.1.0'  \
                'sphinxcontrib-nwdiag          == 0.9.5'  \
                'sphinxcontrib-plantuml        == 0.8.1'  \
                'sphinxcontrib-seqdiag         == 0.8.5'  \
                'livereload                    == 2.5.1'

# RUN pip install sphinxcontrib-libreoffice == 0.2  # doesn't work

COPY files/opt/plantuml/*  /opt/plantuml/
COPY files/usr/local/bin/* /usr/local/bin/

RUN chown root:root /usr/local/bin/* \
 && chmod 755 /usr/local/bin/*

ENV DATA_DIR=/doc \
    JAVA_HOME=/usr/lib/jvm/java-8-oracle

WORKDIR $DATA_DIR

ENTRYPOINT ["/usr/local/bin/docker-entrypoint"]
