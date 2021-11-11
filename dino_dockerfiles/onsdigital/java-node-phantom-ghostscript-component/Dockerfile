FROM onsdigital/java-node-phantom-component

# Dependencies for running ghostscript

RUN apt-get clean
RUN apt-get update -y
RUN apt-get install -fyqq \
  ghostscript

# Test if ghostscript works

RUN gs -v
CMD echo "ghostscript binary is located at /usr/local/bin/gs" \
     && echo "just run 'gs' (version `gs -v`)"
