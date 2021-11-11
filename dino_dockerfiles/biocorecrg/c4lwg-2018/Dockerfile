# Here we define the base image, in this case one specific Debian distro
# This aspect is important for reproducibility / stability 
FROM biocorecrg/debian-perlbrew-pyenv-java:stretch

# File Author / who created this. Contact point in case of problem
MAINTAINER Bioinformatics Core CRG <biocore@crg.eu>

# Specific software versions
ARG FASTQC_VERSION=0.11.5
ARG MULTIQC_VERSION=1.7
ARG BOWTIE_VERSION=1.2.1.1

#Install FASTQC
RUN cd /usr/local; curl -k -L https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v${FASTQC_VERSION}.zip > fastqc.zip
RUN cd /usr/local; unzip fastqc.zip; rm fastqc.zip; chmod 775 FastQC/fastqc; ln -s /usr/local/FastQC/fastqc /usr/local/bin/fastqc

# Install bowtie 
RUN cd /usr/local; curl --fail --silent --show-error --location --remote-name https://github.com/BenLangmead/bowtie/releases/download/v$BOWTIE_VERSION/bowtie-${BOWTIE_VERSION}-linux-x86_64.zip
RUN cd /usr/local; unzip -d /usr/local bowtie-${BOWTIE_VERSION}-linux-x86_64.zip
RUN cd /usr/local; rm bowtie-${BOWTIE_VERSION}-linux-x86_64.zip
RUN cd /usr/local/bin; ln -s ../bowtie-${BOWTIE_VERSION}/bowtie* .

# Install MultiQC
RUN pip install numpy matplotlib 
RUN pip install -I multiqc==${MULTIQC_VERSION}

