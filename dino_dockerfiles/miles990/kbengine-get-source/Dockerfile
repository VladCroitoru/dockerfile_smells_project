FROM miles990/alpine-kbengine-build-tools

MAINTAINER AlexLee <alexlee7171@gmail.com> 

RUN git clone https://github.com/kbengine/kbengine.git && \
	chmod -R 755 /kbengine
	
# RUN wget https://github.com/kbengine/kbengine/archive/v0.8.10.tar.gz && \
#	tar zxvf v0.8.10.tar.gz && \
#	rm -rf v0.8.10.tar.gz && \
#	mv kbengine-0.8.10 kbengine && \
#	chmod -R 755 /kbengine

# Define mountable directories.
VOLUME ["/kbengine"]

EXPOSE 3306
EXPOSE 80
