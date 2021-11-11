FROM python:3.9-slim

ARG LMA_VERSION
ENV LEANPUB_MULTI_ACTION_VERSION $LMA_VERSION
ARG WHEEL_DIR .
ENV WHEEL_DIR $WHEEL_DIR

RUN pip install --no-cache-dir --upgrade pip

WORKDIR /app
COPY $WHEEL_DIR/leanpub_multi_action-$LEANPUB_MULTI_ACTION_VERSION-py3-none-any.whl /app

RUN pip install --no-cache-dir leanpub_multi_action-$LEANPUB_MULTI_ACTION_VERSION-py3-none-any.whl

ENTRYPOINT [ "lma" ]
