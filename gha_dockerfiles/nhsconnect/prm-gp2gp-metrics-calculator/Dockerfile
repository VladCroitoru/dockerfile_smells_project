FROM python:3.9-slim

COPY . /prmcalculator

ARG IMAGE_TAG
ENV BUILD_TAG=${IMAGE_TAG}

RUN cd /prmcalculator && python setup.py install

ENTRYPOINT ["python", "-m", "prmcalculator.pipeline.main"]
