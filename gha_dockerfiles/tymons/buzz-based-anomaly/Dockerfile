ARG CUDA_VERSION=10.2
FROM nvidia/cuda:$CUDA_VERSION-base

CMD nvidia-smi

WORKDIR .

ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update

RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*

RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh
RUN conda --version

COPY ./environment.yml /tmp/environment.yml
RUN conda env create --name pytorch-cuda-env -f /tmp/environment.yml
RUN echo "conda activate pytorch-cuda-env" >> ~/.bashrc

ENV PATH /opt/conda/envs/pytorch-cuda-env/bin:$PATH
ENV CONDA_DEFAULT_ENV $pytorch-cuda-env

COPY . /buzz-based-anomaly
WORKDIR /buzz-based-anomaly
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "pytorch-cuda-env", "python", "train.py"]
