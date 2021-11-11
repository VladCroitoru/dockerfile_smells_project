# Usage
## BUILD
# ```docker build -t aglio .```
## RUN
# ```docker run --rm -v $PWD:/data -ti aglio -i test.apib -o test.html```

# Pull base image
FROM node

# Install Aglio
RUN npm install -g aglio

VOLUME /data

WORKDIR /data

ENTRYPOINT ["aglio"]
