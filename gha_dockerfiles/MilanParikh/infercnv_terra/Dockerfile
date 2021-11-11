# Docker file for inferCNV
FROM rocker/r-base:4.1.0

LABEL org.label-schema.license="BSD-3-Clause" \
      org.label-schema.vendor="Broad Institute" \
      maintainer="Milan Parikh <mparikh@broadinstitute.org>"

RUN apt-get update && apt-get -y install curl libssl-dev libcurl4-openssl-dev \
                                    build-essential gnupg libfftw3-dev default-jdk \
                                    libxml2-dev zlib1g-dev git jags \
                                    python3 python3-dev python3-pip python3-igraph \
                                    libtool autoconf automake bison flex\
                                    # r-cran-cluster r-cran-seurat \
                                    r-cran-rjags r-cran-optparse r-cran-biocmanager time && \
                      apt-get clean && rm -rf /var/tmp/* \
                                    /tmp/* /var/lib/apt/lists/*

RUN pip install --upgrade pip --no-cache-dir && \
    pip install setuptools==57.2.0 --no-cache-dir && \
    pip install numpy==1.21.2 --no-cache-dir && \
    pip install pandas==1.3.2 --no-cache-dir && \
    pip install scipy==1.7.0 --no-cache-dir && \
    pip install Cython==0.29.24 --no-cache-dir && \
    pip install pybind11==2.7.0 --no-cache-dir && \
    pip install scikit-image==0.18.2 --no-cache-dir && \
    pip install scikit-learn==0.24.2 --no-cache-dir && \
    pip install h5py==3.3.0 --no-cache-dir && \
    pip install fitsne==1.2.1 --no-cache-dir && \
    pip install importlib-metadata==4.6.1 --no-cache-dir && \
    pip install joblib==1.0.1 --no-cache-dir && \
    pip install psutil==5.8.0 --no-cache-dir && \
    pip install threadpoolctl==2.2.0 --no-cache-dir && \
    pip install python-igraph==0.9.6 --no-cache-dir && \
    pip install leidenalg==0.8.7 --no-cache-dir && \
    pip install lightgbm==3.2.1 --no-cache-dir && \
    pip install loompy==3.0.6 --no-cache-dir && \
    pip install matplotlib==3.4.2 --no-cache-dir && \
    pip install natsort==7.1.1 --no-cache-dir && \
    pip install numba==0.53.1 --no-cache-dir && \
    pip install scanorama==1.7.1 --no-cache-dir && \
    pip install scikit-misc==0.1.4 --no-cache-dir && \
    pip install seaborn==0.11.1 --no-cache-dir && \
    pip install statsmodels==0.12.2 --no-cache-dir && \
    pip install numcodecs==0.8.0 --no-cache-dir && \
    pip install networkx==2.5.1 --no-cache-dir && \
    pip install zarr==2.8.3 --no-cache-dir && \
    pip install anndata==0.7.6 --no-cache-dir && \
    pip install hnswlib==0.5.2 --no-cache-dir && \
    pip install louvain==0.7.0 --no-cache-dir && \
    pip install umap-learn==0.5.1 --no-cache-dir && \
    pip install torch==1.9.0 --no-cache-dir && \
    pip install harmony-pytorch==0.1.6 --no-cache-dir && \
    pip install cirrocumulus==1.1.17.post1 --no-cache-dir && \
    pip install annoy==1.17.0 --no-cache-dir && \
    pip install pegasusio==0.3.1.post2 --no-cache-dir && \
    pip install demuxEM==0.1.6 --no-cache-dir && \
    pip install forceatlas2-python==1.1 --no-cache-dir && \
    pip install nmf-torch==0.1.1 --no-cache-dir && \
    pip install pegasuspy==1.4.2 --no-cache-dir

RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add - && \
    apt-get update -y && apt-get install -y google-cloud-sdk=348.0.0-0

# Install R and Bioconductor packages
RUN echo "options(repos = c(CRAN = 'https://cran.rstudio.com'))" >.Rprofile
RUN R -e "install.packages(c('cluster', 'Seurat'), repos = 'http://cran.us.r-project.org')"
RUN R -e "BiocManager::install('infercnv')"

# Checkout and install infercnv
# update to version bump commit
RUN git clone https://github.com/broadinstitute/infercnv && cd infercnv && \
      git checkout master && git checkout 18e7f52ce5dca338365838ff52c30afeee41f5fc && \
      R CMD INSTALL . 

ENV PATH=${PATH}:/infercnv/scripts

CMD inferCNV.R --help

#new addition to add modified inferCNV terminal command with --up_to_step support
COPY inferCNV.R /infercnv/scripts/inferCNV.R

RUN chmod +x /infercnv/scripts/inferCNV.R

RUN cd infercnv && \
    R CMD INSTALL .