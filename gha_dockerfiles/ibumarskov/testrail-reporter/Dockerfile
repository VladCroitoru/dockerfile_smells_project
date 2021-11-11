FROM python:3
LABEL maintainer="Ilya Bumarskov <bumarskov@gmail.com>"

COPY testrail_reporter /testrail-reporter/testrail_reporter
COPY README.md /testrail-reporter/
COPY requirements.txt /testrail-reporter/
COPY setup.py /testrail-reporter/

WORKDIR /testrail-reporter

RUN python3 setup.py install
