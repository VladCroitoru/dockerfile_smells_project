FROM ubuntu:latest

# Dependencies
RUN apt update -y && apt upgrade -y
RUN echo 'tzdata tzdata/Areas select Europe' | debconf-set-selections
RUN echo 'tzdata tzdata/Zones/Europe select Paris' | debconf-set-selections
RUN DEBIAN_FRONTEND="noninteractive" apt install -y tzdata
RUN apt install -y software-properties-common g++ nlohmann-json3-dev \
    mosquitto mosquitto-clients libmosquitto-dev cmake pkg-config
RUN add-apt-repository ppa:pistache+team/unstable && apt update -y && apt install -y libpistache-dev

# Debugging
RUN apt install -y curl wget nmap

# Compile
COPY . /app
WORKDIR /app
RUN cmake . && cmake --build . && chmod 755 ./smart-tv

# Run
COPY ./delay.sh /delay.sh
RUN chmod 755 /delay.sh
EXPOSE 9080
RUN useradd -m dorel
USER dorel
CMD ["/delay.sh", "1", "./smart-tv"]
