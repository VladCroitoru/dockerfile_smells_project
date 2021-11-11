FROM python:3-onbuild
MAINTAINER funkydorian

RUN mkdir /etugra

COPY ./etugra.py /tmp

VOLUME /etugra
VOLUME /timestamps
VOLUME /log
WORKDIR /etugra

CMD python -m pip install zeep
ENV  PYTHONPATH .:/usr/local/lib/python3.5

CMD ["python","/tmp/etugra.py","-t"]

