FROM centos:latest

RUN yum update -y \
	&& yum install -y traceroute curl dnsutils netcat-openbsd jq nmap net-tools dhclient \
	&& rm -rf /var/lib/apt/lists/*
