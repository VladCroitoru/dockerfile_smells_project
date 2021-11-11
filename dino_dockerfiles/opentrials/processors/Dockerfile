FROM python:2.7
WORKDIR /service
ARG SOURCE_COMMIT
ENV SOURCE_COMMIT ${SOURCE_COMMIT}
COPY requirements.txt requirements.txt
COPY Makefile Makefile
COPY processors processors

RUN pip install -r requirements.txt
