#docker build -t contactinfo-ms:1.0 .
#docker run -p 127.0.0.1:8080:8080  avijitsarkar123/contactinfo-ms:1.0

#This is contactinfo microservice docker file

FROM avijitsarkar123/ubuntu_java7:latest
MAINTAINER avijit sarkar

EXPOSE 8080

ADD /target/contact-info-0.0.1-SNAPSHOT.jar /data/contact-info-0.0.1-SNAPSHOT.jar
RUN chmod 777 /data/contact-info-0.0.1-SNAPSHOT.jar
CMD ["java", "-jar", "/data/contact-info-0.0.1-SNAPSHOT.jar"]