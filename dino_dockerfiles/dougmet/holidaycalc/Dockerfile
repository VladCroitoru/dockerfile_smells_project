FROM dougmet/plumber:3.3.2

# Copy all files in
COPY . /pbpkg/

# Install package and deps
WORKDIR /pbpkg

# Using devtools for its dependency management
RUN R -e "devtools::install()" \
  && chgrp -R staff /pbpkg

# Plumb your app into 8000
EXPOSE 8000

CMD ["/plumbapp.sh", "/pbpkg/inst/api.R"]
