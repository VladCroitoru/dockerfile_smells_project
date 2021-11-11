FROM foodresearch/bppc
MAINTAINER Mark Fernandes <mark.fernandes@ifr.ac.uk>
#
USER root
RUN groupadd -g 110 med && usermod -a -G med guest
# Add required respositories
RUN add-apt-repository  "deb http://archive.ubuntu.com/ubuntu xenial main universe"
RUN add-apt-repository -y ppa:j-4/vienna-rna
RUN dpkg --configure -a
# install pre-requisites (QUIIME has a LOT of these)
RUN  apt-get update && apt-get install -y wget python-dev python-pip freetype* libfreetype6-dev libpng12-dev pkg-config default-jdk \
 ant r-base  r-base-dev libgsl-dev perl seqprep ampliconnoise gfortran unzip libssl-dev libzmq-dev libxml2 libxslt1.1 libxslt1-dev \
 subversion sqlite3 libsqlite3-dev mpich2 libreadline-dev libmysqlclient18 libmysqlclient-dev ghc libc6-i386 libbz2-dev tcl-dev \
 tk-dev libatlas-dev libatlas-base-dev liblapack-dev swig libhdf5-serial-dev ampliconnoise bwa  cd-hit clearcut raxml \
  fasttree infernal chimeraslayer rtax muscle mothur ea-utils med-config && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* 
 # vienna-rna
RUN echo ">>>Apt-get done<<<<"
#
# install base qiime & python pre-reqs
RUN pip install --upgrade pip  && pip install numpy && pip install h5py && pip install qiime && pip install ipython[all]
RUN echo ">>>>pip install done<<<<"
# Install sourcetracker
RUN mkdir /sourcetracker
ADD sourcetracker-0.9.8.tar.gz /sourcetracker/sourcetracker-0.9.8.tar.gz 
#RUN cd /sourcetracker && tar xzf sourcetracker-0.9.8.tar.gz
#
RUN ln -s /usr/lib/cd-hit/cd-hit /usr/bin/cd-hit && ln -s /usr/lib/ChimeraSlayer/ChimeraSlayer.pl /usr/bin/ChimeraSlayer.pl
#
RUN git clone https://github.com/qiime/qiime-deploy.git
RUN git clone https://github.com/qiime/qiime-deploy-conf.git
RUN echo ">>>>git cloning done<<<<"
ADD qiime.conf qiime-deploy/qiime.conf
ADD usearch5.2.236_i86linux32 /usr/bin/usearch

#RUN dpkg-reconfigure -phigh -a 
# qiime-dploy && qiime-deploy.py
RUN mkdir /qiime && python qiime-deploy/qiime-deploy.py /qiime -f qiime-deploy/qiime.conf && chmod +x /usr/bin/usearch && chmod +x /qiime/activate.sh
# 
ADD Welcome.txt /etc/motd
EXPOSE 8888
#Inherited from bppc Volumes /etc/shellinabox,/home, /var/log/supervisor. Ports22, 4200 Need temp writeable dir for qiime tests
# User should activate volumes in Kitematics and creat a guest subdir in home
#
USER guest
# Run shellinabox and keep process (& container) alive
ENTRYPOINT ["/scripts/launchsiab.sh"]
CMD ["/bin/bash"]
