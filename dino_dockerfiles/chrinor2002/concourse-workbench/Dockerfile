FROM node:8-alpine

# NOTE: JS_* are exposed in the front end JS
ENV JS_INTERVAL 8000
#ENV JS_JOB_NAME_REGEX ^.*$
#ENV JS_JOB_NAME_REGEX_FLAGS i
#ENV CONCOURSE_URL_PROTOCOL https
ENV CONCOURSE_URL_HOST concourse.example.com

# NOTE: Enabling this will enable privileged calls to be made to concourse.
#ENV CONCOURSE_BASIC_AUTH {"username": "concourse", "password": "password"}

# NOTE: Enable this to allow tight control over possible paths that can be executed
#ENV PRIVILEGED_FILTER {"pipeline": {"job": {"trigger": true, "pause": true}}}

RUN mkdir -p /concourse-workbench/
WORKDIR /concourse-workbench/

COPY package.json /concourse-workbench/
RUN npm install

COPY . /concourse-workbench/

EXPOSE 8888
CMD [ "npm", "start" ]
