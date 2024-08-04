---
name: New Service
description: Create a new service
title: New Service
labels: NewService
---

apiVersion: acme.com/v1
kind: Service
metadata:
    name: <service name>
labels:
    app: <app name>
repo:
    name: <repository name>
    owner: <owner>