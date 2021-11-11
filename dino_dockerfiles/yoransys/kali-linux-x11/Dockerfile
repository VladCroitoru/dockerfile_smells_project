FROM kalilinux/kali-linux-docker
RUN apt update
RUN apt install -y xterm synapse kali-linux-full kali-desktop-lxde
ENV DISPLAY=:1
COPY startup.sh /startup.sh
RUN chmod +x  /startup.sh

CMD /startup.sh
