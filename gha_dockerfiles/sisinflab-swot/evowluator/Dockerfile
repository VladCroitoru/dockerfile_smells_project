FROM debian:latest AS base
RUN apt update
RUN apt install -y default-jdk python3 python3-venv

FROM base AS builder
RUN apt install -y gcc gnupg2 python3-dev software-properties-common
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-keys D7CC6F019D06AF36 && add-apt-repository ppa:cwchien/gradle
RUN apt update
RUN apt install -y gradle
COPY . /evowluator
RUN /evowluator/setup.sh

FROM base
COPY --from=builder /evowluator /evowluator
ENV PATH=/evowluator/bin:${PATH}
