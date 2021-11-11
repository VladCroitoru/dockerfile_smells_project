FROM jboss/immutant
MAINTAINER ian@blenke.com

EXPOSE 12001

CMD java -classpath /opt/immutant/jboss/modules/system/layers/base/org/jboss/logging/main/jboss-logging-3.1.2.GA.jar:/opt/immutant/jboss/modules/system/layers/base/org/jgroups/main/jgroups-3.4.0.Alpha2.jar org.jgroups.stack.GossipRouter -port 12001
