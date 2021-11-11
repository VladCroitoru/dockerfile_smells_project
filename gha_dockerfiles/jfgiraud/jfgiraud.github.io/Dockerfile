FROM alpine:3.13
LABEL maintainer = "Jean-François Giraud"


# Define build arguments
ARG USER_UID
ARG USER_GID
ARG USER_NAME
ARG USER_PASSWORD
ARG ROOT_PASSWORD

# Define environment variables
ENV USER_UID=${USER_UID}
ENV USER_GID=${USER_GID}
ENV USER_NAME=${USER_NAME}
ENV USER_PASSWORD=${USER_PASSWORD}
ENV ROOT_PASSWORD=${ROOT_PASSWORD}

RUN apk update
RUN apk add --no-cache bash
RUN apk add --no-cache shadow
RUN apk add --no-cache make
RUN apk add --no-cache python3
RUN apk add --no-cache py3-pip
RUN apk add --no-cache pytest
RUN apk add --no-cache py3-beautifulsoup4
RUN apk add --no-cache py3-lxml

RUN groupadd -g ${USER_GID} ${USER_NAME}
RUN useradd -d /home/${USER_NAME} -g ${USER_GID} -s /bin/bash -u ${USER_UID} ${USER_NAME}
RUN echo "${USER_NAME}:${USER_PASSWORD}" | chpasswd
RUN echo "root:${ROOT_PASSWORD}" | chpasswd
