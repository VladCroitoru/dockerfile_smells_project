FROM ubuntu:eoan
MAINTAINER Adam Price <adam@aprice.cf>

ENV DEBIAN_FRONTEND noninteractive

# Update repos
RUN apt-get update -y

# Install requirements
RUN apt-get install -y \
        software-properties-common \
        openssh-server \
        apt-utils

# Upgrade packages
RUN apt-get upgrade -y

# Install X2Go server components
RUN add-apt-repository ppa:x2go/stable
RUN apt-get update -y
RUN apt-get install -y x2goserver x2goserver-xsession --no-install-recommends

# SSH runtime
RUN mkdir /var/run/sshd

#Configure root password
RUN echo "root:SuperSecureRootPassword" | chpasswd


# Configure default user
RUN adduser --gecos "X2go User" --home /home/x2go --disabled-password x2go
RUN echo "x2go:x2go" | chpasswd

#Desktop Note with credits
RUN mkdir /home/x2go/Desktop
RUN chown x2go:x2go /home/x2go/Desktop
RUN touch /home/x2go/Desktop/README.txt
RUN echo -e "To give the user sudo access, run 'su' and use the password 'SuperSecureRootPassword' (You will be told to change this) and then use 'usermod -aG sudo x2go'.\nEnjoy!\n\nThis script was based on the work of https://github.com/bigbrozer - Check out his Github!" | tee /home/x2go/Desktop/README.txt
RUN chown x2go:x2go /home/x2go/Desktop/README.txt && chmod 777 /home/x2go/Desktop/README.txt

#Expire root password after a day
#RUN chage -d 1 root

# Run it
EXPOSE 22
CMD ["service ssh start && service x2goserver start"]
CMD ["/usr/sbin/sshd", "-D"]
