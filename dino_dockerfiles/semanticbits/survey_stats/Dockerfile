FROM frolvlad/alpine-miniconda3

RUN apk update \
    && apk add  --no-cache \
        bash \
        zsh \
		coreutils

RUN mkdir /app
WORKDIR /app

COPY . .

ENV PYTHONUNBUFFERED 1
ENV MALLOC_MMAP_THRESHOLD_ 1000000
ENV MALLOC_MMAP_MAX_ 262144
ENV MALLOC_MXFAST_ 0

SHELL ["/bin/bash", "-c"]

RUN conda config --set always_yes yes --set changeps1 no \
    && conda install -n root _license \
    && conda update -y -q conda \
    && conda info -a \
    && conda config --add channels intel \
    && conda create -q -n pydev -c intel/label/test \
            python=3 r-base=3.4 libiconv \
            pandas scikit-learn cython \
            r-feather r-survival r-dbi \
    && conda clean --all

SHELL ["/bin/bash", "-c", "source activate pydev"]

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && R --vanilla -e 'install.packages(c("survey"), repos="http://r-forge.r-project.org")' \
    && pip install --no-cache-dir -e .
