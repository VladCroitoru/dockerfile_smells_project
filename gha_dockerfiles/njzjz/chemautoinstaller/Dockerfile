FROM ubuntu:20.04@sha256:626ffe58f6e7566e00254b638eb7e0f3b11d4da9675088f4781a50ae288f3322
RUN apt update && apt install wget bzip2 -y && apt clean -y
COPY "ChemAutoInstaller.sh" "/ChemAutoInstaller.sh"
RUN bash ChemAutoInstaller.sh -A
