FROM ubuntu:16.04

# Pick up some TF dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        libfreetype6-dev \
        libhdf5-serial-dev \
        libpng12-dev \
        libzmq3-dev \
        pkg-config \
        python3 \
        python3-dev \
        rsync \
        software-properties-common \
        unzip \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -O https://bootstrap.pypa.io/get-pip.py && \
    python3 get-pip.py && \
    rm get-pip.py

RUN pip3 --no-cache-dir install \
        Pillow \
        h5py \
        ipykernel \
        jupyter \
        matplotlib \
        numpy \
        pandas \
        tqdm \
        scipy \
        sklearn \
        tensorflow


# RUN ln -s -f /usr/bin/python3 /usr/bin/python#

RUN mkdir -p hand-detection/fine_tuned_model/frcnn_inc_v2_aug4

COPY visualization_utils.py /hand-detection
COPY frcnn_inc_v2_aug.config /hand-detection
COPY fine_tuned_model/frcnn_inc_v2_aug4/optimized_inference_graph.pb /hand-detecion/fine_tuned_model/frcnn_inc_v2_aug4/.
COPY detect.py /hand-detection

WORKDIR "/hand-detection"
