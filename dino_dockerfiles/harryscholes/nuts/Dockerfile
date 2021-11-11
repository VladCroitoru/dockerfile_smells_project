FROM alpine:latest
MAINTAINER Harry Scholes <@harryscholes>

ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH

WORKDIR /home
COPY conda_environment.yml install.sh setup.py nuts/
COPY nuts nuts/nuts/

RUN apk --no-cache add tini

RUN apk --no-cache add --virtual build-dependencies \
    bash \
    curl \
    ca-certificates \
    libstdc++ \
    glib \
    && curl "https://raw.githubusercontent.com/sgerrand/alpine-pkg-glibc/master/sgerrand.rsa.pub" -o /etc/apk/keys/sgerrand.rsa.pub \
    && curl -L "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.23-r3/glibc-2.23-r3.apk" -o glibc.apk \
    && apk add glibc.apk \
    && curl -L "https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.23-r3/glibc-bin-2.23-r3.apk" -o glibc-bin.apk \
    && apk add glibc-bin.apk \
    && curl -L "https://github.com/andyshinn/alpine-pkg-glibc/releases/download/2.25-r0/glibc-i18n-2.25-r0.apk" -o glibc-i18n.apk \
    && apk add --allow-untrusted glibc-i18n.apk \
    && /usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8 \
    && /usr/glibc-compat/sbin/ldconfig /lib /usr/glibc/usr/lib \
    && rm -rf glibc*apk && \
    mkdir -p $CONDA_DIR && \
    curl -L https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh -o miniconda.sh && \
    /bin/bash miniconda.sh -f -b -p $CONDA_DIR && \
    rm miniconda.sh && \
    conda install numpy networkx scipy pytables nomkl && \
    conda upgrade -y pip && \
    conda clean -a && \
    pip install -e nuts && \
    apk del build-dependencies

ENTRYPOINT ["/sbin/tini", "--"]
ENV VOLUME /home/volume
CMD ["python"]
