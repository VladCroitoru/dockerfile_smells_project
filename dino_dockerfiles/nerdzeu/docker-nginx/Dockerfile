FROM nginx:1.16-perl
MAINTAINER Paolo Galeone <nessuno@nerdz.eu>

# Create a group with a well-known id to work correctly with volumes
# and add the correct user to the group.
RUN groupadd -g 7777 nerdz && \
        gpasswd -a nginx nerdz
