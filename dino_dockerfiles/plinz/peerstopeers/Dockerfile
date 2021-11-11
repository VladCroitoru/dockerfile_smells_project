FROM java:7
ADD . /usr/peerstopeers
WORKDIR /usr/peerstopeers/src
RUN cd /usr/peerstopeers/src
RUN javac p2p/Rdv.java
EXPOSE 5001
CMD  ["java", "p2p.Rdv"]
