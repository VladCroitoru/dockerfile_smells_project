FROM osgeo/gdal:ubuntu-small-3.2.1

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    ca-certificates && \
#    libgomp1 python3-pip python3-distutils python3-psycopg2  && \
#    pip3 install --requirement /tmp/requirements.txt && \
#    apt-get purge -y --auto-remove python3-pip && \
    mkdir -p /etc/pki/tls/certs && \
    cp /etc/ssl/certs/ca-certificates.crt /etc/pki/tls/certs/ca-bundle.crt && \
    rm -rf /var/lib/apt/lists/* && \
    useradd -m app

ENV CPL_LOG=/dev/null

USER app

ENV HOME /home/app
ENV CONDA_DIR $HOME/miniconda3
WORKDIR $HOME

RUN curl -s https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh > miniconda.sh && \
    chmod +x $HOME/miniconda.sh && \
    $HOME/miniconda.sh -b -p $CONDA_DIR && \
    rm ~/miniconda.sh

ENV PATH $CONDA_DIR/bin:$PATH
ENV ENV_PATH $HOME/cfsi_env
COPY environment.yml /tmp/

RUN conda env create -p $ENV_PATH --file /tmp/environment.yml --force && \
    conda clean --all --yes

ENV PATH $ENV_PATH/bin:$PATH
