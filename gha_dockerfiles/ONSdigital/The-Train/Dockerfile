FROM openjdk:8

# Add the build artifacts
WORKDIR /usr/src
ADD ./target/*-jar-with-dependencies.jar /usr/src/target/

# Set the entry point
ENTRYPOINT java -Xmx4094m \
          -Drestolino.files="target/web" \
          -Drestolino.packageprefix=com.github.davidcarboni.thetrain.api \
          -jar target/*-jar-with-dependencies.jar
