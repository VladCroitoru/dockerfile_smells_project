FROM python:3.8

EXPOSE 7878

# list of comma separated strings
ENV MODULES="\
    git+https://gitlab.com/papertext/papertext_auth \
    git+https://gitlab.com/PaperText/papertext_docs \
"

ENV PT__auth__hash__algo="argon2"
ENV PT__log_level="INFO"

RUN mkdir ~/.papertext

RUN apt-get update
RUN apt-get install --no-install-recommends -y \
    build-essential \
    libmpc-dev
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

RUN python3.8 -m pip install --upgrade pip
RUN python3.8 -m pip install --upgrade setuptools

WORKDIR /root

COPY README.md      ./paperback/
COPY LICENSE        ./paperback/
COPY pyproject.toml ./paperback/
COPY src/paperback  ./paperback/src/paperback
RUN python3.8 -m pip install ./paperback

COPY src/container/install_deps.sh ./install_deps.sh
# RUN ./install_deps.sh

# COPY src/container/entrypoint.sh ./entrypoint.sh
# CMD sh ~/entrypoint.sh

CMD ./install_deps.sh && paperback
