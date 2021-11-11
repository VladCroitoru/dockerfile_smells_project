FROM debian:stretch-slim

# ================================ from miniconda dockerfile:
# https://hub.docker.com/r/continuumio/miniconda/dockerfile

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
ENV PATH /opt/conda/bin:$PATH

RUN apt-get update --fix-missing && \
    apt-get install -y wget bzip2 ca-certificates curl git && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-4.6.14-Linux-x86_64.sh -O ~/miniconda.sh && \
    /bin/bash ~/miniconda.sh -b -p /opt/conda && \
    rm ~/miniconda.sh && \
    /opt/conda/bin/conda clean -tipsy && \
    ln -s /opt/conda/etc/profile.d/conda.sh /etc/profile.d/conda.sh && \
    echo ". /opt/conda/etc/profile.d/conda.sh" >> ~/.bashrc && \
    echo "conda activate base" >> ~/.bashrc

# ================================ end miniconda section

# create our conda env
COPY env.yml .
RUN conda env create -f env.yml

# I have no idea why we have to run this again
RUN apt-get update
# install make, etc
RUN apt-get install -y build-essential
RUN apt-get install -y git clang

# Create a group and user, then run future commands as this user; we copy
# the source code into this user's home directory before becoming the user
# so that we can make the user own it while we're still root
RUN groupadd -g 999 appuser && \
    useradd -m -r -u 999 -g appuser appuser
# COPY . /home/appuser/lzbench
# RUN chown -R appuser:appuser /home/appuser/lzbench
USER appuser

WORKDIR /home/appuser/
#RUN git clone https://github.com/dblalock/lzbench.git
RUN git clone https://github.com/Devon-MacNeil/testcompress.git
WORKDIR /home/appuser/lzbench
RUN make clean && make

RUN bash -c 'conda init bash'
RUN echo "conda activate myenv" >> ~/.bashrc
CMD ["/bin/bash"]
