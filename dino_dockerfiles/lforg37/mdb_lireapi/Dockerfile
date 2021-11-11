FROM openjdk:8-jdk-alpine

COPY src/ /app/server

RUN 	apk add --no-cache wget ca-certificates ;\
	mkdir -p  /scratch /opt/gradle ;\
	cd /scratch ;\
	wget https://services.gradle.org/distributions/gradle-4.0-bin.zip ;\
	unzip -d /opt/gradle  gradle-4.0-bin.zip ;\
	mkdir -p /app/lire ;\
	cd /app/lire ;\
	rm -r /scratch ;\
	wget http://www.itec.uni-klu.ac.at/~mlux/lire-release/Lire-1.0b4.tar.bz2 ;\
	apk del --no-cache wget ca-certificates ;\
	tar xf Lire-1.0b4.tar.bz2 ;\
	rm Lire-1.0b4.tar.bz2 ;\
	/opt/gradle/gradle-4.0/bin/gradle jar ;\
	cd .. ;\
	cd /app/server ;\
	rm -rf /scratch ;\
	/opt/gradle/gradle-4.0/bin/gradle --refresh-dependencies jar

WORKDIR /app/server
EXPOSE 8080 

ENTRYPOINT ["/opt/gradle/gradle-4.0/bin/gradle"]
CMD ["RUN"]
