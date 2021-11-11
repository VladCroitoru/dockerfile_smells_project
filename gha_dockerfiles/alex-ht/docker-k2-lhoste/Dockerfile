FROM nvcr.io/nvidia/pytorch:21.06-py3
# Install prerequisites
RUN pip install cmake
# Install k2
WORKDIR /opt
RUN git clone https://github.com/k2-fsa/k2.git \
    && cd k2 \
    && K2_MAKE_ARGS="-j2" python3 setup.py install
# Install lhoste
RUN pip install git+https://github.com/lhotse-speech/lhotse
RUN git clone https://github.com/k2-fsa/icefall \
    && cd icefall \
    && pip install -r requirements.txt
ENV PYTHONPATH=/opt/icefall:$PYTHONPATH
WORKDIR /opt/icefall