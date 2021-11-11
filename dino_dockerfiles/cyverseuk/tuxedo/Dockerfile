FROM ubuntu:14.04

LABEL ubuntu.version="14.04" bowtie2.version="2.1.0-2" cufflinks.version="2.1.1-4" cummerbund.version="2.4.1-1" R.version="3.0.2" samtools.version="0.1.19-1" tophat.version="2.0.9-1ubuntu1" 

ARG DEBIAN_FRONTEND=noninteractive

ADD https://raw.githubusercontent.com/cyverseuk/tuxedo/master/cummerbund_plot_scripts.r /usr/local/bin/

ADD https://raw.githubusercontent.com/cyverseuk/tuxedo/master/rna_seq_4_conditions_docker.py /usr/local/bin/

RUN echo "deb http://archive.ubuntu.com/ubuntu/ trusty multiverse" >> /etc/apt/sources.list && \
	apt-get update -y && apt-get -yy install bowtie2 software-properties-common samtools tophat cufflinks r-base r-bioc-cummerbund && \
	chmod 777 /usr/local/bin/rna_seq_4_conditions_docker.py && \
    	chmod 777 /usr/local/bin/cummerbund_plot_scripts.r

WORKDIR /data/

ENTRYPOINT ["python3", "/usr/local/bin/rna_seq_4_conditions_docker.py"]


