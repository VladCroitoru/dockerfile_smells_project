FROM gcc
RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN chmod +x Miniconda3-latest-Linux-x86_64.sh 
RUN ./Miniconda3-latest-Linux-x86_64.sh -p /opt/conda -b
ENV PATH="/opt/conda/bin:${PATH}"
RUN conda update -n base conda
COPY env.txt /tmp/env.txt
RUN conda env create -f=/tmp/env.txt -n kelp
CMD ["/opt/conda/envs/kelp/bin/ipcluster", "start", "--n=10"]
