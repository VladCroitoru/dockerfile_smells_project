FROM ros:noetic-ros-core

SHELL ["/bin/bash", "-c"]

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        python3-pip \
        libgl1-mesa-dev \
        ros-noetic-cv-bridge \
        ros-noetic-tf* && \
    apt-get clean &&  \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir \
        torch \
        opencv-python \
        tqdm

WORKDIR /root
CMD ["/bin/bash"]