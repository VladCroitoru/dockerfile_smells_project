FROM ubuntu:latest

WORKDIR /workspace

ENV HUGO_VERSION='0.88.1'
ENV HUGO_NAME="hugo_extended_${HUGO_VERSION}_Linux-64bit"
ENV HUGO_URL="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/${HUGO_NAME}.deb"
ENV BUILD_DEPS="wget"

ENV BASH_ENV=~/.bashrc

ENV GOPATH /go
ENV PATH $GOPATH/bin:/usr/local/go/bin:$PATH

ENV PATH=/root/miniconda3/bin:${PATH}
ENV PATH /opt/conda/bin:$PATH

ENV QT_QPA_PLATFORM=webgl
ENV GOOGLE_APPLICATION_CREDENTIALS=/workspace/gcp-credentials.json
ENV DISPLAY=:1

RUN apt update \
    && apt install -y wget git libgl1-mesa-glx tar xvfb libxkbcommon-x11-0 libxcb-xinerama0 \
    && rm -rf /var/lib/apt/lists/*

RUN wget -P /tmp https://dl.google.com/go/go1.16.8.linux-amd64.tar.gz \
    && tar -C /usr/local -xzf /tmp/go1.16.8.linux-amd64.tar.gz \
    && rm /tmp/go1.16.8.linux-amd64.tar.gz


RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"

RUN wget "${HUGO_URL}" && \
    apt install "./${HUGO_NAME}.deb" && \
    rm -rf "./${HUGO_NAME}.deb" "${HUGO_NAME}"

RUN wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh

RUN bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm Miniconda3-latest-Linux-x86_64.sh

RUN conda update -y conda

COPY requirements ./requirements

RUN conda env create --file requirements/conda.yml \
    && conda clean --all --yes --quiet

SHELL ["conda", "run", "-n", "odin", "/bin/bash", "-c"]

COPY docker .

ENV CONDA_DEFAULT_ENV=odin
RUN conda init bash \
  && echo 'conda activate odin' >> ~/.bashrc

RUN python requirements/builder.py

COPY . .
ENV GOOS=linux
RUN python requirements/builder.py
CMD xvfb-run --server-args=":1 -screen 0 1920x1080x24" export DISPLAY=:1 && python scripts/godin_all.py
