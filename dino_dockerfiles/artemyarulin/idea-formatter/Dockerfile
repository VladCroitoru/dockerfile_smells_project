FROM openjdk:8u151-jdk
WORKDIR /idea

ENV IDEA=2017.3.2
RUN wget -qO idea.tar.gz https://download-cf.jetbrains.com/idea/ideaIC-$IDEA-no-jdk.tar.gz && \
    tar --strip-components=1 -xf idea.tar.gz && \
    rm idea.tar.gz

ENV MASK="*.*"
CMD bash bin/format.sh -r -m $MASK /srv
