# planemo
#
# VERSION       0.1.0

FROM python:2.7.13

LABEL maintainer "Manabu ISHII <manabu.ishii.rb@gmail.com>"

ENV DEBIAN_FRONTEND noninteractive

RUN pip install git+https://github.com/galaxyproject/planemo.git@0.55.0

ENV GALAXY_TEST_UPLOAD_ASYNC false
ENV GALAXY_TEST_DEFAULT_INTERACTOR api
ENV GALAXY_TEST_PORT 7777

WORKDIR /galaxy-central
ENTRYPOINT ["planemo"]
CMD ["--help"]
