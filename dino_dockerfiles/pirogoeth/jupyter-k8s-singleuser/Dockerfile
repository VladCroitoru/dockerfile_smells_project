ARG JUPYTER_NOTEBOOK_BASE=27ba57364579

FROM jupyter/minimal-notebook:${JUPYTER_NOTEBOOK_BASE}
LABEL maintainer="Sean Johnson <pirogoeth@maio.me>"

ARG GOLANG_VERSION=1.9.1
ARG JUPYTERHUB_VERSION=0.8.1

USER root
RUN apt-get update && \
        apt-get install -fy pkg-config libzmq5 libzmq3-dev git wget && \
        apt-get install -fy texlive texlive-science texlive-xetex && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists /var/cache/apt

USER jovyan
ENV GOROOT=/home/jovyan/.go/go
ENV GOPATH=/home/jovyan/.go
ENV PATH=$PATH:$GOROOT/bin:$GOPATH/bin

RUN pip install --no-cache jupyterhub==${JUPYTERHUB_VERSION} && \
        pip install -U pip numpy pandas scikit-learn \
        scipy enum-compat matplotlib requests Jinja2 \
        ipykernel ipython ipython-genutils ipywidgets \
        MarkupSafe msgpack-python ordered-set keras \
        tensorflow jupyter_dashboards nltk twitter \
        vapeplot
RUN wget -L -O golang.tgz https://storage.googleapis.com/golang/go${GOLANG_VERSION}.linux-amd64.tar.gz && \
        mkdir -p $GOROOT && \
        tar xzvf golang.tgz -C $GOPATH && \
        rm golang.tgz && \
        go get github.com/gopherdata/gophernotes && \
        mkdir -p $(jupyter --data-dir)/kernels/gophernotes && \
        cp -rv $GOPATH/src/github.com/gopherdata/gophernotes/kernel/* $(jupyter --data-dir)/kernels/gophernotes/

# Configure container startup
ENTRYPOINT ["tini", "--"]
CMD ["start-singleuser.sh"]
