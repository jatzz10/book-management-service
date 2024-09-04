#!/bin/bash

gunicorn app.server:app -b 0.0.0.0:8000