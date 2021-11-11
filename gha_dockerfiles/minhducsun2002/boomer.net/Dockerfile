FROM mcr.microsoft.com/dotnet/sdk:5.0.301-alpine3.13 as build
WORKDIR /app

COPY . . 
COPY nuget.config .
RUN echo $BUILD_HASH
RUN dotnet publish Pepper -c release --runtime linux-musl-x64 --self-contained -o dist/ 

FROM mcr.microsoft.com/dotnet/runtime-deps:5.0.7-alpine3.13
COPY --from=build /app/dist /app
WORKDIR /app
CMD ./Pepper
