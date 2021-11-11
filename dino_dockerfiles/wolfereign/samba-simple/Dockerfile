FROM alpine:latest
Label maintainer="Wolfereign"

# Create User & Directories
RUN mkdir -p /samba/config /samba/shares \
	&& chown "998":"998" /samba \
	&& addgroup --system --gid "998" samba \
	&& adduser --system --uid "998" --gid "998" --home /samba samba

# Update Packages and Install Needed Packages
RUN apk add --update --no-cache \ 
		dumb-init \
		samba \
		samba-common-tools \
		supervisor \
		&& rm -rf /var/cache/apk/*

# Copy Needed Files / Scripts Into Image
COPY . /root/

# Expose Needed ports (137/udp and 138udp for nmbd)(139 and 445 for smbd) 
EXPOSE 137/udp 138/udp 139 445

# Supervisord will run the samba services in the foreground and redirect logs
ENTRYPOINT ["/usr/bin/dumb-init", "/bin/sh", "/root/entrypoint.sh"]
