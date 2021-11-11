FROM python:3.9-slim
RUN pip install auto-editor

# install auto-editor external dependancy ffmpeg
RUN apt update -y
RUN apt install --no-install-recommends ffmpeg -y

# golem volume initialization
VOLUME /golem/input /golem/output /golem/work
WORKDIR /golem/work

# copy example file for testing
# COPY example.mp4 /golem/work/