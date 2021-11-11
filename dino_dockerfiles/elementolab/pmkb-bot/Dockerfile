FROM microsoft/dotnet:2.1-sdk-stretch as builder

LABEL org.opencontainers.image.source='https://github.com/eipm/pmkb-bot' \
    Description='.net Core SDK security hardened Image' \
    Vendor='Englander Institute for Precision Medicine' \
    maintainer='paz2010@med.cornell.edu' \
    base_image='microsoft/dotnet' \
    base_image_version='2.1-sdk-stretch'

WORKDIR /app

# Copy everything and build
COPY /src .
RUN dotnet restore Pmkb.Bot.csproj
RUN dotnet publish Pmkb.Bot.csproj -c Release -o out

#FROM microsoft/dotnet:2.1.1-aspnetcore-runtime

#LABEL Description='.net Core SDK security hardened Image' \
#    Vendor='Englander Institute for Precision Medicine' \
#    maintainer='paz2010@med.cornell.edu' \
#    base_image='dotnetcore' \
#    base_image_version='2.1-aspnetcore-runtime' \

#COPY --from=builder /app/out /app/out
#COPY --from=builder /app/pmkb.bot /app/out/pmkb.bot

EXPOSE 3978
#WORKDIR /app/out
#CMD ["dotnet", "Pmkb.Bot.dll"]