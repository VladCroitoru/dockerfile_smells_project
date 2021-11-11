ARG BASE_IMAGE=python
ARG PYTHON_VERSION=3.6
FROM ${BASE_IMAGE}:${PYTHON_VERSION}

# Environment Settings
ENV GEOIP_PATH "/data/geo"
ENV GEOIP_COUNTRY "GeoLite2-Country.mmdb"
ENV GEOIP_CITY "GeoLite2-City.mmdb"
ENV LIBMAXMINDDB_VERSION "1.3.2"

# Create directories
RUN mkdir -p "$GEOIP_PATH"

# Install GeoIP2 C library
# See https://docs.djangoproject.com/en/dev/ref/contrib/gis/geoip2/
RUN cd "/tmp/" && \
    wget --quiet "https://github.com/maxmind/libmaxminddb/releases/download/$LIBMAXMINDDB_VERSION/libmaxminddb-$LIBMAXMINDDB_VERSION.tar.gz" && \
    tar -zxf "libmaxminddb-$LIBMAXMINDDB_VERSION.tar.gz" && \
    rm "libmaxminddb-$LIBMAXMINDDB_VERSION.tar.gz" && \
    cd "/tmp/libmaxminddb-$LIBMAXMINDDB_VERSION/" && \
    ./configure && \
    make && \
    make check && \
    make install && \
    ldconfig && \
    rm -r "/tmp/libmaxminddb-$LIBMAXMINDDB_VERSION"

# Accept Maxmind License Key as a build arg
# See https://blog.maxmind.com/2019/12/18/significant-changes-to-accessing-and-using-geolite2-databases/
ARG MAXMIND_LICENSE_KEY

# Download and unzip the GeoIP2 Country database
RUN cd "$GEOIP_PATH" && \
    wget --quiet "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-Country&license_key=$MAXMIND_LICENSE_KEY&suffix=tar.gz" -O "$GEOIP_COUNTRY.tar.gz" && \
    tar xvzf "$GEOIP_PATH/$GEOIP_COUNTRY.tar.gz" && \
    mv $GEOIP_PATH/GeoLite2-Country_*/* "$GEOIP_PATH/" && \
    rmdir $GEOIP_PATH/GeoLite2-Country_* && \
    rm "$GEOIP_PATH/$GEOIP_COUNTRY.tar.gz"


# Download and unzip the GeoIP2 City database
RUN cd "$GEOIP_PATH" && \
    wget --quiet "https://download.maxmind.com/app/geoip_download?edition_id=GeoLite2-City&license_key=$MAXMIND_LICENSE_KEY&suffix=tar.gz" -O "$GEOIP_CITY.tar.gz" && \
    tar xvzf "$GEOIP_PATH/$GEOIP_CITY.tar.gz" && \
    mv $GEOIP_PATH/GeoLite2-City_*/* "$GEOIP_PATH/" && \
    rmdir $GEOIP_PATH/GeoLite2-City_* && \
    rm "$GEOIP_PATH/$GEOIP_CITY.tar.gz"

# Install the GeoIP Python library
RUN pip install --no-cache-dir --upgrade "geoip2"

# Install IPython, because it's nice to have
RUN pip install --no-cache-dir --upgrade "ipython"

# Install Poetry for dependency management
ENV POETRY_VERSION "1.1.10"
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
ENV PATH "/root/.poetry/bin:${PATH}"
RUN poetry config virtualenvs.create false

# Optionally install Geospatial libraries
ARG GEOSPATIAL
RUN if [ "$GEOSPATIAL" = "true" ]; then \
        apt-get update; \
        apt-get install -y binutils libproj-dev gdal-bin; \
        rm -rf /var/lib/apt/lists/*; \
    fi
