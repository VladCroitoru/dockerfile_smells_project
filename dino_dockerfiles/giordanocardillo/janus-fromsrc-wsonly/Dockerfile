FROM debian:8
COPY ./build.sh /root/build.sh
RUN sh /root/build.sh
EXPOSE 8188 8989 8088 8089
CMD /opt/janus/bin/janus

