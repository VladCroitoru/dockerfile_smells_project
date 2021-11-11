FROM node:alpine

ENV projects_path /project
RUN mkdir ${projects_path}

COPY ./ ${projects_path}

WORKDIR ${projects_path}

RUN echo 'Install server packages...'
RUN cd ${projects_path} && npm install

RUN echo 'Install frontend packages...'
RUN cd frontend && npm install

RUN echo 'Build frontend files...'
RUN cd frontend && npm run build

CMD node server.js