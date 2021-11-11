FROM python:3
MAINTAINER https://github.com/JacobCallahan

RUN mkdir apix
COPY / /apix/
RUN cd /apix && python3 setup.py install

WORKDIR /apix

ENTRYPOINT ["apix"]
CMD ["--help"]
