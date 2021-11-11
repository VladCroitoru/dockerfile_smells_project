FROM rocker/r-ver:4.1.0
MAINTAINER Fabrício Almeida-Silva <fabricio_almeidasilva@hotmail.com>

RUN apt-get update && apt-get install -y \
      python3-pip \
      git-core \
      libcurl4-openssl-dev \
      libgit2-dev \
      libglpk-dev \
      libgmp-dev \
      libicu-dev \
      libssl-dev \
      libxml2-dev \
      libpng-dev \
      libbz2-dev \
      liblzma-dev \
      make \
      pandoc \
      pandoc-citeproc \
      wget \
      libxml-libxml-perl \
      libidn11 \
      default-jre && \
      rm -rf /var/lib/apt/lists/*

ENV LD_LIBRARY_PATH="/usr/local/lib/:$LD_LIBRARY_PATH"

#-----Install SRAToolkit--------------------------------------------------------
RUN wget https://ftp-trace.ncbi.nlm.nih.gov/sra/sdk/2.11.1/sratoolkit.2.11.1-ubuntu64.tar.gz -O /tmp/sratoolkit.tar.gz && \
      tar zxvf /tmp/sratoolkit.tar.gz -C /opt/ && \
      rm /tmp/sratoolkit.tar.gz

#----Install FastQC-------------------------------------------------------------
RUN wget https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.9.zip -O /tmp/fastqc_v0.11.19.zip && \
      unzip /tmp/fastqc_v0.11.19.zip -d /opt && \
      rm /tmp/fastqc_v0.11.19.zip && \
      chmod 755 /opt/FastQC/fastqc && \
      ln -s /opt/FastQC/fastqc /usr/local/bin/fastqc

#----Install MultiQC------------------------------------------------------------
RUN pip3 install multiqc==1.11

#----Install STAR---------------------------------------------------------------
RUN wget https://github.com/alexdobin/STAR/archive/2.7.9a.tar.gz -O /tmp/star-2.7.9a.tar.gz && \
      tar -xzf /tmp/star-2.7.9a.tar.gz -C /opt/

#----Install Trimmomatic--------------------------------------------------------
RUN wget http://www.usadellab.org/cms/uploads/supplementary/Trimmomatic/Trimmomatic-0.39.zip -O /tmp/Trimmomatic-0.39.zip && \
      unzip /tmp/Trimmomatic-0.39.zip -d /opt && \
      rm /tmp/Trimmomatic-0.39.zip && \
      echo 'alias trimmomatic="java -jar opt/Trimmomatic-0.39/trimmomatic-0.39.jar"' >> ~/.bashrc

#----Install SortMeRNA----------------------------------------------------------
RUN wget https://github.com/biocore/sortmerna/releases/download/v4.3.4/sortmerna-4.3.4-Linux.sh -O /tmp/sortmerna-4.3.4-Linux.sh && \
      bash /tmp/sortmerna-4.3.4-Linux.sh --skip-license --prefix=/opt/

#----Install RSeQC--------------------------------------------------------------
RUN pip3 install RSeQC==4.0.0

#----Install salmon-------------------------------------------------------------
RUN wget https://github.com/COMBINE-lab/salmon/releases/download/v1.5.2/salmon-1.5.2_linux_x86_64.tar.gz -O /tmp/salmon-1.5.2.tar.gz && \
      tar -xzf /tmp/salmon-1.5.2.tar.gz -C /opt/ && \
      rm /tmp/salmon-1.5.2.tar.gz

#----Install kallisto-----------------------------------------------------------
RUN wget https://github.com/pachterlab/kallisto/releases/download/v0.46.2/kallisto_linux-v0.46.2.tar.gz -O /tmp/kallisto-0.46.2.tar.gz && \
      tar -xzf /tmp/kallisto-0.46.2.tar.gz -C /opt/ && \
      rm /tmp/kallisto-0.46.2.tar.gz

#----Install Subread------------------------------------------------------------
RUN wget https://sourceforge.net/projects/subread/files/subread-2.0.3/subread-2.0.3-Linux-x86_64.tar.gz -O /tmp/subread-2.0.3.tar.gz && \
      tar -xzf /tmp/subread-2.0.3.tar.gz -C /opt/ && \
      rm /tmp/subread-2.0.3.tar.gz

#----Install StringTie----------------------------------------------------------
RUN wget https://github.com/gpertea/stringtie/releases/download/v2.1.7/stringtie-2.1.7.Linux_x86_64.tar.gz -O /tmp/stringtie-2.1.7.tar.gz && \
      tar -zxf /tmp/stringtie-2.1.7.tar.gz -C /opt/ && \
      rm /tmp/stringtie-2.1.7.tar.gz

#----Install TACO---------------------------------------------------------------
RUN wget https://github.com/tacorna/taco/releases/download/v0.7.3/taco-v0.7.3.Linux_x86_64.tar.gz -O /tmp/taco-v0.7.3.tar.gz && \
      tar -xzvf /tmp/taco-v0.7.3.tar.gz -C /opt/ && \
      rm /tmp/taco-v0.7.3.tar.gz


#----Install imported R packages------------------------------------------------
RUN echo "options(repos = c(CRAN = 'https://cran.rstudio.com/'), download.file.method = 'libcurl', Ncpus = 4)" >> /usr/local/lib/R/etc/Rprofile.site
RUN R -e 'install.packages("remotes")'
RUN R -e 'install.packages("BiocManager")'
RUN Rscript -e 'remotes::install_github("almeidasilvaf/bears")'

#----Set environment variables--------------------------------------------------
ENV PATH="/opt/sratoolkit.2.11.1-ubuntu64/bin/:${PATH}"
ENV LD_LIBRARY_PATH="/usr/local/lib/:${LD_LIBRARY_PATH}"
ENV PATH="opt/STAR-2.7.9a/bin/Linux_x86_64_static/:${PATH}"
ENV PATH="/opt/bin/:${PATH}"
ENV PATH="/opt/salmon-1.5.2_linux_x86_64/bin/:${PATH}"
ENV PATH="/opt/kallisto/:${PATH}"
ENV PATH="/opt/subread-2.0.3-Linux-x86_64/bin/:${PATH}"
ENV PATH="/opt/stringtie-2.1.7.Linux_x86_64/:${PATH}"
ENV PATH="/opt/taco-v0.7.3.Linux_x86_64/:${PATH}"
