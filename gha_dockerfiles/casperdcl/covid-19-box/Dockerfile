FROM python:3.7-slim
LABEL maintainer.name="Casper da Costa-Luis" \
      maintainer.email="casper.dcl@physics.org" \
      repository.url="https://github.com/casperdcl/covid-19-box"
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update -qq && apt-get install -yqq \
 git gcc \
 && apt-get purge && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY src/requirements-gist.txt .
RUN pip install -r requirements-gist.txt && pip cache purge && rm requirements-gist.txt

WORKDIR /wdir
COPY dvc.yaml *.dvc *.py README.md ./
COPY src src
COPY .dvc .dvc
RUN chmod +x src/script.sh
ENTRYPOINT ["/wdir/src/script.sh"]
