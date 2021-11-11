#########
#Builder#
#########
FROM python:3.9-slim-bullseye as build

# Install utils
RUN apt-get update -qq && apt-get install -qq -y \
  gcc \
  libffi-dev \
  g++ \
  && \
  apt-get clean all && rm -rf /var/apt/lists/* && rm -rf /var/cache/apt/*

# Set poetry version and other env vars
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1 \
    BUILDER_HOME=/tmp \
    APP_HOME=/app

# Set directory
WORKDIR $BUILDER_HOME

# Install poetry
RUN pip install poetry

# Copy poetry files
COPY ./pyproject.toml ./poetry.lock $BUILDER_HOME/

RUN poetry config virtualenvs.create false && \
  poetry export --output requirements.txt --without-hashes

#######
#FINAL#
#######

FROM build as final

WORKDIR $APP_HOME

COPY --from=build $BUILDER_HOME/requirements.txt $APP_HOME/requirements.txt

COPY .env $APP_HOME/.env

RUN pip install --no-cache-dir --upgrade -r $APP_HOME/requirements.txt

COPY . $APP_HOME
