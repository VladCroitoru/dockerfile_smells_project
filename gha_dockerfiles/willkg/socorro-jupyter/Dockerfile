FROM jupyter/scipy-notebook:ubuntu-20.04@sha256:e762555e4d39bd9aa65ddcb710b7ad3b7ea1d363af07d00063fbd699e2c7fba7

COPY requirements.txt /tmp
RUN pip install -U pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

COPY bin/entrypoint.sh /tmp/entrypoint.sh

ENTRYPOINT ["/tmp/entrypoint.sh"]
