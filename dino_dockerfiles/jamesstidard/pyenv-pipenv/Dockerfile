FROM ubuntu:17.10

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8


# -- pyenv
RUN apt-get update && apt-get install -y \
    git \
    make \
    gcc \
    curl \
    zlib1g-dev \
    bzip2 \
    libbz2-dev \
    libreadline6-dev \
    sqlite \
    libsqlite3-dev \
    openssl \
    libssl-dev
RUN git clone git://github.com/yyuu/pyenv.git .pyenv
ENV PYENV_ROOT /.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH


# -- Adding Pipfiles
ONBUILD COPY Pipfile Pipfile
ONBUILD COPY Pipfile.lock Pipfile.lock


# -- Install appropriate python
ONBUILD RUN VERSION=$(grep "python_full_version" Pipfile | sed 's/^.* = //' | tr -d '"') && \
    pyenv install $VERSION && \
    pyenv global $VERSION && \
    pip install pipenv


# -- Install dependencies:
ONBUILD RUN set -ex && pipenv install --deploy --system
