FROM r-base:3.3.2

RUN apt-get update \
   && apt-get install -y --no-install-recommends  \
   libcurl4-openssl-dev \
   libssl-dev \
   libxml2-dev





RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite("QuasR" );'


RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite("BSgenome.Hsapiens.UCSC.hg38" );'

RUN Rscript -e 'source("http://bioconductor.org/biocLite.R"); biocLite("DESeq2");'