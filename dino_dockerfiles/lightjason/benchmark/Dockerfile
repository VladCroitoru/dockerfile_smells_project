FROM lightjason/agentspeak:latest

# --- configuration section ----------------------
ENV DOCKERIMAGE_BENCHMARK_VERSION HEAD


# --- machine configuration section --------------
RUN git clone https://github.com/LightJason/Benchmark.git /tmp/benchmark
RUN cd /tmp/benchmark && git checkout $DOCKERIMAGE_BENCHMARK_VERSION
RUN cd /tmp/benchmark && mvn package -DskipTests

RUN cd /tmp/benchmark && export JAR=$(mvn -B help:evaluate -Dexpression=project.build.finalName | grep -vi info | grep -ivvv "warning") && mv target/$JAR.jar /usr/local/bin/
RUN cd /tmp/benchmark && export JAR=$(mvn -B help:evaluate -Dexpression=project.build.finalName | grep -vi info | grep -ivvv "warning") && echo -n "#!/bin/sh\\nset -e\\nSRC=\$(dirname \$0)\\njava -jar \$JAVA_OPTS \$SRC/$JAR.jar \$@\\n" > /usr/local/bin/benchmark
RUN chmod a+x /usr/local/bin/benchmark

