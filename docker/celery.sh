#!/bin/bash

cd my_app_new

if [["${1}" == "celery"]]; then
  celery --app=background_tasks.celery_task:celery_app worker -l INFO
elif [["${1}" == "flower"]]; then
  celery --app=background_tasks.celery_task:celery_app flower
 fi


