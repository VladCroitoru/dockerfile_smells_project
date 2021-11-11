FROM indigodatacloud/ubuntu-sshd:16.04

RUN set -e \
      && apt-get -y update \
      && apt-get -y upgrade \
      && apt-get -y install wget unzip git make g++ zlib1g-dev  perl python-pip libpython2.7-dev
RUN  add-apt-repository -y ppa:openjdk-r/ppa  
RUN apt-get update   
RUN apt-get install -y openjdk-7-jre  


#Download and install prinseq
RUN set -e \
      && cd /usr/local/src \
      && wget 'https://sourceforge.net/projects/prinseq/files/latest/download?source=files' -O prinseq.tar.gz \
      && tar xzvf prinseq.tar.gz \
      && cd prinseq-* \
      && chmod +x *.pl \
      && cp *.pl /usr/local/bin

    

# Download FastQC
ADD http://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.5.zip /tmp/

# Install FastQC
RUN cd /usr/local && \
    unzip /tmp/fastqc_*.zip && \
    chmod 755 /usr/local/FastQC/fastqc && \
    ln -s /usr/local/FastQC/fastqc /usr/local/bin/fastqc && \
    rm -rf /tmp/fastqc_*.zip


#install CutAdapt
RUN pip install 'cutadapt==1.9.1'

#install Blat
RUN wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/blat/blat -P /usr/local/bin
RUN chmod a+x /usr/local/bin/blat

#Make sure you have all the perl modules you need for the trimming
RUN apt-get install -y libjson-perl
RUN apt-get install -y libgraphics-primitive-driver-cairo-perl
RUN cpan Statistics::PCA

#Installing One Data Client

RUN apt-get install -y software-properties-common
RUN apt-add-repository ppa:ansible/ansible
RUN apt-get update && \
    apt-get install -y ansible && \
    rm -rf /var/lib/apt/lists/* 
RUN ansible-galaxy install indigo-dc.oneclient && \
    ansible-playbook /etc/ansible/roles/indigo-dc.oneclient/tests/test.yml

CMD /bin/bash -l
