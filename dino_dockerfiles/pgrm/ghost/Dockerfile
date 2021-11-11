FROM ghost

RUN apt-get update && \
	apt-get install wget -y && \
	wget https://github.com/GavickPro/Perfetta-Free-Ghost-Theme/archive/v.1.5.0.tar.gz && \
	tar -xzvf v.1.5.0.tar.gz && \
	rm v.1.5.0.tar.gz && \
	mv Perfetta-Free-Ghost-Theme-v.1.5.0 $GHOST_SOURCE/content/themes/Perfetta-Free-Ghost-Theme && \
	rm -rf /var/lib/apt/lists/*

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

EXPOSE 2368
CMD ["npm", "start"]