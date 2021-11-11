FROM continuumio/anaconda3

MAINTAINER Umit Yoruk <umityoruk@gmail.com>

# Install opencv dependencies (needed for building opencv)
RUN apt-get update && apt-get install -y build-essential \
    cmake \
    git \
    libgtk2.0-dev \
    pkg-config \
    libavcodec-dev \
    libavformat-dev \
    libswscale-dev

# Install opencv
RUN cd /tmp && \
    curl -O -J -L https://github.com/opencv/opencv/archive/3.4.0.tar.gz && \
    tar -xzvf opencv-3.4.0.tar.gz && \
    mkdir opencv-3.4.0/build && \
    cd /tmp/opencv-3.4.0/build && \
    cmake -D CMAKE_BUILD_TYPE=RELEASE \
          -D CMAKE_INSTALL_PREFIX=/opt/opencv \
          -D INSTALL_PYTHON_EXAMPLES=OFF \
          -D INSTALL_C_EXAMPLES=OFF \
          -D PYTHON_EXECUTABLE=/opt/conda/bin/python \
          -D BUILD_EXAMPLES=OFF .. && \
    make -j4 && make install && rm -r /tmp/*

# Setup anaconda3 packages
RUN pip install pydicom && \
    jupyter nbextension enable --py --sys-prefix widgetsnbextension

# Setup miniconda3 packages (Uncomment below if the base is continuumio/miniconda3)
# RUN conda install -y numpy=1.13 matplotlib jupyter scipy scikit-image scikit-learn h5py && \

# Build renal segmentation code 
RUN git clone https://github.com/umityoruk/renal-segmentation.git && \
    cd renal-segmentation/CppSource/GrabCut3d && make

# Start jupyter server
CMD jupyter notebook --notebook-dir=/renal-segmentation/Notebook --ip='*' --port=8888 --no-browser --allow-root

