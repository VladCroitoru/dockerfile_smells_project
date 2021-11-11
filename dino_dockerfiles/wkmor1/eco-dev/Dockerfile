FROM ubuntu:bionic
MAINTAINER William K Morris <>

# Install Ubuntu packages
ENV    DEBIAN_FRONTEND noninteractive
RUN    apt-get update \
    && apt-get install -y --no-install-recommends \
         apt-transport-https \
         curl \
         cmake \
         openjdk-8-jdk \
         fonts-texgyre \
         fonts-droid-fallback \
         g++-multilib \
         gdal-bin \
         gdebi-core \
         gfortran \
         ghostscript \
         git \
         gnupg \
         iputils-ping \
         jags \
         libavcodec-extra \
         libavdevice-dev \
         libavfilter-dev \
         libboost-filesystem-dev \
         libboost-program-options-dev \
         libboost-thread-dev \
         libbz2-dev \
         libcurl4-openssl-dev \
         libfftw3-dev \
         libfribidi-dev \
         libgdal-dev \
         libharfbuzz-dev \
         libicu-dev \
         liblzma5 \
         libmagick++-dev \
         libopenblas-dev \
         libpango1.0-dev \
         libpgf-dev \
         libpoppler-cpp-dev \
         libpcre2-dev \
         libproj-dev \
         libqt4-dev \
         libreadline-dev \
         librsvg2-dev \
         libssl-dev \
         libtiff5-dev \
         libudunits2-dev \
         libv8-dev \
         libzmq3-dev \
         locales \
         lmodern \
         pdf2svg \
         python-gdal \
         python3-dev \
         python3-gdal \
         python3-pip \
         python3-setuptools \
         qpdf \
         subversion \
         sudo \
         supervisor \
         tk8.6-dev \
         texinfo \
         texlive \
         texlive-bibtex-extra \
         texlive-extra-utils \
         texlive-fonts-extra \
         texlive-humanities \
         texlive-latex-extra \ 
         unzip \
         wget \
         xfonts-base \
         xvfb \
         zip \
    && apt-get install -y --no-install-recommends \
         libgit2-dev \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf var/lib/apt/lists/*

# Set paths and locale
ENV PATH            /opt/julia:/usr/lib/rstudio-server/bin:/build/zig4:$PATH
ENV LANG            en_US.UTF-8
ENV LANGUAGE        $LANG
RUN    echo "en_US "$LANG" UTF-8" >> /etc/locale.gen \
    && locale-gen en_US $LANG \
    && update-locale LANG=$LANG LANGUAGE=$LANG

# Download R, Rstudio, Julia, Inconsolata and OpenBUGS
RUN    RVER=$(curl https://cran.r-project.org/banner.shtml | grep src/base | egrep -o '[0-9]+(\.[0-9]+)+' | head -1) \
    && JULIAVER=$(curl https://api.github.com/repos/JuliaLang/julia/releases/latest | grep tag_name | cut -d \" -f4 | sed 's/v//g') \
    && JULIAMAJOR=$(echo $JULIAVER | cut -c -3) \
    && curl \
         -o r-source.tar.gz https://cran.r-project.org/src/base/R-4/R-$RVER.tar.gz \
         -OL https://www.rstudio.org/download/latest/stable/server/bionic/rstudio-server-latest-amd64.deb \
         -o julia.tar.gz https://julialang-s3.julialang.org/bin/linux/x64/$JULIAMAJOR/julia-$JULIAVER-linux-x86_64.tar.gz \ 
         -OL http://mirrors.ctan.org/install/fonts/inconsolata.tds.zip \
         -o OpenBUGS-3.2.3.tar.gz -L https://github.com/jsta/openbugs/archive/3.2.3.tar.gz

# Install Zonation
RUN    git clone https://github.com/cbig/zonation-core \
    && mkdir build \
    && cd build \
    && cmake ../zonation-core \
    && make \
    && cd .. \
    && rm -rf zonation-core

# Install TensorFlow
RUN    pip3 install --upgrade pip \
    && /usr/local/bin/pip3 install tensorflow tensorflow-probability --ignore-installed six
    
# Install Julia
RUN    mkdir -p /opt/julia \
    && tar xzf julia.tar.gz -C /opt/julia --strip 1 \
    && ln -s /opt/julia/bin/julia /usr/local/bin/julia \
    && rm -rf julia.tar.gz

# Install R
RUN    mkdir -p r-source \ 
    && tar xzf r-source.tar.gz -C r-source --strip 1 \
    && cd r-source \
    && R_PAPERSIZE=letter \
       R_BATCHSAVE="--no-save --no-restore" \
       R_BROWSER=xdg-open \
       PAGER=/usr/bin/pager \
       PERL=/usr/bin/perl \
       R_UNZIPCMD=/usr/bin/unzip \
       R_ZIPCMD=/usr/bin/zip \
       R_PRINTCMD=/usr/bin/lpr \
       LIBnn=lib \
       AWK=/usr/bin/awk \
       CFLAGS="-g -O2 -fstack-protector -Wformat -Werror=format-security -D_FORTIFY_SOURCE=2 -g" \
       CXXFLAGS="-g -O2 -fstack-protector -Wformat -Werror=format-security -D_FORTIFY_SOURCE=2 -g" \
       ./configure --enable-R-shlib \
                   --enable-memory-profiling \
                   --with-readline \
                   --with-blas="-lopenblas" \
                   --with-tcltk \
                   --disable-nls \
    && make \
    && make install \
    && cd / \
    && unset R_HOME \
    && rm r-source.tar.gz \
    && rm -rf r-source

# Install RStudio, rJava, devtools and openblasctl
ENV R_LIBS_USER ~/.r-dir/R/library
RUN    apt-get update \
    && gdebi -n rstudio-server-latest-amd64.deb \
    && echo 'NOT_CRAN=true' >> /usr/local/lib/R/etc/Renviron.site \
    && echo 'options(repos = c(CRAN = "https://cloud.r-project.org/"), download.file.method = "libcurl")' >> /usr/local/lib/R/etc/Rprofile.site \
    && R -e 'install.packages(c("rJava", "devtools", "dismo", "blogdown"))' \
    && R -e 'devtools::install_github("wrathematics/openblasctl")' \
    && R -e 'blogdown::install_hugo()' \
    && echo 'openblasctl::openblas_set_num_threads(1)' >> /usr/local/lib/R/etc/Rprofile.site \
    && echo r-libs-user=$R_LIBS_USER >> /etc/rstudio/rsession.conf \
    && ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc /usr/local/bin \
    && ln -s /usr/lib/rstudio-server/bin/pandoc/pandoc-citeproc /usr/local/bin \
    && apt-get clean \
    && apt-get autoremove \
    && rm -rf var/lib/apt/lists/* rstudio-server-latest-amd64.deb

# Install Maxent
RUN    git clone https://github.com/mrmaxent/Maxent.git \
    && cd Maxent \
    && sed -i 's/float/double/g' density/Extractor.java \
    && make distribution \
    && cp maxent.jar /usr/local/lib/R/library/dismo/java/maxent.jar \
    && cd .. \
    && rm -rf Maxent
    
# Install OpenBUGS
RUN    mkdir -p openbugs \
    && tar xzf OpenBUGS-3.2.3.tar.gz -C openbugs --strip 1 \
    && cd openbugs \
    && ./configure \
    && make \
    && make install \
    && cd / \
    && rm OpenBUGS-3.2.3.tar.gz \
    && rm -rf openbugs

# Copy scripts
COPY   supervisord.conf /etc/supervisor/conf.d/
COPY   userconf.sh /usr/bin/

# Config
RUN    mkdir -p /var/log/supervisor /var/run/sshd \
    && chgrp staff /var/log/supervisor \
    && chmod g+w /var/log/supervisor \
    && chgrp staff /etc/supervisor/conf.d/supervisord.conf \
    && git config --system push.default simple \
    && git config --system url.'https://github.com/'.insteadOf git://github.com/

# Open ports
EXPOSE 8787
# Start supervisor
CMD supervisord
