FROM google/cloud-sdk

MAINTAINER Allen Day "allenday@allenday.com"

ENV BUILD_PACKAGES="make gcc wget zlib1g-dev git g++ cmake python-dev python-setuptools"
ENV IMAGE_PACKAGES="bwa bedtools samtools picard-tools vcftools nginx maven openjdk-7-jdk"

RUN apt-get -y update
RUN apt-get -y --no-install-recommends install $BUILD_PACKAGES $IMAGE_PACKAGES

#for gsutil
WORKDIR /opt
RUN easy_install -U pip
RUN pip install -U crcmod

#freebayes
WORKDIR /opt
RUN git clone --recursive git://github.com/ekg/freebayes.git
RUN wget http://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.8.1-3/sratoolkit.2.8.1-3-ubuntu64.tar.gz
RUN mkdir bin
COPY bin/fastq-exclude.pl /opt/bin/fastq-exclude.pl

#sratools
WORKDIR /opt
RUN tar -xvzf sratoolkit.2.8.1-3-ubuntu64.tar.gz
RUN mv sratoolkit.2.8.1-3-ubuntu64 sratoolkit
RUN rm sratoolkit.2.8.1-3-ubuntu64.tar.gz

WORKDIR /opt/freebayes
RUN make

#vcflib
WORKDIR /opt/freebayes/vcflib
RUN make

#gatk
ENV SHA=f19618653a0d23baaf147efe7f14aeb4eeb0cbb8
WORKDIR /opt
RUN git clone https://github.com/broadgsa/gatk-protected.git gatk
WORKDIR /opt/gatk
RUN git reset --hard $SHA
RUN mvn verify
RUN bash -c 'echo -e "#!/bin/bash\njava -jar /opt/gatk/target/GenomeAnalysisTK.jar \$@"' > /opt/gatk/gatk
RUN chmod +x /opt/gatk/gatk


WORKDIR /opt
RUN ln -s /opt/freebayes/bamtools /opt/bamtools
RUN ln -s /opt/freebayes/vcflib /opt/vcflib
RUN ln -s /opt/freebayes/fastahack /opt/fastahack
RUN ln -s /opt/vcflib/tabixpp/htslib /opt/htslib

WORKDIR /

RUN echo "daemon off;" >> /etc/nginx/nginx.conf

## cleanup
RUN apt-get -y remove --purge $BUILD_PACKAGES
#RUN apt-get -y remove --purge $(apt-mark showauto)
RUN rm -rf /var/lib/apt/lists/*

CMD /usr/sbin/nginx
