FROM continuumio/miniconda
MAINTAINER Kevin Menden <kevin.menden@t-online.de>
LABEL authors="kevin.menden@t-online.de" \
    description="Docker image containing all requirements for hybrid-assembly pipeline"

# Install MaSuRCA 3.2.9
RUN apt-get update && apt-get install -y g++ libboost-all-dev zlib1g-dev libbz2-dev make
RUN curl -fsSL https://github.com/alekseyzimin/masurca/raw/master/MaSuRCA-3.2.9.tar.gz -o /opt/MaSuRCA-3.2.9.tar.gz
RUN cd /opt/; tar -xzvf MaSuRCA-3.2.9.tar.gz; cd MaSuRCA-3.2.9; ./install.sh
ENV PATH $PATH:/opt/MaSuRCA-3.2.9/bin


# Create assembly-env
COPY environment.yml /
RUN conda env create -f /environment.yml && conda clean -a
ENV PATH /opt/conda/envs/assembly-env/bin:$PATH


# Create NanoQC environment
COPY nanoqc-env.yml /
RUN conda env create -f /nanoqc-env.yml

# Install PROCPS
RUN apt-get update && apt-get install -y procps
