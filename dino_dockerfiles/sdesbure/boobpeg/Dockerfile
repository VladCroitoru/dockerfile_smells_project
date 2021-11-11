FROM python:2-slim
MAINTAINER Sylvain Desbureaux <sylvain@desbureaux.fr>

ARG VCS_REF
ARG BUILD_DATE

LABEL org.label-schema.vcs-ref=$VCS_REF \
      org.label-schema.vcs-url="https://github.com/sdesbure/boobpeg" \
      org.label-schema.name="Boobpeg" \
      org.label-schema.docker.dockerfile="/Dockerfile" \
      org.label-schema.license="MIT" \
      org.label-schema.build-date=$BUILD_DATE

RUN apt-get update && apt-get -y install git-core && apt-get clean


COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "./boobpeg_rest.py"]
CMD ["--config-folder", "/config" ]
