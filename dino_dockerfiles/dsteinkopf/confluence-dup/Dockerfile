FROM dsteinkopf/docker-atlassian-confluence

# disable breadcumbs
# see https://confluence.atlassian.com/display/CONFKB/How+to+disable+hiding+(ellipsing)+of+breadcrumbs
USER root
RUN sed --in-place=.orig \
	's/#if ($ellipsisCrumbs.contains($breadcrumb))/#if (false)/' \
	 "${CONF_INSTALL}/confluence/breadcrumbs.vm"

RUN touch /opt/atlassian/confluence/conf/jmxremote.access \
          /opt/atlassian/confluence/conf/jmxremote.password \
          /opt/atlassian/confluence/conf/server.xml

RUN apk update \
	&& apk add \
		graphviz \
		gcompat

USER daemon:daemon

