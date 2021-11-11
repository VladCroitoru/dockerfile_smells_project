FROM khirin/tomcat

ENV	MAX_MEM="640"
ENV	JAVA_OPTS="-Xmx${MAX_MEM}m -Dsubsonic.host=0.0.0.0 -Dsubsonic.contextPath=/subsonic -Dsubsonic.home=/data -Dsubsonic.defaultMusicFolder=/music/1_CURRENT -Dsubsonic.defaultPodcastFolder=/podcasts/ -Dsubsonic.defaultPlaylistFolder=/playlists/ -Djava.awt.headless=true"

LABEL 	maintainer="khirin" \
	name="Subsonic Image" \
        subsonic_version="6.0" \
	date="20170307" \
        image_version="1.5"

COPY ["sources/subsonic_6.0.war", "sources/init.sh", "/tmp/"]

USER root

RUN	addgroup -g 1111 friends \
	&& sed -i 's/friends.*/&tomcat/' /etc/group \
	&& mv /tmp/subsonic_6.0.war ${CATALINA_HOME}/webapps/subsonic.war \
	&& /tmp/init.sh

VOLUME ["/data", "/music", "/playlists", "/podcasts"]

USER tomcat
