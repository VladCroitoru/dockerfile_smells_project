FROM python:slim

RUN  pip --no-cache-dir install --user poetry poethepoet nodeenv
RUN python -m nodeenv --force --clean-src /root/.local
RUN find /root/.local -name __pycache__ -prune -exec rm -rf {} \;

RUN apt update && apt --yes --no-install-recommends install make && rm -rf /var/lib/apt/lists/*

FROM python:slim

COPY --from=0 /usr/bin/make /usr/bin/make

RUN adduser --disabled-password --gecos "" dock

USER dock

ENV HOME=/home/dock
COPY --from=0 --chown=dock:dock /root/.local ${HOME}/.local

RUN mkdir ${HOME}/app
WORKDIR ${HOME}/app

ENV PATH=${PATH}:${HOME}/.local/bin
ENV POETRY_VIRTUALENVS_CREATE=false

CMD bash
