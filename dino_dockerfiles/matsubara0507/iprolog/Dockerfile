FROM python:latest

ENV HOME /root
WORKDIR $HOME

RUN pip install ipython jupyter

# Prolog

RUN apt-get update && apt-get install -y --no-install-recommends \
    gprolog \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

WORKDIR $HOME/iprolog
ADD . $HOME/iprolog
RUN cd kernels && jupyter kernelspec install prolog

EXPOSE 8888

CMD ["jupyter", "notebook", "--no-browser", "--allow-root", "--ip='*'"]
