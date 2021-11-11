FROM ubuntu:14.04

RUN useradd --create-home syncthing


# gpg: key 00654A3E: public key "Syncthing Release Management <release@syncthing.net>" imported
RUN apt-get install -y curl
RUN curl -s https://syncthing.net/release-key.txt | sudo apt-key add -
RUN echo "deb http://apt.syncthing.net/ syncthing release" | sudo tee /etc/apt/sources.list.d/syncthing.list
RUN apt-get update
RUN apt-get install -y syncthing=0.12.22 ca-certificates

USER syncthing
CMD ["syncthing"]

