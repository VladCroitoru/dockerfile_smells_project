FROM ubuntu:16.04
LABEL Name=dad Authors="@gwleclerc,@matcornic,@Thiht,@TheCampagnards"

ENV TERM=linux

WORKDIR /opt/dad

RUN apt-get update && \
    apt-get install -y \
      bash \
      curl \
      jq \
      unzip && \
    apt-get clean && \
    dad_release=$(curl -s https://api.github.com/repos/soprasteria/dad/releases | jq -M -r '.[0].assets[0].browser_download_url') && \
    curl -Lo dad.zip "$dad_release" && \
    unzip dad.zip && \
    rm dad.zip && \
    apt-get remove -y curl jq unzip

EXPOSE 8080
CMD ["./dad", "serve"]
