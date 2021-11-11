FROM ubuntu

MAINTAINER juliens@microsoft.com

RUN apt-get update && apt-get upgrade -y

RUN apt-get install stress

ENTRYPOINT ["stress"]
