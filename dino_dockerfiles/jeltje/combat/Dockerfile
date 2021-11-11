FROM r-base

MAINTAINER jeltje.van.baren@gmail.com

RUN apt-get update && apt-get install -y \
	libxml2-dev \
	libcurl4-openssl-dev

RUN Rscript -e 'source("http://bioconductor.org/biocLite.R")' \
	-e 'biocLite("sva", ask=FALSE)' \
	-e 'install.packages("optparse")'

RUN mkdir /data

WORKDIR /data 

COPY ./combat.R /usr/local/bin

ENTRYPOINT ["/usr/local/bin/combat.R"]
CMD ["--help"]


