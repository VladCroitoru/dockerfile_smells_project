FROM max13fr/minecraft

ENV MINECRAFT_VERSION 1.7.10
ENV FTB_INFINITY_URL http://ftb.cursecdn.com/FTB2/modpacks/FTBInfinity/2_4_1/FTBInfinityServer.zip
ENV MINECRAFT_OPTS -server -Xms2048m -Xmx4096m -XX:MaxPermSize=256m -XX:+UseParNewGC -XX:+UseConcMarkSweepGC -Dfml.queryResult=confirm
ENV MINECRAFT_STARTUP_JAR FTBServer-$MINECRAFT_VERSION-*.jar
ENV LAUNCHWRAPPER net/minecraft/launchwrapper/1.12/launchwrapper-1.12.jar

RUN curl -SL $FTB_INFINITY_URL -o /tmp/infinity.zip && \
    unzip /tmp/infinity.zip -d $MINECRAFT_HOME && \
    mkdir -p $MINECRAFT_HOME/$(dirname libraries/${LAUNCHWRAPPER}) && \
    curl -S https://libraries.minecraft.net/$LAUNCHWRAPPER -o $MINECRAFT_HOME/libraries/$LAUNCHWRAPPER && \
    find $MINECRAFT_HOME -name "*.log" -exec rm -f {} \; && \
    rm -rf $MINECRAFT_HOME/ops.* $MINECRAFT_HOME/whitelist.* $MINECRAFT_HOME/logs/* /tmp/*
