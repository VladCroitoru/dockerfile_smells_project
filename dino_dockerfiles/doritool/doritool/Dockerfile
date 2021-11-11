FROM willmclaren/ensembl-vep

LABEL	description="Doritool container image" vendor="CNIO" maintainer="Miguel Madrid Mencía <miguel.madrid-mencia@inserm.fr>"

# https://github.com/Ensembl/ensembl-vep/blob/release/88/docker/Dockerfile
# https://hub.docker.com/r/willmclaren/ensembl-vep/
# https://github.com/rocker-org/rocker/blob/master/r-base/Dockerfile
# https://hub.docker.com/_/r-base/

USER root

# Minimun packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    ed less	locales wget ca-certificates fonts-texgyre \
    libcurl4-gnutls-dev libxml2-dev

# Config locale
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
	&& locale-gen en_US.utf8 \
	&& /usr/sbin/update-locale LANG=en_US.UTF-8
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

# Install R and BioConductor packages
RUN echo "deb http://cran.rstudio.com/bin/linux/ubuntu xenial/" | tee -a /etc/apt/sources.list
RUN gpg --keyserver keyserver.ubuntu.com --recv-key E084DAB9 && \
    gpg -a --export E084DAB9 | apt-key add -
RUN apt-get update && apt-get install -y --no-install-recommends \
      littler \
      r-cran-littler \
      r-base \
      r-base-dev \
      r-recommended
RUN  echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"), download.file.method = "libcurl")' >> /etc/R/Rprofile.site \
      && echo 'source("/etc/R/Rprofile.site")' >> /etc/littler.r \
      && ln -s /usr/share/doc/littler/examples/install.r /usr/local/bin/install.r \
      && ln -s /usr/share/doc/littler/examples/install2.r /usr/local/bin/install2.r \
      && ln -s /usr/share/doc/littler/examples/installGithub.r /usr/local/bin/installGithub.r \
      && ln -s /usr/share/doc/littler/examples/testInstalled.r /usr/local/bin/testInstalled.r \
      && install.r docopt \
      && rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
      && rm -rf /var/lib/apt/lists/*
RUN   echo 'install.packages(c("RCurl", "XML", "gProfileR"), repos="http://cran.us.r-project.org", dependencies=TRUE)' > /tmp/packages.R \
      && echo 'source("https://bioconductor.org/biocLite.R")' >> /tmp/packages.R \
      && echo 'biocLite(c("org.Hs.eg.db","FGNet","AnnotationDbi","topGO"))' >> /tmp/packages.R
      # && echo 'biocLite(c("org.Hs.eg.db","FGNet","AnnotationDbi","topGO","KEGGprofile"))' >> /tmp/packages.R \
RUN   echo 'install.packages("devtools");library(devtools);dev_mode(on=F)' >> /tmp/packages.R
RUN   echo 'install_github("mimadrid/KEGGprofile")' >> /tmp/packages.R \
      && Rscript /tmp/packages.R \
      && rm -rf /tmp/*/downloaded_packages/ /tmp/packages.R \
      && rm -rf /var/lib/apt/lists/*

#RUN cd ${HOME} && git clone https://github.com/doritool/doritool.git
RUN mkdir -p /opt/doritool
COPY . /opt/doritool
RUN chmod +x /opt/doritool/code/DoriTool.sh
ENV PATH="/opt/doritool/code:${PATH}"


ENV HOME="/home/vep"

RUN mkdir -p $HOME && chmod 777 $HOME && chown vep vep $HOME

USER vep

RUN cd /tmp/ && git clone https://github.com/Ensembl/VEP_plugins.git && \
    mkdir -p ${HOME}/.vep/Plugins/config/ && \
    cp -r VEP_plugins/* ${HOME}/.vep/Plugins/



WORKDIR ${HOME}/doritool

ENTRYPOINT ["DoriTool.sh"]

