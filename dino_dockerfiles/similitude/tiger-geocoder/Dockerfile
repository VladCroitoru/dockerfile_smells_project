FROM orlade/docker-postgis
# Note: This is built from https://github.com/helmi03/docker-postgis.
# The DockerHub build has an error.

MAINTAINER Oliver Lade <piemaster21@gmail.com>
# See https://www.census.gov/geo/maps-data/data/tiger-line.html
# See http://www.peterstratton.com/2014/04/your-own-private-geocoder-using-postgis-and-ubuntu/

# Install system dependencies.
RUN apt-get update
RUN apt-get install -qq wget python unzip

# Set the necessary Postgres environment.
ENV PGDATA /usr/local/pgsql/data
ENV PGUSER docker
ENV PGPASSWORD docker
RUN echo 'host all docker ::1/0 md5' > /etc/postgresql/9.3/main/pg_hba.conf
RUN echo 'local all docker md5' >> /etc/postgresql/9.3/main/pg_hba.conf

# Download the TIGER PostGIS extension.
RUN wget -q http://postgis.net/stuff/postgis-2.1.5dev.tar.gz
RUN tar xvfz postgis-2.1.5dev.tar.gz

# Set the platform variables in the installation scripts.
RUN sed -i 's/pgsql-9.0\///' postgis-2.1.5dev/extras/tiger_geocoder/tiger_2011/tiger_loader_2013.sql
RUN sed -i '/PGUSER/d' postgis-2.1.5dev/extras/tiger_geocoder/tiger_2011/tiger_loader_2013.sql
RUN sed -i '/PGPASSWORD/d' postgis-2.1.5dev/extras/tiger_geocoder/tiger_2011/tiger_loader_2013.sql

RUN sed -i '/PGUSER/d' postgis-2.1.5dev/extras/tiger_geocoder/tiger_2011/create_geocode.sh
RUN sed -i '/PGPASSWORD/d' postgis-2.1.5dev/extras/tiger_geocoder/tiger_2011/create_geocode.sh
RUN sed -i '/\${PSQL_CMD}/ s/-d/-v ON_ERROR_STOP=1 -d/' postgis-2.1.5dev/extras/tiger_geocoder/tiger_2011/create_geocode.sh
RUN sed -i '/search_path/ s/#//' postgis-2.1.5dev/extras/tiger_geocoder/tiger_2011/create_geocode.sh

# Create the geocoder PostGIS database and install the extension.
RUN service postgresql start && \
        createdb geocoder && \
        psql -d geocoder -f /usr/share/postgresql/9.3/contrib/postgis-2.1/postgis.sql && \
        psql -d geocoder -f /usr/share/postgresql/9.3/contrib/postgis-2.1/spatial_ref_sys.sql && \
        psql -d geocoder -c "CREATE EXTENSION fuzzystrmatch" && \
        cd postgis-2.1.5dev/extras/tiger_geocoder/tiger_2011 && ./create_geocode.sh && \
        service postgresql stop

# Prepare the database for the TIGER data.
RUN mkdir -p /gisdata/temp
RUN chmod 777 /gisdata

RUN service postgresql start && \
        psql -d geocoder -c "SELECT loader_generate_nation_script('sh');" && \
        psql -d geocoder -o /gisdata/temp.sh -c "SELECT loader_generate_script(ARRAY['DC'], 'sh');" && \
#        psql -d geocoder -o /gisdata/temp.sh -c "SELECT loader_generate_script(ARRAY['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY'], 'sh');" && \
        service postgresql stop

# Clean up the data generation script.
RUN sed 's/\s*+$//' /gisdata/temp.sh | tail -n +3 | head -n -2 > /gisdata/generate.sh
RUN rm /gisdata/temp.sh
RUN chmod +x /gisdata/generate.sh

# Generate the data and load it into the database.
RUN service postgresql start && \
        /gisdata/generate.sh && \
        psql -d geocoder -c "SELECT install_missing_indexes();" && \
        service postgresql stop

# Check that it worked.
RUN service postgresql start && \
        psql -d geocoder -c "SELECT g.rating, ST_X(geomout) As lon, ST_Y(geomout) As lat, (addy).* FROM geocode('1731 New Hampshire Avenue Northwest, Washington, DC 20010', 1) As g;" && \
        service postgresql stop


# Copy the API directory across.
#ADD api /api

# Install Python wrapper script dependencies.
#RUN apt-get install -qq python-lxml
