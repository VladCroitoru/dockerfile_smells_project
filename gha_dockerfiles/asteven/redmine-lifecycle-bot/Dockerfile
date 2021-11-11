# Dockerfile based on ideas from https://pythonspeed.com/

FROM docker.io/python:3.9-slim AS compile-image

LABEL maintainer "Steven Armstrong <steven@armstrong.cc>"

RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential gcc

ENV VIRTUAL_ENV=/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Install python packages into virtual env.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Dumb-init as pid 1.
RUN pip install dumb-init


FROM docker.io/python:3.9-slim AS runtime-image

COPY --from=compile-image /venv /venv

# Install runtime dependencies.
COPY redmine-lifecycle-bot /venv/bin
RUN chmod +x /venv/bin/redmine-lifecycle-bot

RUN useradd redmine-bot
USER redmine-bot

# Ensure exectutables from virtualenv are prefered.
ENV PATH "/venv/bin:${PATH}"
ENTRYPOINT ["/venv/bin/dumb-init", "--", "redmine-lifecycle-bot"]
