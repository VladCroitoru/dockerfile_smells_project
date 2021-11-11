FROM lpasquali/wine:latest
MAINTAINER Luca Pasquali <lpasquali@gmail.com>
WORKDIR /home/semilanceata
USER root
COPY start.sh /scripts/
RUN chmod +x /scripts/start.sh 
USER semilanceata
RUN wget -r -np -k http://amyco.fr/Pixi5X/Application%20Files/Piximetre_5_9_0_1532/ 
RUN find './amyco.fr/Pixi5X/Application Files/Piximetre_5_9_0_1532/'| rename -v 's/\.deploy$//'
CMD ["/scripts/start.sh"]
