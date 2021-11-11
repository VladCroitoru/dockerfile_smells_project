FROM python:3.8 AS base

ENV VIRTUAL_ENV=/opt/venv
# WORKDIR $VIRTUAL_ENV
# RUN chown -R $USER:$USER $VIRTUAL_ENV
# RUN chmod 755 $VIRTUAL_ENV

# USER $USER

RUN pip install --upgrade pip
RUN python3 -m venv $VIRTUAL_ENV

ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY requirements.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements.txt

FROM base AS base-dev
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
COPY requirements-dev.txt .
RUN --mount=type=cache,target=/root/.cache/pip \
    pip install -r requirements-dev.txt

FROM python:3.8-slim AS prod
RUN apt update && apt install curl -y
ENV VIRTUAL_ENV=/opt/venv
COPY --from=base $VIRTUAL_ENV $VIRTUAL_ENV
COPY . /app
WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# check every 5s to ensure this service returns HTTP 200
HEALTHCHECK --interval=10s --timeout=5s --start-period=60s --retries=3 \
    CMD curl -fs http://localhost:5000/api/healthz || exit 1

CMD ["./scripts/run.sh"]

FROM prod as development
ARG USER_ID=1001
ARG GROUP_ID=1001
ARG USER=user

RUN addgroup --gid $GROUP_ID $USER
RUN adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID $USER

RUN mkdir -p /home/user/.config/pudb ; chown -R ${USER_ID}:${GROUP_ID} /home/user/.config/pudb

COPY --from=prod --chown=$USER:$USER /app /app

ENV VIRTUAL_ENV=/opt/venv
COPY --from=base-dev $VIRTUAL_ENV $VIRTUAL_ENV
USER $USER
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
CMD ["./scripts/dev-run.sh"]
