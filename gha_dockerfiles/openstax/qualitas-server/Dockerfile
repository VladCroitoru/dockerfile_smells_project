FROM python:3.7-alpine as base

# Install base packages
RUN apk add --update --no-cache --virtual .build-deps gcc g++ postgresql-dev curl \
    libffi-dev tini yaml-dev python3-dev py3-psutil linux-headers musl-dev openssl-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools && \
    rm -rf /var/cache/apk/*

# Install rustup for installing cryptography
RUN curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

FROM base as builder

WORKDIR /app

COPY ["requirements.txt", "/app"]

# create Virtualenv
RUN python -m venv /opt/venv && \
  . /opt/venv/bin/activate && \
  pip install --no-cache-dir -U pip

# Set cargo path so cryptography can install w/o errors
RUN . /opt/venv/bin/activate && \
    source $HOME/.cargo/env && \
    pip install -r requirements.txt

FROM builder as runner

# copy everything from /opt
COPY --from=builder /opt/venv /opt/venv

# Set the application environment
ENV PYTHONIOENCODING utf_8
ENV PYTHONPATH /app:$PYTHONPATH
ENV PATH="/app/bin:${PATH}"
ENV FLASK_APP=/app/wsgi.py
# make sure we use the virtualenv
ENV PATH="/opt/venv/bin:$PATH"

COPY . .

RUN chmod +x bin/docker-entrypoint.sh

CMD ["bin/docker-entrypoint.sh", "wsgi:app"]
