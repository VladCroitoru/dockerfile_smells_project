FROM ubuntu:latest
RUN apt update && apt upgrade -y
RUN apt install -y git mercurial build-essential libssl-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl
RUN groupadd -g 1000 python
RUN useradd -u 1000 -g 1000 -m python -s /bin/bash -d /home/python
ENV PYENV_ROOT /home/python/.pyenv
ENV PATH /home/python/.pyenv/shims:/home/python/.pyenv/bin:${PATH}
USER python
WORKDIR /home/python/
RUN curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash
RUN pyenv install 3.6.4 && pyenv global 3.6.4
COPY . /home/python/amigo_investidor
USER root
RUN chown -R 1000:1000 .
USER python
WORKDIR /home/python/amigo_investidor
ENV LANG C.UTF-8
EXPOSE 8080
CMD make run_daemons
