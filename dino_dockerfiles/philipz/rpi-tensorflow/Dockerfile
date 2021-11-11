FROM resin/rpi-raspbian
MAINTAINER Philpz <philipzheng@gmail.com>

ENV QEMU_EXECVE 1
COPY qemu/cross-build-end qemu/cross-build-start qemu/qemu-arm-static qemu/sh-shim /usr/bin/
RUN [ "cross-build-start" ]
ENV LC_ALL=C.UTF-8
RUN apt-get update -y && apt-get install -y python-pip python-dev wget vim gcc g++ gfortran libatlas-base-dev cython \
	libfreetype6-dev libpng12-dev pkg-config python-scipy
RUN wget --no-check-certificate https://github.com/samjabrahams/tensorflow-on-raspberry-pi/raw/master/bin/tensorflow-0.8.0-cp27-none-linux_armv7l.whl && pip install tensorflow-0.8.0-cp27-none-linux_armv7l.whl && rm tensorflow-0.8.0-cp27-none-linux_armv7l.whl
RUN apt-get remove python-pip && apt-get autoremove
RUN wget https://bootstrap.pypa.io/get-pip.py && \
    python get-pip.py && \
    rm get-pip.py

RUN pip --no-cache-dir install \
        scikit-learn \
        ipykernel \
        jupyter \
        matplotlib \
        && \
    python -m ipykernel.kernelspec
RUN [ "cross-build-end" ]

COPY jupyter_notebook_config.py /root/.jupyter/
COPY notebooks /notebooks
COPY run_jupyter.sh /

# TensorBoard
EXPOSE 6006
# IPython
EXPOSE 8888

WORKDIR "/notebooks"

CMD ["/run_jupyter.sh"]
