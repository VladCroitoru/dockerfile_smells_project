FROM debian as build

RUN apt-get update
RUN apt-get -y install wget unzip

RUN wget "http://naciscdn.org/naturalearth/packages/natural_earth_vector.sqlite.zip"

RUN unzip natural_earth_vector.sqlite.zip

FROM terranodo/datasette:spatialite

COPY --from=build packages/natural_earth_vector.sqlite /natural_earth_vector.sqlite

CMD ["datasette", "serve", "/natural_earth_vector.sqlite", "--host", "0.0.0.0", "--cors"]
