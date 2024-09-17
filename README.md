# Introduction to Anyscale Jobs

**⏱️ Time to complete**: 5 min

This tutorial shows you how to:

1. Submit Anyscale Jobs
2. View and monitor the job in Anyscale UI.

## When to use Anyscale Jobs

We recommend running [batch Ray apps](https://docs.ray.io/en/latest/cluster/running-applications/job-submission/index.html) as Anyscale Jobs if the following features are needed: 
- Automated failure handling and retries
- Alerting
- Programmatic submission API & CI/CD integration
- Cron jobs
- Job queue and priority-based scheduling
- Record and persist outputs such as logs


**Note**: 
- In open source Ray, users run batch Ray apps with "Ray Jobs". Anyscale Jobs launch Ray Jobs on standalone Ray Clusters and manage the lifecycle of them. It also provides the additional features listed above. No code change to your Ray script is needed when running your existing Ray Jobs as Anyscale Jobs.
- For development work that requires rapid iteration, it is better to use [Anyscale Workspaces](https://docs.anyscale.com/platform/workspaces/) or other development environments.


## Submit an Anyscale Job

You can submit jobs from any machines, using the Anyscale CLI or SDK. In this tutorial, we use Anyscale CLI as an example. 

### Step 1: install Anycale CLI and authenticate
```bash
# Install the lastet version of Anyscale CLI
$ pip install -U anyscale
# Authenticate
$ anyscale login
```

### Step 2: Submit an Anyscale Job
This example includes a simple processing job that runs a few [Ray Tasks](https://docs.ray.io/en/latest/ray-core/key-concepts.html#tasks). Run the following command to submit it as an Anyscale Job

```bash
$ anyscale job submit --wait -f job.yaml
```
This example includes two important files
- job.yaml: set the entrypoint and configs of your job. Learn more about the [supported fields](https://docs.anyscale.com/reference/job-api#jobconfig)
- main.py: the Ray script to run

 It's also possible to set the entrypoint and configs directly without using YAML files. However, YAML files are recommended for better flexibility, maintainability, etc. For more details, check out the [Anyscale Job reference](https://docs.anyscale.com/reference/job-api).


## View jobs in UI

The output from the submission command should print the URL to your job in Anyscale UI. You can view the job state, logs, metrics, and Ray Dashboard in UI.

<img src="assets/anyscale-job.png" height=400px>


## Summary

This tutorial shows your how to:
1. Submit Anyscale Jobs
2. View and monitor the job in Anyscale UI.

Check out [Anyscale Jobs documentation](https://docs.anyscale.com/platform/jobs/) for more guides:
- Run cron jobs
- Run multiple jobs on the same cluster with job queue
- monitor and debug
- and more