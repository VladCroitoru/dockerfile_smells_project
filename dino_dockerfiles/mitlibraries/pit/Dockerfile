FROM python:3.5
MAINTAINER Mike Graves <mgraves@mit.edu>

COPY pit /pit/pit
COPY Pipfile* /pit/
COPY LICENSE /pit/
COPY setup.* /pit/

RUN python3.5 -m pip install pipenv

WORKDIR /pit/
RUN pipenv install --system
RUN python3.5 -m pip install .

ENTRYPOINT ["pit"]
CMD ["--help"]
