FROM quay.io/orgsync/clojure:2.5.3
WORKDIR /code
ADD . /code/

RUN lein uberjar \
    && mkdir /opt/markov-elear \
    && mv /code/target/markov-elear.jar /opt/markov-elear/markov-elear.jar \
    && rm -Rf /code \
    && rm -Rf /root/.m2

WORKDIR /opt/markov-elear

ENV HEAP_SIZE 100m
ENV APP_CONSUMER_KEY: foo
ENV APP_CONSUMER_SECRET: foo
ENV USER_ACCESS_TOKEN: foo
ENV USE_ACCESS_SECRET: foo

CMD exec java \
    -server \
    -XX:+UseG1GC \
    -Xmx${HEAP_SIZE} \
    -Xms${HEAP_SIZE} \
    -XX:MaxGCPauseMillis=1000 \
    -XX:+AggressiveOpts \
    -jar markov-elear.jar
