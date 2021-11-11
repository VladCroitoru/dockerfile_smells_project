FROM openjdk:alpine


RUN apk update && apk --update  add git python py-pip junit wget 


RUN pip install redis
RUN git clone https://github.com/mariosky/sandbox.git /home/sandbox
RUN wget http://search.maven.org/remotecontent?filepath=org/hamcrest/hamcrest-core/1.3/hamcrest-core-1.3.jar  --output-document=/usr/share/java/hamcrest-core.jar
RUN chmod +x /usr/share/java/hamcrest-core.jar





