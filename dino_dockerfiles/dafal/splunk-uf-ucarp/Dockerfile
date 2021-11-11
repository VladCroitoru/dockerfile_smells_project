FROM splunk/universalforwarder:latest

MAINTAINER Eric Daras <eric@daras.family>

# Install ucarp package
RUN apt-get update && apt-get install -y ucarp \
    && rm -rf /var/lib/apt/lists/*

# Copy example vip-up/down file to /etc/ucarp 
RUN mkdir /etc/ucarp \
	&& cp /usr/share/doc/ucarp/examples/vip-down.sh /etc/ucarp/vip-down.sh \
	&& chmod +x /etc/ucarp/vip-down.sh \
	&& cp /usr/share/doc/ucarp/examples/vip-up.sh /etc/ucarp/vip-up.sh \
	&& chmod +x /etc/ucarp/vip-up.sh

# Add the ucarp command on top ot the splunk default entrypoint
RUN sed -i '4i/usr/sbin/ucarp --interface=${UCARP_INTERFACE} --srcip=${UCARP_SOURCEADDRESS} --vhid=${UCARP_VHID} --pass=${UCARP_PASS} --addr=${UCARP_VIRTUALADDRESS} --upscript=/etc/ucarp/vip-up.sh --downscript=/etc/ucarp/vip-down.sh --xparam=${UCARP_VIRTUALPREFIX} --daemonize ${UCARP_OPTS}' /sbin/entrypoint.sh