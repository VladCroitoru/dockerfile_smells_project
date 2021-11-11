FROM bioconductor/release_core2
MAINTAINER Diego Diez <diego10ruiz@gmail.com>

# Update the repository sources list.
RUN apt-get update

## Add general tools.
RUN apt-get install -y build-essential git python python-dev
RUN apt-get install -y autoconf
RUN apt-get install -y libopenmpi-dev openmpi-bin ssh
RUN apt-get install -y libxml2-dev libxslt1-dev ghostscript

## Add requirements for R packages.
RUN apt-get install -y libudunits2-dev

## Add samtools.
RUN apt-get install -y samtools

## Add MACS2.
# Install MACS dependancies.
RUN apt-get install -y python-numpy cython

# Clone MACS repository and checkout the requested tag.
RUN cd /tmp && git clone https://github.com/taoliu/MACS.git && cd MACS && git checkout v2.0.9

# Compile and install MACS.
RUN cd /tmp/MACS && python setup.py install

# Cleanup.
RUN apt-get clean
RUN rm -rf /tmp/MACS

## Install MEME suite.
# Download and untar.
ADD http://meme-suite.org/meme-software/4.11.3/meme_4.11.3_1.tar.gz /tmp
RUN cd /tmp && tar zxvf meme_4.11.3_1.tar.gz

# Compile.
RUN cd /tmp/meme_4.11.3 && ./configure --prefix /opt
RUN cd /tmp/meme_4.11.3 && make
#RUN make test
RUN cd /tmp/meme_4.11.3 && make install

# Cleanup.
RUN cd /tmp
RUN rm -rf /tmp/meme_4.11.3

# Add /opt/bin to PATH.
ENV PATH /opt/bin:$PATH

## Install R packages.
ADD install.R /tmp/
RUN R -f /tmp/install.R
