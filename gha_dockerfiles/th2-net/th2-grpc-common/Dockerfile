FROM gradle:6.8.2-jdk11 as java_generator
WORKDIR /home/project
ARG nexus_url
ARG nexus_user
ARG nexus_password

COPY ./ .
RUN ./gradlew clean build publish \
    -Pnexus_url=${nexus_url} \
    -Pnexus_user=${nexus_user} \
    -Pnexus_password=${nexus_password}

FROM python:3.8-slim as python_generator
ARG pypi_repository_url
ARG pypi_user
ARG pypi_password

WORKDIR /home/project
COPY --from=java_generator /home/project .
RUN pip install -r requirements.txt && \
    pip install twine && \
    python setup.py generate && \
    python setup.py sdist && \
    twine upload --repository-url ${pypi_repository_url} --username ${pypi_user} --password ${pypi_password} dist/*
