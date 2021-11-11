FROM ubuntu:14.04 
RUN apt-get update -qq --fix-missing; \ 
	apt-get install -qq -y wget unzip; 
RUN wget -q -O bowtie2.zip http://sourceforge.net/projects/bowtie-bio/files/bowtie2/2.2.4/bowtie2-2.2.4-linux-x86_64.zip/download; \ 
	unzip bowtie2.zip -d /opt/; \ 
	ln -s /opt/bowtie2-2.2.4/ /opt/bowtie2; \ 
	rm bowtie2.zip 
ENV PATH $PATH:/opt/bowtie2 
