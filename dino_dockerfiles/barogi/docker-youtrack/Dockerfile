FROM java:7
#MAINTAINER Till Backhaus <tback@tfw.ag>

ENV YOUTRACK_VERSION 6.5.17057

RUN wget https://download.jetbrains.com/charisma/youtrack-${YOUTRACK_VERSION}.jar -O youtrack.jar

EXPOSE 80
CMD ["java", "-Xmx1g", "-XX:MaxPermSize=250m", "-Djava.awt.headless=true", "-Djetbrains.youtrack.disableBrowser=true", "-jar", "youtrack.jar", "80"]
