FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu16.04
MAINTAINER Deepak Roy Chittajallu <deepk.chittajallu@kitware.com>

# Install system pre-requisites
RUN apt-get update && \
    apt-get install -y \
    build-essential wget git \
    libcupti-dev && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Build path for libraries
ENV BUILD_PATH /build

# Install miniconda
RUN mkdir -p $BUILD_PATH && \
    wget https://repo.continuum.io/miniconda/Miniconda-latest-Linux-x86_64.sh \
    -O $BUILD_PATH/install_miniconda.sh && \
    bash $BUILD_PATH/install_miniconda.sh -b -p $BUILD_PATH/miniconda && \
    rm $BUILD_PATH/install_miniconda.sh && \
    chmod -R +r $BUILD_PATH && \
    chmod +x $BUILD_PATH/miniconda/bin/python
ENV PATH $BUILD_PATH/miniconda/bin:${PATH}

# Download and install slicer_cli_web
RUN cd $BUILD_PATH && \
    conda install --yes -c cdeepakroy ctk-cli=1.4.1 && \
    git clone https://github.com/girder/slicer_cli_web.git && \
    cd slicer_cli_web && \
    find . -depth -name .git -exec rm -rf '{}' \;                   

# Copy cnn-image-classification files
ENV cnn_image_classification_path $PWD/cnn-image-classification
RUN mkdir -p $cnn_image_classification_path
COPY . $cnn_image_classification_path
WORKDIR $cnn_image_classification_path
RUN pip install --ignore-installed --upgrade pip setuptools && \
    pip install -U -r requirements.txt && \
    cd ClassifyImage && \
    bash cache_pretrained_models.sh

# Set entrypoint
ENTRYPOINT ["/build/miniconda/bin/python", "/build/slicer_cli_web/server/cli_list_entrypoint.py"]
