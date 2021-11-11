#################################################################
# Dockerfile
#
# Version:          0.0.1
# Software:         pAss
# Software Version: 0.0.2
# Description:      A gene centric metagenomics assembly and annotation pipeline
# Website:          https://github.com/etheleon/pAss
# Tags:             Genomics Metagenomics
# Provides:         MEGAN 5
# Base Image:       etheleon/pAssbase
#Run CMD:  	ROOTDIR=/Users/uesu/github/reAssemble/justK03043
#		docker run -v $ROOTDIR/data/contigs:/data/contigs \
#		    -v $ROOTDIR/data/konr:/data/refSeqProtDB \
#		    -v $ROOTDIR/out:/data/out  \
#		    -v $ROOTDIR/misc:/data/misc newpass:latest \
#		    maxDiversity --outputDIR /data/out --format --threads 8 --refseqKO /data/refSeqProtDB  --contigs /data/contigs  --megan /usr/local/bin/MEGAN --meganLicense /data/misc/MEGAN5-academic-license.txt
#################################################################

# Build image with:  docker build -t krizsan/ubuntu1504java8:v1 .
 
FROM etheleon/passbase:0.0.1

RUN git clone https://github.com/etheleon/pAss.git /tmp/pAss

WORKDIR /tmp/pAss
#RUN carton
RUN minil install

ENV PATH=/usr/local/megan:/tmp/pAss:${PATH}
ENV PERL5LIB=/tmp/pAss/local/lib/perl5:/tmp/pAss/local/share/perl/5.22.1

VOLUME ["/data/contigs", "/data/refSeqProtDB", "/data/out", "data/misc"]
ENTRYPOINT ["/tmp/pAss/script/maxDiversity"]
CMD ["--outputDIR", "/data/out", "--format", "--refseqKO", "/data/refSeqProtDB", "--contigs", "/data/contigs", "--megan", "/usr/local/bin/MEGAN", "--meganLicense", "/data/misc/MEGAN5-academic-license.txt"]

#################### INSTALLATION ENDS ##############################
MAINTAINER Wesley GOI <wesley@bic.nus.edu.sg>
