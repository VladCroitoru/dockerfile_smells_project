FROM microsoft/dotnet:2.1-sdk-alpine

# Install Nodejs
RUN apk add --no-cache nodejs nodejs-npm libuv \  
    && ln -s /usr/lib/libuv.so.1 /usr/lib/libuv.so \
    && mkdir /usr/src \
    && mkdir /usr/src/app

# Switch Workdir
WORKDIR /usr/src/app

# Copy everything local
COPY . .

# Install node packages and restore dotnet packages
RUN npm install \  
    && dotnet restore \
    && dotnet build

EXPOSE 5000

CMD ["dotnet", "run"]  