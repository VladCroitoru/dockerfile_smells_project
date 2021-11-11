################################################################################
# requirements: stage for generating requirements.txt
FROM acidrain/python-poetry:3.10-slim as requirements

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
WORKDIR /root

# generate requirements.txt from poerty.lock, pyproject.toml (only productions)
COPY poetry.lock pyproject.toml ./
RUN poetry export -f requirements.txt --output /root/requirements.txt

################################################################################
# production: stage for production release
FROM python:3.10.0-slim-bullseye as production

# surpress block buffering for stdout and stderr
# see also: https://docs.python.org/ja/3/using/cmdline.html#envvar-PYTHONUNBUFFERED
ENV PYTHONUNBUFFERED=1

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
WORKDIR /app

RUN --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt/lists \
    apt-get update && \
    apt-get install -y --no-install-recommends tzdata=2021a-\* libpq5=13.4\* libffi7=3.3\* libssl1.1=1.1.1\* && \
    apt-get clean

# copy requirements.txt from the requirements stage
COPY --from=requirements /root/requirements.txt ./

# using cache mount (needs BuildKit)
# see also: https://pythonspeed.com/articles/docker-cache-pip-downloads/
RUN --mount=type=cache,target=/root/.cache \
    --mount=type=cache,target=/var/cache/apt \
    --mount=type=cache,target=/var/lib/apt/lists \
    apt-get install -y --no-install-recommends build-essential=12.\* libpq-dev=13.4\* libffi-dev=3.3\* && \
    pip install -r requirements.txt && \
    apt-get remove --purge -y build-essential libpq-dev libffi-dev && \
    apt-get autoremove -y && \
    find / -type d -name __pycache__ | xargs rm -rf

COPY ./manage.py ./entrypoint.sh /app/
COPY ./momoichigo/ /app/momoichigo/

CMD ["/bin/sh", "/app/entrypoint.sh"]
