FROM ghcr.io/siwatinc/java-baseimage:openjdk15
RUN wget https://www.multicraft.org/download/linux64 && tar -xvzf ./linux64 && rm ./linux64 && rm -rv ./multicraft/panel && mv -v ./multicraft /installer && sed -i '1 i\cd /installer' /installer/setup.sh
RUN apt-get update && apt-get install -y iproute2 zip
RUN useradd -m multicraft
COPY ./initialize.sh /initialize.sh
COPY ./install.sh /installer/install.sh
CMD chmod +x /initialize.sh && chmod +x /installer/install.sh && /initialize.sh
