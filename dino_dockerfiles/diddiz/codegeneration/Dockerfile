FROM openjdk:jdk

WORKDIR /usr/src/CodeGeneration

# Get dependencies
RUN wget http://central.maven.org/maven2/com/google/guava/guava/21.0/guava-21.0.jar && \
	wget http://central.maven.org/maven2/com/google/code/gson/gson/2.8.0/gson-2.8.0.jar && \
	wget http://central.maven.org/maven2/net/sf/jopt-simple/jopt-simple/6.0-alpha-1/jopt-simple-6.0-alpha-1.jar && \
	wget https://github.com/DiddiZ/Utils/releases/download/v1.5/utils-1.5.jar

# Add souce code
COPY ./src .
COPY ./web ./web

# Compile
RUN javac -sourcepath . -cp guava-21.0.jar:utils-1.5.jar:gson-2.8.0.jar:jopt-simple-6.0-alpha-1.jar  de/diddiz/codegeneration/CodeGeneration.java

VOLUME /usr/src/CodeGeneration/populations
EXPOSE 80
CMD ["java", "-cp", "guava-21.0.jar:utils-1.5.jar:gson-2.8.0.jar:jopt-simple-6.0-alpha-1.jar:.", "de/diddiz/codegeneration/CodeGeneration", "-server", "-poolsize=1000"]