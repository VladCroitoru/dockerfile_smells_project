FROM ubuntu:16.04

RUN apt-get update && \
	apt-get -y install sip-tester
	
WORKDIR /

# Instant Messging SIPp Scripts 
COPY uac_im.xml /
COPY uas_im.xml /

# Simple call flow SIPp Scripts
COPY uac_invite.xml /
COPY uas_invite.xml /
COPY uac_invite_pcap.xml /
