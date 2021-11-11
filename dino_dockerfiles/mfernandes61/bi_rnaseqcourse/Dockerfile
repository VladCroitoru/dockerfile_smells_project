FROM dorowu/ubuntu-desktop-lxde-vnc
MAINTAINER Mark Fernandes <mark.fernandes@ifr.ac.uk>
# Environment to deliver BI RNAseq course using  LXDE and VNC server under Docker

RUN REL="$(lsb_release -c -s)"
# Add the appropriate repositories including CRAN
RUN \
  apt-get update && \
  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E084DAB9 && \
   apt-get install -y  software-properties-common && \
#   add-apt-repository  "deb http://archive.ubuntu.com/ubuntu '$REL' universe" && \
#	add-apt-repository  "deb http://archive.ubuntu.com/ubuntu '$REL' main restricted universe multiverse" && \
#	add-apt-repository  "deb http://archive.ubuntu.com/ubuntu '$REL'-updates main restricted universe multiverse" && \
#	add-apt-repository  "deb http://archive.ubuntu.com/ubuntu '$REL'-backports main restricted universe multiverse" && \
#  add-apt-repository  "deb http://cran.ma.imperial.ac.uk/bin/linux/ubuntu '$REL'/" && \

   add-apt-repository  "deb http://archive.ubuntu.com/ubuntu trusty universe" && \
	add-apt-repository  "deb http://archive.ubuntu.com/ubuntu trusty main restricted universe multiverse" && \
	add-apt-repository  "deb http://archive.ubuntu.com/ubuntu trusty-updates main restricted universe multiverse" && \
	add-apt-repository  "deb http://archive.ubuntu.com/ubuntu trusty-backports main restricted universe multiverse" && \
   add-apt-repository  "deb http://cran.ma.imperial.ac.uk/bin/linux/ubuntu trusty/" && \
   apt-get update && apt-get install -y wget unzip default-jre r-base r-base-dev samtools fastqc \
		libcurl4-openssl-dev libxml2-dev &&\
	rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 

#
# create our fastqc folder & files that are not installed by apt-get install fastqc :-(
RUN mkdir /etc/fastqc && mkdir /etc/fastqc/Configuration
ADD fastqc/* /etc/fastqc/Configuration/
RUN mkdir /docs && cd /docs && wget http://www.bioinformatics.babraham.ac.uk/training/RNASeq_Course/RNA-Seq_analysis_course.pdf &&\
	wget http://www.bioinformatics.babraham.ac.uk/training/RNASeq_Course/Analysing%20RNA-Seq%20data%20Exercise.pdf
 RUN mkdir /data && cd /data && wget http://www.bioinformatics.babraham.ac.uk/training/RNASeq_Course/RNA-Seq_Course_Data.tar.gz && \
	tar zxf /data/*.tar.gz -C /data && rm /data/*.gz

RUN mkdir /tools && cd /tools && wget http://www.bioinformatics.babraham.ac.uk/projects/seqmonk/seqmonk_v1.37.0.zip && \
	wget ftp://ftp.ccb.jhu.edu/pub/infphilo/hisat2/downloads/hisat2-2.0.5-Linux_x86_64.zip && unzip seq*.zip && \
	unzip hisat*.zip && rm /tools/*.zip && chmod 755 /tools/Seq*/seqmonk && ln -s /tools/Seq*/seqmonk /usr/local/bin/ && \
	ln -s /tools/hisat2*/hisat2 /usr/local/bin/ && mkdir /tools/examples && cd /tools/examples && \
	wget http://www.bioinformatics.babraham.ac.uk/projects/seqmonk/example_seqmonk_data.smk
# cd /tools/SeqMonk chmod 755 seqmonk and ln -s  to /usr/local/bin/.  ln -s /tools/hisat2*/hisat2 /usr/local/bin/


USER root
#RUN R -e \"source('https://bioconductor.org/biocLite.R'); biocLite('DESeq2')\"
# RUN bash - -c "R -e \"source('http://bioconductor.org/biocLite.R'); biocLite('DESeq2')\""
# -c means commands read from string 

ADD Welcome.txt /etc/motd
RUN mkdir /scripts
ADD /scripts/*.sh /scripts/
RUN chmod +x /scripts/*.sh && ln -s /scripts/add2R /usr/local/bin/
# RUN add2R.sh

EXPOSE 22 
VOLUME /Coursedata

