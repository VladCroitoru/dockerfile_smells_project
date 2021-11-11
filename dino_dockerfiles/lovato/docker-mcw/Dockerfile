FROM webratio/ant

# Installs Git

RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y curl --fix-missing
RUN apt-get install -y --force-yes git-all
RUN apt-get install -y --force-yes zip
RUN apt-get autoremove -y
RUN apt-get clean
