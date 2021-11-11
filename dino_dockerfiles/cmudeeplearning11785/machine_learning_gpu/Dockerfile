FROM cmudeeplearning11785/machine_learning_gpu_base

#-----------------------------------
# Sphinx
#-----------------------------------
RUN mkdir -p /home/sphinx
WORKDIR /home/sphinx
# Download is currently broken
#RUN wget -O pocketsphinx-5prealpha.tar.gz https://sourceforge.net/projects/cmusphinx/files/pocketsphinx/5prealpha/pocketsphinx-5prealpha.tar.gz/download 
#RUN wget -O sphinxbase-5prealpha.tar.gz https://sourceforge.net/projects/cmusphinx/files/sphinxbase/5prealpha/sphinxbase-5prealpha.tar.gz/download 
#RUN tar xzf pocketsphinx-5prealpha.tar.gz
#RUN tar xzf sphinxbase-5prealpha.tar.gz
ADD pocketsphinx-5prealpha.tar.gz /home/sphinx
ADD sphinxbase-5prealpha.tar.gz /home/sphinx
RUN apt-get install -y autoconf libtool automake bison swig

WORKDIR /home/sphinx/sphinxbase-5prealpha
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install
RUN ldconfig

WORKDIR /home/sphinx/pocketsphinx-5prealpha
RUN ./autogen.sh
RUN ./configure
RUN make
RUN make install
RUN ldconfig

#-----------------------------------
# CTC
#-----------------------------------

RUN pip3 install --upgrade pip

# Decoder
WORKDIR /home/ctc
RUN git clone --recursive https://github.com/parlance/ctcdecode.git
WORKDIR /home/ctc/ctcdecode
RUN pip3 install wget
COPY boost_1_63_0.tar.gz /home/ctc/ctcdecode/third_party/
RUN pip3 install .

# Warp-CTC
RUN apt-get install -y cmake
#RUN git clone https://github.com/torch/distro.git /home/torch --recursive
#RUN cd /home/torch && bash install-deps
#ENV TORCH_NVCC_FLAGS -D__CUDA_NO_HALF_OPERATORS__
#RUN cd /home/torch && ./install.sh
RUN apt-get install -y git cmake tree htop bmon iotop
RUN pip3 install cython
RUN apt-get install -y libffi-dev
WORKDIR /home/ctc
RUN git clone https://github.com/bstriner/warp-ctc.git
WORKDIR /home/ctc/warp-ctc
RUN ldconfig
RUN bash -c -l "cd /home/ctc/warp-ctc && mkdir build && cd build && cmake .. && make && make install"
ENV WARP_CTC_PATH /home/ctc/warp-ctc/build
RUN ldconfig
RUN bash -c -l "cd /home/ctc/warp-ctc/pytorch_binding && python3 setup.py install"
#RUN bash -c -l "cd /home/ctc/warp-ctc/pytorch_binding && pip3 install --global-option=build_ext --global-option=-I/home/ctc/warp-ctc/include ."
#RUN cd pytorch_binding && python3 setup.py install
RUN ldconfig


#-----------------------------------
# Cleanup
#-----------------------------------

WORKDIR /workspace
