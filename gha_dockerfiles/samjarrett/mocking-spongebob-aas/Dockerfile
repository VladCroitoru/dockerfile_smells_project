FROM public.ecr.aws/sam/build-python3.9

WORKDIR /deps

COPY requirements.txt /tmp/
RUN set -xe && \
    pip install -r /tmp/requirements.txt -t . && \
    find . -name __pycache__ -type d | xargs rm -rf && \
    rm -rf bin *.dist-info && \
    true
