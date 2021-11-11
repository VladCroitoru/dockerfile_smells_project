FROM python:3.8-slim AS base
LABEL maintainer "Boungjin Kim<kbj80494@gmail.com>"
LABEL title="FastAPI"
LABEL version="1.0"
LABEL description="This image is Buzzni Machine Learning API Server"

# setting ENV
ENV TZ=Asia/Seoul \
    BZN_HOME=/bz_app
RUN ln -snf /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone


# docker volume
RUN mkdir -p ${BZN_HOME}

# apt setting
RUN apt-get update -qq 
RUN apt-get upgrade -y

WORKDIR ${BZN_HOME}
COPY . ${BZN_HOME}
RUN pip install --disable-pip-version-check -r requirements.txt
WORKDIR ${BZN_HOME}/backend
# CMD ["python", "main.py"]
