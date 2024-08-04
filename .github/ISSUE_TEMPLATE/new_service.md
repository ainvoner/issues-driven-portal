---
name: New Service
about: Create a new service
title: New Service
labels: service

---

```yaml
apiVersion: acme.com/v1
kind: Service
metadata:
    name: my-new-service
labels:
    app: my-new-app
repo:
    name: my-new-repo
    owner: owner-name