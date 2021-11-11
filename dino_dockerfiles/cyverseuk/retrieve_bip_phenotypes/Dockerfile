# Docker container for retrieveing Phenotypic data from the Brassica Information Portal.
# It uses the BIP-API, stores output in .csv-format and passes the Sequence IDs on into a .txt file for further queries.


# Pull base image.
FROM ubuntu:14.04.4
FROM ruby:2.1-onbuild

MAINTAINER Annemarie Eckes, Annemarie.Eckes@earlham.ac.uk

# clone repo


COPY Gemfile.lock /usr/src/app/Gemfile.lock
COPY retrieve_phenotypes_and_ID.rb /usr/src/app/retrieve_phenotypes_and_ID.rb
COPY retrieve_trial.sh /usr/src/app/retrieve_trial.sh
ADD ExtractSeqIds.sh /usr/src/app/ExtractSeqIds.sh

WORKDIR /usr/src/app


RUN chmod 777 retrieve_phenotypes_and_ID.rb   #to remove permission error
RUN chmod +x retrieve_trial.sh
RUN chmod +x ExtractSeqIds.sh
RUN bundle install
#RUN /usr/src/app/retrieve_trial.sh

ENTRYPOINT ["/usr/src/app/retrieve_trial.sh"]
