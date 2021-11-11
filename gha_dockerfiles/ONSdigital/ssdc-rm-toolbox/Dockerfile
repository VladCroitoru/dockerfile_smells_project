FROM python:3.9-slim

RUN pip install pipenv

COPY .bashrc_extras /tmp

RUN apt-get update && apt-get -yq install curl && apt-get -yq install jq && apt-get -yq install vim-tiny && \
    apt-get -yq install unzip && apt-get -yq install postgresql-client || true && \
    apt-get -yq install openssh-client || true && apt-get -yq install procps || true && \
    apt-get -yq clean && groupadd --gid 1000 toolbox && \
    useradd --create-home --system --uid 1000 --gid toolbox toolbox && \
    cat /tmp/.bashrc_extras >> /home/toolbox/.bashrc && rm /tmp/.bashrc_extras
WORKDIR /home/toolbox

COPY Pipfile* /home/toolbox/
RUN pipenv install --system --deploy
USER toolbox

RUN mkdir /home/toolbox/.postgresql && mkdir /home/toolbox/.postgresql-rw

COPY --chown=toolbox . /home/toolbox