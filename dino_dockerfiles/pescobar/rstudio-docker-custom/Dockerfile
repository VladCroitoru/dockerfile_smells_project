FROM rocker/rstudio:3.4.0

RUN apt-get update \
 && apt-get install -y \
    file \
    libgcj15-dev \
    libgdal1-dev \
    libpng12-dev \
    git \
    libapparmor1 \
    libcurl4-openssl-dev \
    libedit2 \
    libssl-dev \
    lsb-release \
    psmisc \
    python-setuptools \
    sudo \
    wget \
    antiword \
    autotools-dev \
    bwidget \
    cdbs \
    debhelper \
    fftw-dev \
    ggobi \
    graphviz \
    grass-dev \
    imagemagick \
    jags \
    libarmadillo-dev \
    libatk1.0-dev \
    libbam-dev \
    libblas-dev \
    libboost-dev \
    libboost-graph-dev \
    libcairo2-dev \
    libc-dev-bin \
    libcurl4-openssl-dev \
    libfftw3-dev \
    libfontconfig1 \
    libfontconfig1-dev \
    libfreetype6 \
    libfreetype6-dev \
    libgcj15-dev \
    libgd-dev \
    libgdal-dev \
    libgl1-mesa-dev \
    libglade2-dev \
    libglib2.0-dev \
    libglu1-mesa-dev \
    libgmp3-dev \
    libgraphviz-dev \
    libgsl0-dev \
    libgtk2.0-0 \
  && apt-get clean 

RUN Rscript -e "source ('https://bioconductor.org/biocLite.R'); biocLite(c('bit64', 'blob', 'pkgconfig', 'DBI', 'memoise', 'BH', 'plogr'))" \
    && Rscript -e "install.packages('https://stat.ethz.ch/CRAN/src/contrib/blob_1.1.0.tar.gz', repos=NULL)" \
    && Rscript -e "install.packages('https://stat.ethz.ch/CRAN/src/contrib/RSQLite_2.0.tar.gz', repos=NULL)" \
    && Rscript -e "source ('https://bioconductor.org/biocLite.R'); biocLite(c('affycoretools', 'oligoClasses', 'ggplot2', 'edgeR', 'DESeq2', 'goseq', 'GenomicFeatures', 'org.Mm.eg.db', 'org.Hs.eg.db', 'KEGG.db', 'pathview', 'pheatmap'))" 
