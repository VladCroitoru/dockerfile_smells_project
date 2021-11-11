FROM linuxbrew/linuxbrew:1.5.1

USER root 
# Install latest version of R

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        make \
        build-essential \
        libssl-dev \
        zlib1g-dev \
        libbz2-dev \
        libreadline-dev \
        libsqlite3-dev \
        wget \
        curl \
        llvm \
        libncurses5-dev \
        libncursesw5-dev \
        xz-utils \
        tk-dev \
        ed \
        less \
        locales \
        vim-tiny \
        ca-certificates \
        fonts-texgyre \
        libxml2-dev \
        libcairo2-dev \
        libsqlite-dev \
        libmariadbd-dev \
        libmariadb-client-lgpl-dev \
        libpq-dev \
        libssh2-1-dev \
        libcurl4-openssl-dev \
    && rm -rf /var/lib/apt/lists/*

## Configure default locale, see https://github.com/rocker-org/rocker/issues/19
RUN echo "en_US.UTF-8 UTF-8" >> /etc/locale.gen \
    && locale-gen en_US.utf8 \
    && /usr/sbin/update-locale LANG=en_US.UTF-8

ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8

## Use Debian unstable via pinning -- new style via APT::Default-Release
RUN echo "deb http://http.debian.net/debian sid main" > /etc/apt/sources.list.d/debian-unstable.list \
    && echo 'APT::Default-Release "testing";' > /etc/apt/apt.conf.d/default

ENV R_BASE_VERSION 3.4.3

## Now install R and littler, and create a link for littler in /usr/local/bin
## Also set a default CRAN repo, and make sure littler knows about it too
RUN apt-get update \
    && apt-get install -t unstable -y --no-install-recommends --allow-unauthenticated \
        littler \
                r-cran-littler \
        r-base=${R_BASE_VERSION}* \
        r-base-dev=${R_BASE_VERSION}* \
        r-recommended=${R_BASE_VERSION}* \
        && echo 'options(repos = c(CRAN = "https://cran.rstudio.com/"), download.file.method = "libcurl")' >> /etc/R/Rprofile.site \
        && echo 'source("/etc/R/Rprofile.site")' >> /etc/littler.r \
    && ln -s /usr/share/doc/littler/examples/install.r /usr/local/bin/install.r \
    && ln -s /usr/share/doc/littler/examples/install2.r /usr/local/bin/install2.r \
    && ln -s /usr/share/doc/littler/examples/installGithub.r /usr/local/bin/installGithub.r \
    && ln -s /usr/share/doc/littler/examples/testInstalled.r /usr/local/bin/testInstalled.r \
    && install.r docopt \
    && rm -rf /tmp/downloaded_packages/ /tmp/*.rds \
    && rm -rf /var/lib/apt/lists/*

USER linuxbrew
# Install homebrew files
RUN brew install gcc \
    && brew install https://raw.githubusercontent.com/Linuxbrew/homebrew-core/043fb1f50af078db481b971d36c605f0dcf72ccd/Formula/jdk.rb \
    && brew tap brewsci/science \
    && brew tap brewsci/bio \
    && brew install \
            bwa \
            samtools \
            bcftools \
            gsl \
            bedtools \
            nextflow \
            sambamba \
            vcflib \
            vcftools \
            picard-tools \
            pigz \
            parallel \
            snpeff \
            muscle \
            vcfanno \
            igvtools \
            bamtools \
            trimmomatic \
            pyenv \
            pyenv-virtualenv \
            primer3

RUN brew install fastqc --ignore-dependencies

# Take over the R lib
RUN sudo chown -R linuxbrew:linuxbrew /usr/local/
ENV R_LIBS_USER=/usr/local/lib/R/site-library
# Install R packages and link python
RUN echo "r <- getOption('repos'); r['CRAN'] <- 'http://cran.us.r-project.org'; options(repos = r);" > ~/.Rprofile \
    && Rscript -e 'install.packages(c("memoise", "tidyverse", "cowplot", "ggmap", "ape", "devtools", "knitr", "rmarkdown", "aws.s3", "genetics"))'
RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite(c("phyloseq"))'
RUN Rscript -e 'devtools::install_github("andersenlab/cegwas")'

# Install telseq
RUN wget -O /home/linuxbrew/.linuxbrew/bin/telseq https://github.com/zd1/telseq/raw/master/bin/ubuntu/telseq  \
    && chmod +x /home/linuxbrew/.linuxbrew/bin/telseq

ADD setup_pyenv.sh setup_pyenv.sh
RUN bash setup_pyenv.sh

ENV PYENV_ROOT /usr/local/var/pyenv
ADD bin/init_pyenv.sh /home/linuxbrew/.bashrc
