# Dockerfile for vix analysis
# Xiaomeng(Sophia) Wang, Dec 2017

# Usage: The dockerfile is to build a docker image.
# Usage: It guarantees that the software will always run the same, regardless of its environment.


# use rocker/tidyverse as the base image
FROM rocker/tidyverse


# get OS updates and install build tools
RUN apt-get update
RUN apt-get install -y build-essential


# install the ezknitr packages
RUN Rscript -e "install.packages('ezknitr', repos = 'http://cran.us.r-project.org')"


# install conda
RUN apt-get update --fix-missing && apt-get install -y wget bzip2 ca-certificates \
    libglib2.0-0 libxext6 libsm6 libxrender1 \
    git mercurial subversion

RUN echo 'export PATH=/opt/conda/bin:$PATH' > /etc/profile.d/conda.sh && \
    wget --quiet https://repo.continuum.io/archive/Anaconda3-5.0.1-Linux-x86_64.sh -O ~/anaconda.sh && \
    /bin/bash ~/anaconda.sh -b -p /opt/conda && \
    rm ~/anaconda.sh

RUN apt-get install -y curl grep sed dpkg && \
    TINI_VERSION=`curl https://github.com/krallin/tini/releases/latest | grep -o "/v.*\"" | sed 's:^..\(.*\).$:\1:'` && \
    curl -L "https://github.com/krallin/tini/releases/download/v${TINI_VERSION}/tini_${TINI_VERSION}.deb" > tini.deb && \
    dpkg -i tini.deb && \
    rm tini.deb && \
    apt-get clean

ENV PATH /opt/conda/bin:$PATH

ENTRYPOINT [ "/usr/bin/tini", "--" ]
CMD [ "/bin/bash" ]


# open the docker container
RUN mkdir docker-vix-analysis
ADD . /docker-vix-analysis
WORKDIR "docker-vix-analysis"

# Create Environment with environment.yml
RUN conda install nbformat
RUN conda install -c conda-forge ca-certificates
CMD ["conda", "env", "create", "-f", "environment.yml"]
#RUN conda env create -f "environment.yml"

# deactive source
RUN /bin/bash -c "source deactivate"
