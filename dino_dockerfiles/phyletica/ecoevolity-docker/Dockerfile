FROM ubuntu:bionic

# Install dependencies for ecoevolity and pycoevolity
RUN apt-get update -q && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y -q \
        git \
        cmake \
        g++ \
        python \
        python-pip

# Install R for pycoevolity plotting
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y -q --no-install-recommends \
        r-base

# Install R packages used by pycoevolity
RUN R -e 'install.packages(c("ggplot2", "ggridges"), repos = "http://cloud.r-project.org/")'

# Download build and install ecoevolity
RUN git clone https://github.com/phyletica/ecoevolity.git && \
    cd ecoevolity && \
    ./build.sh --prefix /usr/local

# Install pycoevolity via pip
RUN pip install git+git://github.com/phyletica/pycoevolity.git

# Download example data and config file
RUN git clone https://github.com/phyletica/ecoevolity-example-data.git

# Let's give it a spin
RUN cd ecoevolity-example-data && \
    mkdir test && \
    ecoevolity --relax-missing-sites --relax-triallelic-sites --ignore-data --prefix ./test/ ecoevolity-config.yml && \
    cd test && \
    pyco-sumtimes ecoevolity-config-state-run-1.log && \
    cd .. && \
    rm -r test
