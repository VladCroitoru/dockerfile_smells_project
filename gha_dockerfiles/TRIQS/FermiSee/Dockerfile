FROM ubuntu:21.04

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
      g++ \
      git \
      make \
      cmake \
      sudo \
      hdf5-tools \
      libboost-dev \
      liblapack-dev \
      libfftw3-dev \
      libgmp-dev \
      libhdf5-dev \
      libopenmpi-dev \
      gunicorn \
      python3-dev \
      python3-mako \
      python3-numpy \
      python3-scipy \
      python3-mpi4py \
      python3-pip \
      python3-plotly \ 
      python3-skimage \
      python3-gunicorn \
      python3-pandas \
      python3-flask \ 
      libpython3-dev \
      && \
      apt-get autoremove --purge -y && \
      apt-get autoclean -y && \
      rm -rf /var/cache/apt/* /var/lib/apt/lists/*

# Install Python dependencies.
RUN pip3 install dash dash-daq dash-bootstrap-components dash-extensions

# triqs
RUN cd / && mkdir -p source \
    && cd /source && git clone -b unstable https://github.com/TRIQS/triqs triqs.src \
    && mkdir -p triqs.build && cd triqs.build \
    && cmake ../triqs.src -DCMAKE_INSTALL_PREFIX=/usr/local -DMPIEXEC_PREFLAGS='--allow-run-as-root' \
    && make -j8 && make install \
    && rm -rf /source

ENV PYTHONPATH=/usr/local/lib/python3.9/site-packages:${PYTHONPATH} \
    TRIQS_ROOT=/usr/local

RUN useradd -m triqs
USER triqs
WORKDIR /home/triqs

# Create a working directory.
RUN mkdir /home/triqs/fermisee
WORKDIR /home/triqs/fermisee

# Copy the rest of the codebase into the image
COPY . ./

# Finally, run gunicorn.
# CMD [ "gunicorn", "--workers=4", "--threads=1", "-b 0.0.0.0:9375", "app:server"]
# or run in debug mode
CMD ["python3", "app.py"]
