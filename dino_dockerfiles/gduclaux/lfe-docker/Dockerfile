# Pull base image.

FROM gduclaux/lfe-docker-dependencies

MAINTAINER Guillaume Duclaux

WORKDIR /build

RUN git clone https://github.com/gduclaux/lfe_notebook.git

ENV TINI_VERSION v0.8.4

ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/local/bin/tini

RUN chmod +x /usr/local/bin/tini

RUN mkdir /root/.ipython

RUN mkdir /workspace && \
  mkdir /workspace/volume

# Copy test files to workspace

RUN cp -av /build/* /workspace/

# setup space for working in

VOLUME /workspace/volume

# launch notebook

WORKDIR /workspace

EXPOSE 8888

ENTRYPOINT ["/usr/local/bin/tini","--"]

CMD jupyter notebook --ip=0.0.0.0 --no-browser --NotebookApp.token='' --allow-root --NotebookApp.iopub_data_rate_limit=1.0e10
