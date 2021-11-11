#USE BLAST BINARIES FROM UMMIDOCK REPO 
FROM ummidock/blast_binaries:2.6.0-binaries 
WORKDIR /NGStools/
RUN apt-get update

RUN apt-get update && apt-get -y install \
	bc \
	bzip2 \
	gcc \
	git \
	gzip \
	make \
	wget  \
	unzip \
	python \
	python-pip \
	parallel \
	libncurses5-dev \
	libncursesw5-dev \
	zlib1g-dev

#get bowtie
RUN wget https://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.9/bowtie2-2.2.9-linux-x86_64.zip && unzip bowtie2-2.2.9-linux-x86_64.zip
ENV PATH="/NGStools/bowtie2-2.2.9:$PATH"

RUN wget https://sourceforge.net/projects/samtools/files/samtools/0.1.19/samtools-0.1.19.tar.bz2
RUN mkdir samtools && tar jxf samtools-0.1.19.tar.bz2 -C samtools --strip-components=1
WORKDIR /NGStools/samtools/
#RUN ./configure --without-curses --disable-bz2 --disable-lzma
RUN make
ENV PATH="/NGStools/samtools:$PATH"

WORKDIR /NGStools/
RUN rm -rf samtools-0.1.19.tar.bz2 

RUN pip2 install --upgrade numpy PyYaml lxml biopython

RUN git clone https://github.com/phe-bioinformatics/emm-typing-tool
ENV PATH="/NGStools/emm-typing-tool:$PATH"

RUN mkdir reference
WORKDIR /NGStools/EMM_data/
RUN wget ftp://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/006/785/GCF_000006785.2_ASM678v2/GCF_000006785.2_ASM678v2_genomic.fna.gz && gunzip ./*.gz
RUN makeblastdb -in GCF_000006785.2_ASM678v2_genomic.fna -dbtype nucl  -out reference
RUN cp GCF_000006785.2_ASM678v2_genomic.fna reference.seq

#WORKDIR /NGStools/
#RUN mkdir EMM_data
RUN cp /NGStools/emm-typing-tool/edit_allele_file.sh /NGStools/EMM_data/
#WORKDIR /NGStools/EMM_data/
RUN wget ftp://ftp.cdc.gov/pub/infectious_diseases/biotech/tsemm/trimmed.tfa
RUN sh edit_allele_file.sh

WORKDIR /NGStools/
RUN emm_typing.py -h

RUN apt-get -y install emboss
