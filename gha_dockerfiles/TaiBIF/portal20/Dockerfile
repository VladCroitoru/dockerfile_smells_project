FROM python:3.8.11-slim

# set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# for Pillow to support jpeg/png
#ENV INCLUDE=/usr/include
#ENV LIBRARY_PATH=/lib:/usr/lib

# update & install system package
RUN apt-get update && apt-get install -y \
    gettext nodejs
#    rm -rf /var/lib/apt/lists/*

# install npm from source
RUN curl https://www.npmjs.com/install.sh -o npm-install.sh
RUN sh npm-install.sh
RUN rm npm-install.sh

# timezone to Asia/Taipei
RUN ln -sf /usr/share/zoneinfo/Asia/Taipei /etc/localtime
RUN echo "Asia/Taipei" > /etc/timezone
ENV TZ=Asia/Taipei

WORKDIR /taibif-code/

# install python package
RUN pip install --upgrade pip
RUN pip install --no-cache-dir pipenv
COPY Pipfile Pipfile.lock ./
RUN pipenv install --system


COPY . /taibif-code/


# install frontend packages
COPY package.json package-lock.json ./
RUN npm install

#RUN npm run build-dev # not working?

# dev
#RUN apk --update add --no-cache postgresql-client

# remove compiling environment `build-dependencies`
#RUN apk del build-dependencies