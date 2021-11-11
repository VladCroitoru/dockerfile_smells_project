FROM ubuntu:14.04.3
MAINTAINER Kapeel Chougule
RUN apt-get update && apt-get install -y \
   build-essential \
   git \
   python \
   samtools
ENV HISAT2GIT https://github.com/infphilo/hisat2.git
RUN git clone "$HISAT2GIT" \
    && cd hisat2 \  
    && make
ENV PATH "/hisat2:$PATH"
ADD Hisat2_alignment.pl /usr/bin/
RUN [ "chmod", "+x",  "/usr/bin/Hisat2_alignment.pl" ]
ENTRYPOINT ["Hisat2_alignment.pl"]
