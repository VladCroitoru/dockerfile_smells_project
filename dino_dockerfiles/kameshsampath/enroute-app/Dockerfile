FROM kameshsampath/jpm4j

MAINTAINER Kamesh Sampath, kamesh.sampath@hotmail.com

ENV BNDTOOLS_VERSION=3.2.0.201605172007
ENV ENROUTE_VERSION=3.2.0.201605172024

##
# Refer to other available labels here 
##
LABEL io.k8s.description="OSGi enRoute" \
      io.k8s.display-name="OSGi enRoute Application" \
      io.openshift.expose-services="8080:http" \
      io.openshift.tags="builder,osgi,enroute" \
      io.openshift.s2i.scripts-url="image:///opt/enroute/s2i"

COPY s2i opt/enroute/s2i
ADD README.md opt/enroute/s2i/usage.txt

# ensure all scripts are runnable and create a placeholder directory for gradle wrapper distributions
# for cases where we can inject the distributions via s2i 
RUN chmod +x /opt/enroute/s2i/* && \
    mkdir -p $HOME/.gradle/wrapper/dists

# Modify the usage script in your application dir to inform the user how to run
# this image.
CMD ["/opt/enroute/s2i/run"]