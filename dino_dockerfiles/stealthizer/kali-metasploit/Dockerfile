FROM kalilinux/kali-linux-docker
MAINTAINER stealthizer
RUN apt-get update && apt-get install metasploit-framework --assume-yes
RUN msfupdate
CMD msfconsole
