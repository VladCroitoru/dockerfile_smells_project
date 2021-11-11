FROM lukovkin/dockerfile-cuda-keras

RUN source activate keras \
  && conda install -y \
    jupyter \
    matplotlib \
    seaborn

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888
