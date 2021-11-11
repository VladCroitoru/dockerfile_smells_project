# Base Docker Image
FROM r-base

# Maintainer
MAINTAINER kapeelchougule "kchougul@cshl.edu"

RUN apt-get update -qq \ 
  && apt-get install -t unstable -y --no-install-recommends \
    libcurl4-openssl-dev \
    libssl-dev \
    libsqlite3-dev \
    libxml2-dev \
    qpdf \
    vim \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/ \
  && rm -rf /tmp/downloaded_packages/ /tmp/*.rds

# Install devtools
RUN install2.r --error \
  devtools

RUN echo 'source("https://bioconductor.org/biocLite.R")' > /tmp/packages.R
RUN echo 'biocLite("rhdf5")' >> /tmp/packages.R
RUN echo 'biocLite("devtools")' >> /tmp/packages.R
RUN echo 'biocLite("pachterlab/sleuth")' >> /tmp/packages.R
RUN echo 'install.packages("getopt",dependencies = TRUE)' >> /tmp/packages.R
RUN Rscript /tmp/packages.R

ADD sleuth.R /usr/bin/
RUN [ "chmod", "+x",  "/usr/bin/sleuth.R" ]
ENTRYPOINT ["sleuth.R"]
#CMD ["Rscript", "/usr/bin/sleuth.R"]

