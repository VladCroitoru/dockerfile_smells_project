FROM ubuntu:14.04

RUN apt-get update && apt-get install shellinabox

# a new user is needed to get access to the container
RUN useradd shellboxuser
RUN echo "shellboxuser:shellboxuser" | chpasswd

#this is needed to gain root access
RUN echo "root:shellboxuser" | chpasswd

EXPOSE 4200

CMD ["shellinaboxd", "-s", "/:LOGIN", "--disable-ssl"]







