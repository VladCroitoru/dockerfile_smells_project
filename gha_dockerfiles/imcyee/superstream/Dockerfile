FROM node:12.18.1

# Create app directory
WORKDIR /usr/src/app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 8080

# CMD [ "ts-node-dev", "./src/index.ts" ]

# If you are building your code for production
# RUN npm ci --only=production

# # FROM python:3.7-alpine3.12
# FROM python:2.7-alpine3.9

# ENV LIBRARY_PATH=/lib:/usr/lib

# # RUN curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# RUN apk add --no-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ \
#     git zlib-dev jpeg-dev gcc musl-dev postgresql-dev py3-anyjson ruby-bundler py3-pip libjpeg curl && \
#     curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

# WORKDIR /stream

# ADD . /stream



# # ENV PATH="${PATH}:/root/.poetry/bin"

# # RUN poetry install  && \
# #     bundler install

# RUN source $HOME/.poetry/env && poetry update && poetry install
# RUN bundler install

# EXPOSE 8000

# CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]
