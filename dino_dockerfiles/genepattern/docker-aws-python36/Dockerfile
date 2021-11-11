# copyright 2017-2018 Regents of the University of California and the Broad Institute. All rights reserved.
FROM python:3.6

MAINTAINER Ted Liefeld <jliefeld@cloud.ucsd.edu>

# ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 # 2018-04-06:20:14:05 EJ trying something out, I may reverse this change
ENV LANG=C LC_ALL=C

COPY common/container_scripts/runS3OnBatch.sh common/container_scripts/runLocal.sh /usr/local/bin/ 

RUN mkdir /build

RUN mkdir /conda && \
    cd /conda && \
    wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda
    
ENV PATH="/opt/conda/bin:${PATH}"

ADD requirements.txt /build/requirements.txt
RUN pip install -r /build/requirements.txt
RUN conda install R==3.3.2 && \
	conda install rpy2 && \
	pip install sklearn && \
    	pip install awscli && \
    	pip install cuzcatlan ccal && \
  	chmod ugo+x /usr/local/bin/runS3OnBatch.sh && \
    	chmod ugo+x /usr/local/bin/runLocal.sh 



CMD [ "/usr/local/bin/runS3OnBatch.sh"]
