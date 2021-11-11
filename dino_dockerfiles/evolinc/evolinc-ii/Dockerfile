FROM ubuntu:18.04
MAINTAINER Upendra Devisetty <upendra@cyverse.org>
LABEL Description "This Dockerfile is for evolinc-ii pipeline"

RUN echo 'debconf debconf/frontend select Noninteractive' | debconf-set-selections
RUN apt-get update && apt-get install -y g++ \
		make \
		git \
		zlib1g-dev \
		libcurl4-openssl-dev \
		libssl-dev \
		libxml2-dev \
		python3 \
		python3-pip \
		python3-biopython \
		wget \
		curl \
		python3-matplotlib \
		python3-numpy \
        	python3-pandas \
		perl \
		bioperl \
		gnupg2 \
        	openjdk-8-jdk \
		ghostscript

# Bedtools
RUN wget https://github.com/arq5x/bedtools2/releases/download/v2.26.0/bedtools-2.26.0.tar.gz
RUN tar zxvf bedtools-2.26.0.tar.gz
RUN cd bedtools2 && make
RUN cd ..

# Cufflinks
RUN wget -O- http://cole-trapnell-lab.github.io/cufflinks/assets/downloads/cufflinks-2.2.1.Linux_x86_64.tar.gz | tar xzvf -

# Mafft
RUN apt-get install -y mafft

# R libraries
RUN echo "deb https://cloud.r-project.org/bin/linux/ubuntu bionic-cran40/" >> /etc/apt/sources.list
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E298A3A825C0D65DFD57CBB651716619E084DAB9
RUN apt-get update
RUN apt-get install -y r-base r-base-dev
RUN Rscript -e 'install.packages("BiocManager");'
RUN Rscript -e 'install.packages("UpSetR", dependencies = TRUE, repos="http://cran.rstudio.com/");'
RUN Rscript -e 'install.packages("getopt", dependencies = TRUE, repos="http://cran.rstudio.com/");'
RUN Rscript -e 'install.packages("reshape2", dependencies = TRUE, repos="http://cran.rstudio.com/");'
RUN Rscript -e 'install.packages("dplyr", dependencies = TRUE, repos="http://cran.rstudio.com/");'
RUN Rscript -e 'install.packages("XML", dependencies = TRUE, repos="http://cran.rstudio.com/");'
RUN Rscript -e 'BiocManager::install("rtracklayer", dependencies = TRUE);'

# RAxML
RUN git clone https://github.com/stamatak/standard-RAxML.git
WORKDIR /standard-RAxML
RUN make -f Makefile.SSE3.PTHREADS.gcc
RUN cp raxmlHPC-PTHREADS-SSE3 /usr/bin/
WORKDIR /

#ViennaRNA package for RNA structure prediction
RUN wget https://www.tbi.univie.ac.at/RNA/download/sourcecode/2_4_x/ViennaRNA-2.4.14.tar.gz
RUN tar -zxvf ViennaRNA-2.4.14.tar.gz
RUN cd ViennaRNA-2.4.14 \
	&& ./configure \
	&& make \
	&& make install

#locarna for RNA structure prediction
RUN wget https://github.com/s-will/LocARNA/releases/download/v1.9.2.1/locarna-1.9.2.1.tar.gz
RUN tar -zxvf locarna-1.9.2.1.tar.gz
RUN cd locarna-1.9.2.1 \
	&& ./configure \
	&& make \
	&& make install

#minimap2
RUN wget https://github.com/lh3/minimap2/releases/download/v2.17/minimap2-2.17_x64-linux.tar.bz2
RUN tar -jxvf minimap2-2.17_x64-linux.tar.bz2

#samtools
RUN wget https://github.com/samtools/samtools/releases/download/1.10/samtools-1.10.tar.bz2
RUN tar -jxvf samtools-1.10.tar.bz2
RUN cd samtools-1.10 \
	&& ./configure --prefix=/samtools \
	&& make \
	&& make install


# Setting paths to all the softwares
ENV BINPATH /usr/bin
ENV PATH /usr/local/lib/:$PATH
ENV PATH /minimap2-2.17_x64-linux/:$PATH
ENV PATH /bedtools2/bin/:$PATH
ENV PATH /cufflinks-2.2.1.Linux_x86_64/:$PATH
ENV PATH /ncbi-blast-2.6.0+/bin/:$PATH
ENV PATH /samtools-1.10/:$PATH

# Add all the scripts to the root directory Path
ADD *.py *.pl *.R *.sh *.jar /
RUN chmod +x /Building_Families.sh
RUN chmod +x /evolinc-part-II.sh && cp /evolinc-part-II.sh $BINPATH

ENTRYPOINT ["/evolinc-part-II.sh"]
CMD ["-h"]
