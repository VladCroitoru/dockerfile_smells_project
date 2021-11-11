# install python image
ARG IMAGE_VERSION=3.9-slim
FROM python:${IMAGE_VERSION}

# install required packages
RUN apt-get -y update --fix-missing
RUN apt-get -y install git gcc curl ncat wait-for-it
RUN python -m pip install --upgrade pip
RUN pip install pipenv

# set application working directory
WORKDIR /app

# copy pipenv data
COPY Pipfile .

# install project dependencies
RUN pipenv lock -v 2>&1
RUN pipenv install --deploy --system

# copy project data
COPY plugin plugin/
COPY scraper scraper/
COPY scripts scripts/
COPY static static/
COPY tor_scraper.py plugin_manager.py ./

# specify build arguments
ARG BUILD_VERSION=unspecified

# set image labels
LABEL maintainer="dolejskad@gmail.com"
LABEL version=${BUILD_VERSION}

# set environment variables
ENV TORSCRAPER_VERSION ${BUILD_VERSION}
ENV TORSCRAPER_ROOT /app

# expose control server port
EXPOSE 8080/tcp
# define volumes
VOLUME ["/app/config", "/app/plugin", "/app/scripts", "/app/data"]

# run application entrypoint script
CMD ["/app/scripts/entrypoint.sh"]
