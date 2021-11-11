FROM bioconductor/release_core2:R3.6.1_Bioc3.10

# bzip
RUN apt-get update
RUN apt-get install bzip2

# parallel
RUN mkdir /download && cd /download && wget http://ftp.gnu.org/gnu/parallel/parallel-20190722.tar.bz2 && tar xvf parallel-20190722.tar.bz2
RUN cd /download/parallel-20190722 && ./configure && make && make install

# basic packages
RUN Rscript -e "install.packages(c('Rtsne', 'devtools', 'dplyr','Hmisc','phangorn','reshape2','tidyverse', 'R.utils'))"

# dada2 through github
RUN Rscript -e "library('devtools'); devtools::install_github('benjjneb/dada2', ref='v1.14')"

# BiocManager packages
RUN Rscript -e "BiocManager::install(c('DECIPHER','DESeq2','edgeR','msa','phyloseq','ggplot2','gplots', 'cowplot'))"

# DirichletMultinomial
RUN apt-get -y install gsl-bin libgsl0-dev
RUN Rscript -e "BiocManager::install('DirichletMultinomial')"

RUN Rscript -e "install.packages(c('foreach','doParallel'))"

# more packages due to popular requests
RUN Rscript -e "devtools::install_github('jakobbossek/ggheatmap')"
# RUN Rscript -e "BiocManager::install(c('wesanderson', 'rstan'))"

RUN Rscript -e "devtools::install_github('bm2-lab/MetaTopics')"
RUN Rscript -e "BiocManager::install(c('topicmodels', 'slam'))"
