FROM ivukotic/ml_platform_auto:latest

LABEL maintainer Ilija Vukotic <ivukotic@cern.ch>

RUN apt-get update && apt-get install sendmail -y
RUN pip3.8 install ipwhois

COPY . .

RUN mkdir -p Users/Images
# build info
RUN echo "Timestamp:" `date --utc` | tee /image-build-info.txt

# CMD ["/.run"]
