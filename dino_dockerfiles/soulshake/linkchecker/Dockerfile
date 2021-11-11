FROM python:2.7

RUN pip install --upgrade pip \
    && pip install \
        requests==2.9.0 \
        linkchecker

COPY . /src
WORKDIR /src
CMD ["--help"]
ENTRYPOINT ["_bin/linkchecker"]
