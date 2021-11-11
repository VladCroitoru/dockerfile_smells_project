# copyright 2017-2018 Regents of the University of California and the Broad Institute. All rights reserved.

FROM r-base:3.4.1

RUN mkdir /build

RUN apt-get update && apt-get upgrade --yes && \
    apt-get install build-essential --yes && \
    apt-get install python --yes && \
    wget --no-check-certificate https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py 

RUN pip install awscli 

RUN apt-get update && apt-get upgrade --yes && \
    apt-get install -t unstable libmariadbclient-dev  --yes && \
    apt-get install -t unstable libssl-dev  --yes && \
    apt-get install curl --yes 

RUN    apt-get install libxml2-dev --yes && \
    apt-get install libcurl4-gnutls-dev --yes && \
    apt-get install mesa-common-dev --yes 

    

COPY common/container_scripts/runS3OnBatch.sh /usr/local/bin/runS3OnBatch.sh
COPY common/container_scripts/installPackages.R-2  /build/source/installPackages.R
COPY sources.list /etc/apt/sources.list
COPY common/container_scripts/runLocal.sh /usr/local/bin/runLocal.sh
COPY Rprofile.gp.site ~/.Rprofile
COPY Rprofile.gp.site /usr/lib/R/etc/Rprofile.site
RUN chmod ugo+x /usr/local/bin/runS3OnBatch.sh
ENV R_LIBS_S3=/genepattern-server/Rlibraries/R344/rlibs
ENV R_LIBS=/usr/local/lib/R/site-library
ENV R_HOME=/usr/local/lib64/R
COPY install_stuff.R /build/source

RUN Rscript /build/source/install_stuff.R
 
CMD ["/usr/local/bin/runS3OnBatch.sh" ]

