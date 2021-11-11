FROM python:2.7
MAINTAINER platform@counsyl.com

ENV PBR_DIR /pbr
WORKDIR $PBR_DIR

COPY setup.py $PBR_DIR/
COPY setup.cfg $PBR_DIR/

CMD ["python", "setup.py", "--version"]
