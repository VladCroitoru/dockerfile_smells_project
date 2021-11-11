FROM java:8

RUN mkdir /opt/s3ninja
RUN curl -o /opt/s3ninja/s3ninja.zip https://oss.sonatype.org/content/groups/public/com/scireum/s3ninja/2.7/s3ninja-2.7-zip.zip

RUN cd /opt/s3ninja && unzip /opt/s3ninja/s3ninja.zip
RUN rm /opt/s3ninja/s3ninja.zip
RUN mkdir -m 777 -p /opt/s3ninja/data/s3

VOLUME /opt/s3ninja/data/s3

EXPOSE 9444
EXPOSE 9191

CMD /opt/s3ninja/sirius.sh start && sleep 5 && tail -f /opt/s3ninja/logs/stdout.txt