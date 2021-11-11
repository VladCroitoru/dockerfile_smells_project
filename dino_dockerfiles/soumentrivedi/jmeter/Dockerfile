#
# Dockerfile for a jmeter client.
# A container from this image will be ready to run a jmeter client.
# 
# Usage:
#  docker run -d \
#             -v <absolute path on host>:/logs \
#             -v <absolute path on host>:/input-data \
#             -v <absolute path on host>:/scripts \
#             <docker image> -n \
#                            -LDEBUG # <-- ok, this is optional.
#                            -t /scripts/<script file name> 
#                            -l /logs/<output jtl file name>
#                            -R<server IP addresses>
#
# TODO - The current recipe demands that the jmeter.properties used by jmeter-server image and
#        the one used by *this* image be in lock step; at least as far as the ports are concerned.
#        That seems icky.  Fix it, yo!

# Use jmeter-base as the foundation
FROM soumentrivedi/jmeter-base

MAINTAINER Souman Trivedi soumen.trivedi@gmail.com 

# Create mount point for script, data and log files
VOLUME ["/scripts"]
VOLUME ["/input_data"]
VOLUME ["/logs"]

# Use a predefined configuration.  This sets the contract for connecting to jmeter servers.
ADD jmeter.properties /var/lib/apache-jmeter/bin/

ENTRYPOINT [ "/var/lib/apache-jmeter/bin/jmeter" ]
