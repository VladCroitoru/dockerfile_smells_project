FROM continuumio/miniconda:latest
MAINTAINER David Turanski <dturanski@pivotal.io>
COPY app/* /app/

RUN if [ -f ./app/environment.yml ]; then conda env create --name scst-env --force --file ./app/environment.yml; fi

RUN if [ -f /app/requirements.txt ]; then pip install -r /app/requirements.txt; fi

# If testing a local build of 'springcloudstream', copy the wheel file to lib and uncomment the following lines.
#COPY lib/* ./python-lib
#ENV PYTHONPATH=./python-lib:$PYTHONPATH
CMD ["/bin/bash", "-c", "source activate scst-env && python /app/sentiment-service.py --port=9999 --debug"]