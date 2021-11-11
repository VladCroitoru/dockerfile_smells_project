FROM ubuntu:latest

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install -y wget libnotify4 libxkbfile1 libgconf-2-4 libnss3 libgtk2.0-0 libxss1 libgconf-2-4 libasound2 libxtst6 libcanberra-gtk-dev libgl1-mesa-glx libgl1-mesa-dri && rm -rf /var/lib/apt/lists/* && \
    wget https://go.microsoft.com/fwlink/?LinkID=760868 -O vscode.deb && \
    dpkg -i vscode.deb && \
    rm vscode.deb && \
    useradd -m vscode -s /bin/bash
RUN sed -i 's/BIG-REQUESTS/_IG-REQUESTS/' /usr/lib/x86_64-linux-gnu/libxcb.so.1
WORKDIR /root
USER vscode

CMD code --verbose --disable-gpu
