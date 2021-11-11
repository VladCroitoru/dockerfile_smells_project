FROM openjdk:8-jre

RUN wget -q http://nilhcem.github.com/FakeSMTP/downloads/fakeSMTP-latest.zip && unzip fakeSMTP-latest.zip -d /opt && rm fakeSMTP-latest.zip
EXPOSE 4775
VOLUME ["/var/mail"]

# Start the STMP server without a GUI (background)
CMD java -jar /opt/fakeSMTP-2.0.jar --start-server --background --port 4775 --output-dir /var/mail
