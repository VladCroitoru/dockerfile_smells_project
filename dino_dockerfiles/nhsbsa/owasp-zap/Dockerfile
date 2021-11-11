FROM owasp/zap2docker-weekly:latest
MAINTAINER Phil Stephenson "philip.stephenson1@nhs.net"
EXPOSE 8080
ENTRYPOINT ["zap.sh"] 
CMD ["-daemon", "-port", "8080", "-host", "0.0.0.0", "-config", "api.disablekey=true"]
