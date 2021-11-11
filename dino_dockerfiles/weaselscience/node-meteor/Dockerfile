FROM node:8
RUN curl https://install.meteor.com | sh
RUN useradd --create-home meteor
USER meteor
RUN meteor help > /dev/null
