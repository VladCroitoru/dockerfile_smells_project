FROM zoltu/aspnetcore-gulp-bower

RUN npm install -g handlebars

# begin nuget caching laayer
COPY global.json /app/global.json
COPY code/project.json /app/code/project.json
COPY code/project.lock.json /app/code/project.lock.json
COPY tests/project.json /app/tests/project.json
COPY tests/project.lock.json /app/tests/project.lock.json
WORKDIR /app
RUN dotnet restore
# end nuget caching layer

# begin server layer
COPY code/*.cs /app/code/
COPY code/Controllers/ /app/code/Controllers/
COPY code/Extensions/ /app/code/Extensions/
COPY tests/ /app/tests
WORKDIR /app
RUN dotnet restore
WORKDIR /app/code
RUN dotnet build
WORKDIR /app/tests
RUN dotnet build
RUN dotnet test
# end server layer

# begin client layer
COPY code/client /app/code/client
WORKDIR /app/code
RUN handlebars /app/code/client/scripts/templates/ --output /app/code/client/scripts/templates/template.min.js --map
# end client layer

EXPOSE 80

ENTRYPOINT ["dotnet", "run"]
