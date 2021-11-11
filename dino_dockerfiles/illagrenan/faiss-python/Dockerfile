# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Stage 1
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
FROM nvidia/cuda:8.0-devel-ubuntu16.04 as builder
LABEL authors="Vašek Dohnal <vaclav.dohnal@gmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends software-properties-common && add-apt-repository ppa:deadsnakes/ppa -y
RUN apt-get update && apt-get install -y --no-install-recommends \
    libopenblas-dev \
    python3.6 \
    python3.6-dev \
    swig \
    git \
    wget \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN curl https://bootstrap.pypa.io/get-pip.py | python3.6
RUN pip3.6 install --no-input --upgrade --no-cache-dir pip setuptools wheel
RUN pip3.6 install --isolated --no-input --compile --exists-action=a --disable-pip-version-check --use-wheel --no-cache-dir matplotlib numpy

WORKDIR /opt

RUN python3.6 -c "import distutils.sysconfig; print(distutils.sysconfig.get_python_inc())"
RUN python3.6 -c "import numpy ; print(numpy.get_include())"
RUN git clone --depth=1 https://github.com/facebookresearch/faiss .

COPY ./makefile.inc ./makefile.inc

RUN make tests/test_blas -j $(nproc) && \
    make -j $(nproc) && \
    make demos/demo_sift1M -j $(nproc) && \
    make py

RUN cd gpu && \
    make -j $(nproc) && \
    make test/demo_ivfpq_indexing_gpu && \
    make py

RUN python3.6 -c "import faiss; print(dir(faiss))"

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Stage 2
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
FROM illagrenan/ubuntu1604-python36

RUN apt-get update && apt-get install -y --no-install-recommends \
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip3.6 install --isolated --no-input --compile --exists-action=a --disable-pip-version-check --use-wheel --no-cache-dir numpy

RUN mkdir -p /opt/faiss

# https://github.com/facebookresearch/faiss/blob/master/INSTALL.md#python
COPY --from=builder /opt/swigfaiss.py /opt/faiss/
COPY --from=builder /opt/swigfaiss_gpu.py /opt/faiss/
COPY --from=builder /opt/faiss.py /opt/faiss/

COPY --from=builder /opt/_swigfaiss.so /opt/faiss/
COPY --from=builder /opt/_swigfaiss_gpu.so /opt/faiss/

ENV PYTHONPATH $PYTHONPATH:/opt/faiss
ENV BLASLDFLAGS /usr/lib/libopenblas.so.0

RUN python3.6 -c "import faiss; print(dir(faiss))"
