FROM ubuntu:14.04.2

MAINTAINER ian.miell@gmail.com

RUN apt-get update && apt-get install -y -qq git python-pip
RUN pip install shutit

WORKDIR /opt
RUN git clone https://github.com/ianmiell/shutit-library

ENV HOME /root

RUN mkdir /opt/themortgagemeter
ADD . /opt/themortgagemeter


################################################################################
# Build the project using ShutIt.
# First set up the shutit configuration dotfile
RUN mkdir ~/.shutit
RUN touch ~/.shutit/config
RUN chmod 600 ~/.shutit/config
#  
RUN echo "[com.themortgagemeter.setup]" > ~/.shutit/config

# Git repository to clone the code from within the container. We will run
# git clone [this value]
# TODO: Fill this in appropriately and then delete this line
RUN echo "gitrepo:https://github.com/ianmiell/themortgagemeter.git" >> ~/.shutit/config

# Git password for pushing changes up (only needed if password required)
# TODO: Fill this in appropriately replacing mygitpass, and then delete this line
#RUN echo "#gitpassword:mygitpass" >> ~/.shutit/config

# Email to send emails
# TODO: Fill this in appropriately replacing the email address with yours and then delete this line
RUN echo "senderemail:ian.miell@gmail.com" >> ~/.shutit/config

# Password for senderemail account
# TODO: Fill this in appropriately replacing mymailpass with your email password and then delete this line
RUN echo "mailpass:mymailpass" >> ~/.shutit/config

# Administrative email account (ie mail to send alerts etc to)
# TODO: Fill this in appropriately replacing the email address with yours and then delete this line
RUN echo "adminemail:ian.miell@gmail.com" >> ~/.shutit/config

# Your site's domain name, eg themortgagemeter.com
RUN echo "sitename:My Site" >> ~/.shutit/config

# This value will be the root password for your container
# TODO: Fill this in appropriately replacing rootpass your preferred container password, and then delete this line
RUN echo "containerpass:mypass" >> ~/.shutit/config
# CONFIG SECTION COMPLETE
################################################################################

# Change the working directory to the ShutIt build
WORKDIR /opt/themortgagemeter/docker/shutit/shutit_modules/com/themortgagemeter

RUN shutit build --shutit_module_path /opt/shutit-library --delivery dockerfile

CMD ["/root/start_themortgagemeter.sh"]

