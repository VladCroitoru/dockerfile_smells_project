FROM ubuntu:17.10
#I was going to pull an image with Java and Git already installed but want to make sure I had full controll of versions

LABEL maintainer="Richard Dawson <r.dawson@me.com>"

ENV DEBIAN_FRONTEND="noninteractive"

#update system, install prereq & depenaces for application
RUN apt-get update && apt-get install -y \
git \
default-jdk

#Setup location for pre-build sourcefiles
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

#Pull copy of the MLD test application
RUN git clone https://github.com/MyLifeDigital/mld-devops-test.git

#Build note application and move into live excutable location
WORKDIR /usr/src/app/mld-devops-test
RUN ./gradlew clean build
RUN mkdir -p /opt/MLD
WORKDIR /usr/src/app/mld-devops-test/build/libs
RUN mv *.jar /opt/MLD/Notes.jar


#Start the application
ENTRYPOINT ["java","-jar","/opt/MLD/Notes.jar"]

# private and public mapping
EXPOSE 8080:8080/tcp
