# % Last Change: Tue Jan 07 11:58:35 AM 2020 CST
# Base Image
FROM continuumio/miniconda3:4.7.12

# Metadata
LABEL software="genomic data analysis" \
	description="docker image for general genomic data analysis" \
	website="https://github.com/litd/dana" \
	documentation="https://github.com/litd/dana" \
	license="https://github.com/litd/dana" \
	tags="Genomics" \
	maintainer="Tiandao Li <litd99@gmail.com>"

ENV PATH /opt/conda/bin:$PATH

# Installation
RUN conda install -c bioconda bcftools && \
	conda install -c bioconda bedtools && \
	conda install -c bioconda htslib && \
	conda install -c bioconda samtools && \
	conda clean --all --yes

WORKDIR /opt/conda/bin
RUN wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/bedSort
RUN chmod +x bedSort

# set timezone, debian and ubuntu
RUN ln -sf /usr/share/zoneinfo/America/Chicago /etc/localtime && \
	echo "America/Chicago" > /etc/timezone

CMD [ "/bin/bash" ]

