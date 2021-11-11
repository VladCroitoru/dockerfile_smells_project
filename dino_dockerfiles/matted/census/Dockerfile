FROM ipython/scipystack

MAINTAINER Matt Edwards <matted@mit.edu>

RUN mkdir /root/census
WORKDIR /root/census
RUN git clone https://github.com/matted/census.git .

RUN curl -o miniconda.sh http://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh
RUN chmod a+x miniconda.sh
RUN ./miniconda.sh -b
RUN /root/miniconda/bin/conda update --yes conda
RUN /root/miniconda/bin/conda create --yes -n conda python=2.7
RUN /root/miniconda/bin/conda install --yes python=2.7 atlas numpy scipy pysam

ENV PATH /root/miniconda/bin/:$PATH

RUN python setup.py install --quiet

CMD echo "Please run bam_to_histo.py or calculate_libsize.py."

# Examples:
#
# Build the image:
# docker build -t=matted/census .
#
# Investigate the image:
# docker run -t --rm=true -i matted/census /bin/bash
#
# Pipe input files to the image so we can process without attaching any directories:
# cat example_duplicate_histo.txt | docker run --rm=true -i matted/census calculate_libsize.py /dev/stdin > output.txt
# 
# Run on files in the current directory and grab the output to a file:
# docker run -t --rm=true -i -v `pwd`:/tmp -w=/tmp matted/census calculate_libsize.py example_duplicate_histo.txt > output.txt
#
