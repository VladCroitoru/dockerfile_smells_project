FROM ivukotic/ml_base:latest

LABEL maintainer Ilija Vukotic <ivukotic@cern.ch>

#############################
# Python 3 packages
#############################

RUN pip3 --no-cache-dir install \
    h5py \
    tables \
    ipykernel \
    metakernel \
    jupyter \
    jupyterlab \
    matplotlib \
    numpy \
    pandas \
    scipy \
    sklearn \
    qtpy \
    tensorflow \
    keras 

RUN python3 -m ipykernel.kernelspec

# build info
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt

COPY app/entrypoint.sh /entrypoint.sh
COPY app/gan.py /gan.py

RUN chmod 755 /entrypoint.sh

#execute
CMD ["/entrypoint.sh"] 