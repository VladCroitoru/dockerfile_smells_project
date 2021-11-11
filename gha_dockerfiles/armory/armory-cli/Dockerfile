FROM debian:10.10-slim
ARG BUILD_PATH
ENV APP=/usr/local/bin/armory \
    USER_UID=1001 \
    USER_NAME=armory
RUN apt-get update -y  && apt upgrade -y \
	&& apt-get install -y ca-certificates bash
RUN adduser --disabled-password --gecos "First Last,RoomNumber,WorkPhone,HomePhone" --uid ${USER_UID} ${USER_NAME}
WORKDIR /usr/local/bin
COPY ${BUILD_PATH} ./
COPY ./entrypoint.sh ./

USER ${USER_NAME}
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]