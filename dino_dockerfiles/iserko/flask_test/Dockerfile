FROM python:2.7.13

ENV PYTHONPATH=/home/user/code/src

COPY requirements.txt /tmp/requirements.txt

RUN useradd -ms /bin/bash user && \
    pip install -r /tmp/requirements.txt && \
    rm -f /tmp/requirements.txt

COPY . /home/user/code

WORKDIR /home/user/code

RUN python -m compileall -f src

USER user