FROM python:alpine

LABEL maintainer="Tiago Rodrigues <mail@tig.pt>"

##################
#  Install praw  #
##################

RUN pip install praw

############################
#  Install beautifulsoup4  #
############################

RUN pip install beautifulsoup4

#######################
#  Run python script  #
#######################

CMD ["python", "-u", "/volumes/script.py"]
