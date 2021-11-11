FROM kalilinux/kali-linux-docker

RUN apt-get -y update && apt-get -y install \
	python \
	python-pip \
	aircrack-ng \
	tcpdump \
	tcpreplay
RUN pip install scapy

CMD ["/bin/bash"]