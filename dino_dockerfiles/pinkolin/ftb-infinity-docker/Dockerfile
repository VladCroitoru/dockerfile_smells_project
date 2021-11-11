FROM java:8-jre


MAINTAINER Jonas Bonno Mikkelsen (https://github.com/JonasBonno)


RUN apt-get update && \
	apt-get upgrade --yes --force-yes && \
	apt-get clean && \ 
	rm -rf /var/lib/apt/lists/* 


# Expose port 25565
EXPOSE 25565


# Adding startscript and executes it
ADD start.sh /start.sh
RUN chmod 0755 /start.sh
CMD ["bash", "start.sh"]
