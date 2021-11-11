FROM rcsa/python3-base:latest

RUN apt-get update

RUN apt-get update && apt-get upgrade -y 
RUN apt-get install -y \
    curl \
    sqlite3 

RUN pip install Flask 

COPY . /src

#RUN . /src/rentpath/bin/activate

VOLUME /data

EXPOSE 5000


CMD ["python","/src/input-listings.py"]

