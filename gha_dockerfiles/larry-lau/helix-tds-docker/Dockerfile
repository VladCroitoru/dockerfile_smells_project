# escape=`

ARG BASE_IMAGE=mcr.microsoft.com/windows/nanoserver:1809
ARG BUILD_IMAGE=mcr.microsoft.com/dotnet/framework/sdk:4.8

FROM ${BUILD_IMAGE} AS prep

# Gather only artifacts necessary for NuGet restore, retaining directory structure
COPY *.sln nuget.config Directory.Build.targets Packages.props \nuget\
COPY src\ \temp\
COPY resources\ \resources\
RUN Invoke-Expression 'robocopy C:\temp C:\nuget\src /s /ndl /njh /njs *.csproj *.scproj packages.config'

FROM ${BUILD_IMAGE} AS builder

# TDS licensing via environment variables: https://hedgehogdevelopment.github.io/tds/chapter5.html#sitecore-tds-builds-using-cloud-servers
ARG TDS_Owner
ARG TDS_Key
ARG BUILD_CONFIGURATION
ARG DEV_TOOL

SHELL ["powershell", "-Command", "$ErrorActionPreference = 'Stop'; $ProgressPreference = 'SilentlyContinue';"]

# Install Scoop (Windows Package Manager) from Scoop.sh (This command is on their homepage)
# Tell Scoop to download and install NodeJS
# RUN [Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12 ; `
#     iwr -useb get.scoop.sh | iex ; `
#     scoop install nodejs-lts

# Create an empty working directory
WORKDIR C:\build

# Copy prepped NuGet artifacts, and restore as distinct layer to take better advantage of caching
COPY --from=prep .\nuget .\
RUN nuget restore -Verbosity quiet

# Copy 3rd party resources
COPY --from=prep .\resources\UrlRewrite C:\out\website

# For TDS development only
COPY --from=prep .\resources\${DEV_TOOL} C:\out\website

# Copy remaining source code
COPY TdsGlobal.config HelixRules.ruleset .\
COPY src\ .\src\

# Copy transforms, retaining directory structure
RUN Invoke-Expression 'robocopy C:\build\src C:\out\transforms /s /ndl /njh /njs *.xdt'

#ENV TDS_OWNER=$TDS_Owner
#ENV TDS_KEY=$TDS_Key

# Build using Release configuration
#RUN msbuild /p:Configuration=Release
RUN msbuild /p:Configuration=$env:BUILD_CONFIGURATION /p:DeployOnBuild=True /p:DeployDefaultTarget=WebPublish /p:WebPublishMethod=FileSystem /p:PublishUrl=C:\out\website /p:DebugSymbols=false /p:DebugType=None

# Copy Item resource file .dat to App_Data folder
RUN New-Item -Path C:\out\data -Name "App_Data\items\core" -ItemType "directory" -Force; `
  New-Item -Path C:\out\data -Name "App_Data\items\master" -ItemType "directory" -Force; `
  New-Item -Path C:\out\data -Name "App_Data\items\web" -ItemType "directory" -Force; `
  Get-ChildItem -Path .\src -Filter "App_Data" -Recurse | % { Copy-Item -Path $_.FullName -Destination C:\out\data -Recurse -Force };

# COPY Master to Web
#RUN Copy-Item -Path C:\out\website\App_Data\items\master -Filter *.dat -Destination C:\out\website\App_Data\items\web -Recurse

FROM ${BASE_IMAGE}

WORKDIR C:\artifacts

# Build output will land at the location specified in TDS projects (the "Build Output Path"), relative to our builder's WORKDIR
# As configured, this means our build output will be:
#	C:\build\TdsGeneratedPackages\Release -> files
#	C:\build\TdsGeneratedPackages\WebDeploy_Release -> WDP item packages

# Copy build artifacts
COPY --from=builder C:\out\website .\website\
COPY --from=builder C:\out\data .\data\
COPY --from=builder C:\out\transforms .\transforms\
#COPY --from=builder C:\build\TdsGeneratedPackages\WebDeploy_Release .\packages\