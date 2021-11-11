FROM openjdk:8-jdk

# Add files.
ADD target/java-compiler-0.0.1-SNAPSHOT-jar-with-dependencies.jar /usr/src/codingame/java-compiler/java-compiler.jar
ADD src/main/resources/cgjavac /usr/src/codingame/java-compiler/cgjavac

ENTRYPOINT ["/usr/src/codingame/java-compiler/cgjavac"]