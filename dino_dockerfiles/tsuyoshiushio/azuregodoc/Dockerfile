FROM golang:1.8
MAINTAINER Tsuyoshi Ushio

# go-autorest
RUN go get github.com/Azure/go-autorest/autorest

# Azure SDK for go

RUN go get github.com/Azure/azure-sdk-for-go/arm/advisor
RUN go get github.com/Azure/azure-sdk-for-go/arm/analysisservices
RUN go get github.com/Azure/azure-sdk-for-go/arm/apimanagement
RUN go get github.com/Azure/azure-sdk-for-go/arm/apimdeployment
RUN go get github.com/Azure/azure-sdk-for-go/arm/appinsights
RUN go get github.com/Azure/azure-sdk-for-go/arm/authorization
RUN go get github.com/Azure/azure-sdk-for-go/arm/automation
RUN go get github.com/Azure/azure-sdk-for-go/arm/batch
RUN go get github.com/Azure/azure-sdk-for-go/arm/billing
RUN go get github.com/Azure/azure-sdk-for-go/arm/cdn
RUN go get github.com/Azure/azure-sdk-for-go/arm/cognitiveservices
RUN go get github.com/Azure/azure-sdk-for-go/arm/commerce
RUN go get github.com/Azure/azure-sdk-for-go/arm/compute
RUN go get github.com/Azure/azure-sdk-for-go/arm/consumption
RUN go get github.com/Azure/azure-sdk-for-go/arm/containerinstance
RUN go get github.com/Azure/azure-sdk-for-go/arm/containerregistry
RUN go get github.com/Azure/azure-sdk-for-go/arm/containerservice
RUN go get github.com/Azure/azure-sdk-for-go/arm/cosmos-db
RUN go get github.com/Azure/azure-sdk-for-go/arm/customer-insights
RUN go get github.com/Azure/azure-sdk-for-go/arm/datalake-analytics/account
RUN go get github.com/Azure/azure-sdk-for-go/arm/datalake-store/account
RUN go get github.com/Azure/azure-sdk-for-go/arm/devtestlabs
RUN go get github.com/Azure/azure-sdk-for-go/arm/disk
RUN go get github.com/Azure/azure-sdk-for-go/arm/dns
RUN go get github.com/Azure/azure-sdk-for-go/arm/documentdb
RUN go get github.com/Azure/azure-sdk-for-go/arm/eventgrid
RUN go get github.com/Azure/azure-sdk-for-go/arm/eventhub
RUN go get github.com/Azure/azure-sdk-for-go/arm/graphrbac
RUN go get github.com/Azure/azure-sdk-for-go/arm/hdinsight
RUN go get github.com/Azure/azure-sdk-for-go/arm/insights
RUN go get github.com/Azure/azure-sdk-for-go/arm/intune
RUN go get github.com/Azure/azure-sdk-for-go/arm/iothub
RUN go get github.com/Azure/azure-sdk-for-go/arm/keyvault
RUN go get github.com/Azure/azure-sdk-for-go/arm/logic
RUN go get github.com/Azure/azure-sdk-for-go/arm/machinelearning/commitmentplans
RUN go get github.com/Azure/azure-sdk-for-go/arm/machinelearning/webservices
RUN go get github.com/Azure/azure-sdk-for-go/arm/mediaservices
RUN go get github.com/Azure/azure-sdk-for-go/arm/mobileengagement
RUN go get github.com/Azure/azure-sdk-for-go/arm/monitor
RUN go get github.com/Azure/azure-sdk-for-go/arm/mysql
RUN go get github.com/Azure/azure-sdk-for-go/arm/network
RUN go get github.com/Azure/azure-sdk-for-go/arm/networkwatcher
RUN go get github.com/Azure/azure-sdk-for-go/arm/notificationhubs
RUN go get github.com/Azure/azure-sdk-for-go/arm/operationalinsights
RUN go get github.com/Azure/azure-sdk-for-go/arm/postgresql
RUN go get github.com/Azure/azure-sdk-for-go/arm/powerbiembedded
RUN go get github.com/Azure/azure-sdk-for-go/arm/recoveryservices
RUN go get github.com/Azure/azure-sdk-for-go/arm/recoveryservicesbackup
RUN go get github.com/Azure/azure-sdk-for-go/arm/recoveryservicessiterecovery
RUN go get github.com/Azure/azure-sdk-for-go/arm/redis
RUN go get github.com/Azure/azure-sdk-for-go/arm/relay
RUN go get github.com/Azure/azure-sdk-for-go/arm/resourcehealth
RUN go get github.com/Azure/azure-sdk-for-go/arm/resources/features
RUN go get github.com/Azure/azure-sdk-for-go/arm/resources/links
RUN go get github.com/Azure/azure-sdk-for-go/arm/resources/locks
RUN go get github.com/Azure/azure-sdk-for-go/arm/resources/managedapplications
RUN go get github.com/Azure/azure-sdk-for-go/arm/resources/policy
RUN go get github.com/Azure/azure-sdk-for-go/arm/resources/resources
RUN go get github.com/Azure/azure-sdk-for-go/arm/resources/subscriptions
RUN go get github.com/Azure/azure-sdk-for-go/arm/scheduler
RUN go get github.com/Azure/azure-sdk-for-go/arm/search
RUN go get github.com/Azure/azure-sdk-for-go/arm/servermanagement
RUN go get github.com/Azure/azure-sdk-for-go/arm/service-map
RUN go get github.com/Azure/azure-sdk-for-go/arm/servicebus
RUN go get github.com/Azure/azure-sdk-for-go/arm/servicefabric
RUN go get github.com/Azure/azure-sdk-for-go/arm/sql
RUN go get github.com/Azure/azure-sdk-for-go/arm/storage
RUN go get github.com/Azure/azure-sdk-for-go/arm/storageimportexport
RUN go get github.com/Azure/azure-sdk-for-go/arm/storsimple8000series
RUN go get github.com/Azure/azure-sdk-for-go/arm/streamanalytics
RUN go get github.com/Azure/azure-sdk-for-go/arm/trafficmanager
RUN go get github.com/Azure/azure-sdk-for-go/arm/web

RUN go get github.com/Azure/azure-sdk-for-go/dataplane/keyvault
RUN go get github.com/Azure/azure-sdk-for-go/management
RUN go get github.com/Azure/azure-sdk-for-go/storage

# This directory is invalid. it includes two packages in one directory
# RUN go get github.com/Azure/azure-sdk-for-go/datalake-store/filesystem

EXPOSE 80

ENTRYPOINT godoc -http :80