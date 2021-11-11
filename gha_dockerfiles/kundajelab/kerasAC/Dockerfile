FROM  kundajelab/anaconda-tensorflow-keras:latest
MAINTAINER Anna Shcherbina <annashch@stanford.edu>

#
# Install kerasAC and dependencies
#
RUN apt-get update
RUN apt-get install -y libz-dev liblzma-dev gcc libcurl4 libcurl4-openssl-dev samtools
RUN pip install --upgrade pip
RUN pip install tiledb>=0.5.2 \
    		pysam \
		psutil \
		tables \
		numpy>=1.9 \
		keras>=2.2 \
		h5py \
		pandas \
		deeplift \
		abstention \
		boto3 \
		pyBigWig

RUN pip install pysam 
WORKDIR /opt
RUN git clone https://github.com/kundajelab/kerasAC.git
WORKDIR /opt/kerasAC
RUN python setup.py build
RUN python setup.py develop

