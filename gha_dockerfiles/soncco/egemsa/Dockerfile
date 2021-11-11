FROM python:3.9
ENV PYTHONUNBUFFERED=1

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash -
RUN apt-get update --allow-releaseinfo-change \
  && apt-get install -y locales \
  && sed -i -e 's/# es_PE.UTF-8 UTF-8/es_PE.UTF-8 UTF-8/' /etc/locale.gen \
  && dpkg-reconfigure --frontend=noninteractive locales \
  && apt-get install -y nodejs \
  && apt-get install -y vim

ENV LANG pt_BR.UTF-8
ENV LC_ALL es_PE.UTF-8

RUN mkdir /code
WORKDIR /code

COPY ["requirements.txt", "/code/"]
RUN pip install -r requirements.txt

COPY ["package.json", "/code/"]

RUN npm install

COPY ["src", "/code/src"]

RUN npm run stylus

COPY [".", "/code/"]