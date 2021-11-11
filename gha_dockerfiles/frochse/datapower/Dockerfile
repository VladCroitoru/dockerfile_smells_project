FROM ibmcom/datapower 
COPY config /opt/ibm/datapower/drouter/config
COPY local /opt/ibm/datapower/drouter/local
COPY certs /opt/ibm/datapower/root/secure/usrcerts
USER root
RUN chown -R drouter:root /opt/ibm/datapower/drouter/config \
                          /opt/ibm/datapower/drouter/local \
			  /opt/ibm/datapower/root/secure/usrcerts
RUN set-user drouter
USER drouter
