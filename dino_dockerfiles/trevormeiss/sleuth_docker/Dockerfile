# This is the Dockefile to build DToxS
# Base Docker Image
FROM r-base

# Maintainer
MAINTAINER Trevor Meiss "tmeiss@uw.edu"

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
RUN echo 'biocLite("pachterlab/sleuth")' >> /tmp/packages.R
RUN Rscript /tmp/packages.R

ENV HOME /home/user
WORKDIR $HOME

ADD cuffdiff2_data_kallisto_results/ $HOME/test/cuffdiff2_data_kallisto_results/
ADD test.R $HOME/test

CMD ["/bin/bash"]
