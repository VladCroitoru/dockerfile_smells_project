FROM python:3.10.0-alpine3.14

RUN /usr/sbin/adduser -g python -D python

USER python
RUN /usr/local/bin/python -m venv /home/python/venv

ENV PATH="/home/python/venv/bin:${PATH}" \
    PYTHONUNBUFFERED="1"

COPY --chown=python:python requirements.txt /home/python/docker-pelican/requirements.txt
RUN /home/python/venv/bin/pip install --no-cache-dir --requirement /home/python/docker-pelican/requirements.txt

WORKDIR /pelican-site

ENTRYPOINT ["/home/python/venv/bin/pelican"]

LABEL org.opencontainers.image.authors="William Jackson <william@subtlecoolness.com>" \
      org.opencontainers.image.source="https://github.com/williamjacksn/docker-pelican"
