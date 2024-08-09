#!/bin/bash

wrk2 -c 100 -t 100 -R 1000 -L -s multipart.lua http://192.168.178.38/process-image