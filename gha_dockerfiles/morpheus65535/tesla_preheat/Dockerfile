FROM python:3-alpine

# set python to use utf-8 rather than ascii.
ENV PYTHONIOENCODING="UTF-8"

# Make sure Python output to stdout appear in realtime
ENV PYTHONUNBUFFERED=0

RUN apk add --update --no-cache tzdata git py3-pip python3-dev && \
    git clone -b main --single-branch https://github.com/morpheus65535/tesla_preheat.git /tesla && \
    pip3 install -r /tesla/requirements.txt

CMD ["python", "/tesla/tesla.py"]