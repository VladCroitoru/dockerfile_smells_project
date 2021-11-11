FROM python:3.8.12-alpine3.14

COPY workspace /workspace
ENV ALPINE_FIRST_TIME_SETUP=1
RUN /workspace/root/.profile

USER alpine
WORKDIR /home/alpine
CMD ash -l
