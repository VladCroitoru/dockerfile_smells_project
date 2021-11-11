FROM debian:stretch

LABEL org.label-schema.license="GPL-3.0" \
      org.label-schema.vcs-url="https://github.com/aminevsaziz/Container_For_Landslide_Susceptibility_Mapping_In_Mila_Basin" \
      org.label-schema.vendor="Merghadi Abdelaziz" \
      maintainer="Merghadi Abdelaziz <aminevsaziz@outlook.com>"

ARG RSTUDIO_VERSION

ENV R_VERSION=3.4.3 \
    LC_ALL=en_US.UTF-8 \
    LANG=en_US.UTF-8 \
    TERM=xterm \
    MRAN=https://mran.microsoft.com/snapshot/2018-03-15 \
    PANDOC_TEMPLATES_VERSION=1.18 \
    JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/jre \
    PATH=/usr/lib/rstudio-server/bin:$JAVA_HOME/bin:$PATH
## Install Dependencies
RUN COMPILEDEPS="build-essential \
                  bash-completion \
                  ca-certificates \
                  file \
                  fonts-texgyre \
                  g++ \
                  gfortran \
                  gsfonts \
                  libbz2-1.0 \
                  libcurl3 \
                  libicu57 \
                  libjpeg62-turbo \
                  libatlas-base-dev \
                  libopenblas-dev \
                  libpangocairo-1.0-0 \
                  libpcre3 \
                  libpng16-16 \
                  libreadline7 \
                  libtiff5 \
                  liblzma5 \
                  locales \
                  make \
                  autoconf \
                  automake \
                  cmake \
                  unzip \
                  zip \
                  zlib1g \
                  libssl-dev \
                  libxml2-dev \
                  cdbs \
                  pkg-config \
                  xauth " \
  ## fix missing/confilcted dependencies by Adding cloudfront repos ,official CDN gives frequent 503 errors
  && rm /etc/apt/sources.list \
  && sources="deb http://cloudfront.debian.net/debian stretch main contrib \ndeb http://cloudfront.debian.net/debian stretch-updates main contrib \ndeb http://cloudfront.debian.net/debian-security stretch/updates main contrib \ndeb http://cloud.r-project.org/bin/linux/debian stretch-cran34/" \
  && printf "$sources" >> /etc/apt/sources.list \
  && apt-get -q update \
  && apt-get -y install --no-install-recommends $COMPILEDEPS \
  ## Configure default locale
  && echo 'LC_ALL="'${LC_ALL}'"' >> /etc/environment \
  && echo 'LANG="'${LANG}'"' >> /etc/environment \
  && echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen \
  && locale-gen en_US.UTF-8 \
  && /usr/sbin/update-locale LANG=en_US.UTF-8 \
  ## list of devel dependencies that we need to ensure that all deps or this deps are installed for best performance
  && BUILDDEPS="curl \
  default-jdk \
  libbz2-dev \
  libcairo2-dev \
  libcurl4-openssl-dev \
  libpango1.0-dev \
  libjpeg-dev \
  libicu-dev \
  libpcre3-dev \
  libpng-dev \
  libreadline-dev \
  libtiff5-dev \
  liblzma-dev \
  libx11-dev \
  libxt-dev \
  perl \
  tcl8.6-dev \
  tk8.6-dev \
  ## Latex & documentations
  texinfo \
  texlive-extra-utils \
  texlive-fonts-recommended \
  texlive-fonts-extra \
  texlive-latex-recommended \
  x11proto-core-dev \
  xauth \
  xfonts-base \
  xvfb \
  zlib1g-dev" \
  && apt-get -q update \
  && apt-get -y install --no-install-recommends --fix-missing $BUILDDEPS \
  ## Set JAVA & JAVA_HOME
  && echo 'JAVA_HOME="'$JAVA_HOME'"' >> /etc/environment \
  && export PATH=$PATH \
  ## Download source code
  && cd /tmp/ \
  && curl -O https://cran.r-project.org/src/base/R-3/R-$R_VERSION.tar.gz \
  ## Extract source code
  && tar -xf R-$R_VERSION.tar.gz \
  && cd R-$R_VERSION \
  && mkdir Build && cd Build \
  ## Set compiler flags
  && ../configure R_PAPERSIZE=a4 \
                  R_BATCHSAVE="--no-save --no-restore" \
                  R_BROWSER=xdg-open \
                  PAGER=/usr/bin/pager \
                  PERL=/usr/bin/perl \
                  R_UNZIPCMD=/usr/bin/unzip \
                  R_ZIPCMD=/usr/bin/zip \
                  R_PRINTCMD=/usr/bin/lpr \
                  LIBnn=lib \
                  AWK=/usr/bin/awk \
                  CFLAGS="-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g" \
                  CXXFLAGS="-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g" \
                  CXX11FLAGS="-g -O2 -fstack-protector-strong -Wformat -Werror=format-security -Wdate-time -D_FORTIFY_SOURCE=2 -g" \
                  FFLAGS="-g -O2 -fstack-protector-strong" \
                  FCFLAGS="-g -O2 -fstack-protector-strong" \
                  --enable-R-shlib \
                  --enable-memory-profiling \
                  --with-readline \
                  --with-tcltk \
                  --disable-nls \
                  --with-blas \
                  --without-recommended-packages \
  ## make,check & install
  && make && make install \
  ## Add a library directory (for user-installed packages)
  && mkdir -p /usr/local/lib/R/site-library \
  && chown root:staff /usr/local/lib/R/site-library \
  && chmod g+wx /usr/local/lib/R/site-library \
  # Export Library location / MRAN Repo to environments so to be used sys wide by for example Littler
  && echo LIBLOC=/usr/local/lib/R/site-library >> /etc/environment && echo MRAN=$MRAN >> /etc/environment \
  ## Fix library path & Set Renviron.site/Renviron to get libs from base R install
  && echo "R_LIBS_USER='/usr/local/lib/R/site-library'" >> /usr/local/lib/R/etc/Renviron \
  && echo "R_LIBS=\${R_LIBS-'/usr/local/lib/R/site-library:/usr/local/lib/R/library:/usr/lib/R/library'}" >> /usr/local/lib/R/etc/Renviron \
  ## Add repos user profile
  && echo "options(repos = c(CRAN='"$MRAN"'), download.file.method = 'libcurl')" >> /usr/local/lib/R/etc/Rprofile.site \
  ## Use littler installation scripts
  && Rscript -e "install.packages(c('littler', 'docopt'), repo = '"$MRAN"')" \
  && ln -s /usr/local/lib/R/site-library/littler/examples/install2.r /usr/local/bin/install2.r \
  && ln -s /usr/local/lib/R/site-library/littler/examples/installGithub.r /usr/local/bin/installGithub.r \
  && ln -s /usr/local/lib/R/site-library/littler/bin/r /usr/local/bin/r \
  ## TEMPORARY WORKAROUND to get more robust error handling for install2.r prior to littler update
  && curl -O /usr/local/bin/install2.r https://github.com/eddelbuettel/littler/raw/master/inst/examples/install2.r \
  && chmod +x /usr/local/bin/install2.r \
  ## Clean up from R source install & remove installed libs used for compiling R source
  && cd / \
  && rm -rf /tmp/* \
  && apt-get remove --purge -y $BUILDDEPS \
  && apt-get autoremove -y \
  && apt-get autoclean -y \
  && rm -rf /var/lib/apt/lists/*

## Download and install RStudio server & dependencies
RUN cd /tmp/ \
  && Rstudio="libsqlite-dev \
    libmariadbd-dev \
    libmariadb-client-lgpl-dev \
    libcurl4-openssl-dev \
    libcairo2-dev \
    libxt-dev \
    libapparmor1 \
    lsb-release \
    psmisc \
    libedit2 \
    libxml2-dev \
    libssl-dev \
    libssh2-1-dev \
    ssh \
    python-setuptools \
    file \
    sudo \
    ## system dependency of nlopt
    libnlopt-dev \
    ## system dependency of hunspell(devtools)
    libhunspell-dev \
    ## Tools
    libpq-dev \
    ed \
    qpdf \
    less \
    vim-tiny \
    nano \
    wget \
    git \
    ## used by some base R plots
    ghostscript \
    libgs-dev \
    libmagick++-dev \
    imagemagick \
    ## for V8-based javascript wrappers
    libv8-dev " \
  ## used to build rJava
  && rjava="openjdk-8-jdk \
    libbz2-dev \
    libicu-dev \
    liblzma-dev " \
  ## Consider including Additional libraries for Mapping & Spatial packages
  && Spatial="libgdal-dev \
    libgeos-dev \
    libgsl0-dev \
    libhdf4-alt-dev \
    libhdf5-dev \
    libproj-dev \
    libnetcdf-dev " \
  && apt-get -q update \
  && apt-get -y install --no-install-recommends $COMPILEDEPS $Rstudio $rjava $Spatial \
  ## install missing stretch libssl1.0.0 from debian pool
  && wget -O libssl1.0.0.deb http://ftp.debian.org/debian/pool/main/o/openssl/libssl1.0.0_1.0.1t-1+deb8u7_amd64.deb \
  && dpkg -i libssl1.0.0.deb \
  && rm libssl1.0.0.deb \
  ## Attempts to get detect latest version, otherwise falls back to version given in $VER
  && RSTUDIO_LATEST=$(wget --no-check-certificate -qO- https://s3.amazonaws.com/rstudio-server/current.ver) \
  && [ -z "$RSTUDIO_VERSION" ] && RSTUDIO_VERSION=$RSTUDIO_LATEST || true \
  && wget -q http://download2.rstudio.org/rstudio-server-${RSTUDIO_VERSION}-amd64.deb \
  && dpkg -i rstudio-server-${RSTUDIO_VERSION}-amd64.deb \
  && rm rstudio-server-*-amd64.deb \
  ## Symlink pandoc & standard pandoc templates for use system-wide
  && ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc /usr/local/bin \
  && ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc-citeproc /usr/local/bin \
  && git clone https://github.com/jgm/pandoc-templates \
  && mkdir -p /opt/pandoc/templates \
  && cp -r pandoc-templates*/* /opt/pandoc/templates && rm -rf pandoc-templates* \
  && mkdir /root/.pandoc && ln -s /opt/pandoc/templates /root/.pandoc/templates \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/ \
  ## RStudio wants an /etc/R, will populate from $R_HOME/etc
  && mkdir -p /etc/R \
  ## Write config files in $R_HOME/etc
  && echo '\n\
    \n# Configure httr to perform out-of-band authentication if HTTR_LOCALHOST \
    \n# is not set since a redirect to localhost may not work depending upon \
    \n# where this Docker container is running. \
    \nif(is.na(Sys.getenv("HTTR_LOCALHOST", unset=NA))) { \
    \n  options(httr_oob_default = TRUE) \
    \n}' >> /usr/local/lib/R/etc/Rprofile.site \
  && echo "PATH=${PATH}" >> /usr/local/lib/R/etc/Renviron \
  ## Need to configure non-root user for RStudio
  && useradd rstudio \
  && echo "rstudio:rstudio" | chpasswd \
	  && mkdir /home/rstudio \
	  && chown rstudio:rstudio /home/rstudio \
    && addgroup rstudio staff \
    ## Prevent rstudio from deciding to use /usr/bin/R if a user apt-get installs a package
  && echo 'rsession-which-r=/usr/local/bin/R' >> /etc/rstudio/rserver.conf \
  ## configure git not to request password each time
  && git config --system credential.helper 'cache --timeout=3600' \
  && git config --system push.default simple \
  ## Set up S6 init system
  && wget -P /tmp/ https://github.com/just-containers/s6-overlay/releases/download/v1.11.0.1/s6-overlay-amd64.tar.gz \
  && tar xzf /tmp/s6-overlay-amd64.tar.gz -C / \
  && mkdir -p /etc/services.d/rstudio \
  && echo '#!/bin/bash \
           \n exec /usr/lib/rstudio-server/bin/rserver --server-daemonize 0' > /etc/services.d/rstudio/run \
   && echo '#!/bin/bash \
           \n rstudio-server stop' > /etc/services.d/rstudio/finish \
  ## Clean up
  && cd / \
  && rm -rf /tmp/* \
  && apt-get -f install \
  && apt-get -y autoclean \
  && apt-get -y clean \
  && apt-get -y autoremove \
  && rm -rf /var/lib/apt/lists/*

## Install The Required R Packages
RUN install2.r  --error  \
     tidyverse \
     RGraphics \
     ranger \
     randomForest \
     gbm \
     nnet \
     e1071 \
     kernlab \
     mda \
     DiceKriging \
     DiceOptim \
     mco \
     testthat \
     Hmisc \
     car \
     mlr \
     mlrMBO \
     ## for rmarkdown
     formatR \
     rfigshare \
     printr \
     rmarkdown \
     bitops \
     ## remotes included for installation from heterogenous sources including git/svn, local, url, and specific cran versions
     remotes \
     ## Color Palettes
     colormap \
     ## include useful tools
     setRNG \
     sp \
     raster \
     rgdal \
     packrat \
     ## Additional ggplot2 Extensions
     ggraptR \
     ggcorrplot \
     ggedit \
     ggiraph \
     ggrepel \
     ggQC \
     GGally \
     ggalt \
     ggthemes \
     animation \
 && Rscript -e 'remotes::install_github("dgrtwo/gganimate")' \
 ## remove all downloaded packages to reduce image size
 && rm -rf /tmp/*

COPY userconf.sh /etc/cont-init.d/userconf
## running with "-e ADD=shiny" adds shiny server
COPY add_shiny.sh /etc/cont-init.d/add

EXPOSE 8787
## automatically link a shared volume for kitematic users
VOLUME /home/rstudio/kitematic

CMD ["/init"]

# ----------------------
# Get project scripts
# ----------------------
 RUN cd /home/rstudio \
     && git clone https://github.com/aminevsaziz/lsm_in_Mila_basin.git \
 && chown -R rstudio:rstudio lsm_in_Mila_basin

 # ----------
 # Notes
 # ----------
 # Nothing Yet!!
