FROM ubuntu:latest
MAINTAINER marko.marinkovic@sbgenomics.com
# RUN apt-get -y update
# RUN wget --no-check-certificate wget https://github.com/samtools/samtools/releases/download/1.2/samtools-1.2.tar.bz2
ADD https://github.com/markomarinkovic/autobuild/raw/master/test.sh /home
WORKDIR /home
RUN chmod +x test.sh
