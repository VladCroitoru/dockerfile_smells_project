## base image
FROM python:3.8.2-slim-buster AS compile-image

## install dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc

## virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

## add and install requirements
RUN pip install --upgrade pip && pip install pip-tools
COPY ./requirements.txt .
RUN pip install -r requirements.txt

## base image
FROM python:3.8.2-slim-buster AS runtime-image

ENV APP_UID=9999
ENV APP_GID=9999
ENV APP_HOME=/usr/src/app
ENV APP_USER wfuser

## copy Python dependencies from build image
COPY --from=compile-image /opt/venv /opt/venv

## add user/group
RUN addgroup --system --gid $APP_GID $APP_USER \
    && adduser --system --no-create-home -u $APP_UID --group $APP_USER \
    && mkdir -p $APP_HOME \
    && chown -R $APP_UID:$APP_GID $APP_HOME \
    && chmod -R 755 $APP_HOME

WORKDIR $APP_HOME
USER $APP_USER
COPY ./ ./

## set python environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/opt/venv/bin:$PATH"

CMD python ./main.py
