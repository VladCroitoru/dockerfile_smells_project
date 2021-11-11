FROM lukovkin/dockerfile-mkl-keras

RUN source activate keras \
  && conda install -y \
    jupyter \
    matplotlib \
    seaborn

VOLUME /notebook
WORKDIR /notebook
EXPOSE 8888
CMD source activate keras \
  && jupyter notebook --no-browser --ip=0.0.0.0
