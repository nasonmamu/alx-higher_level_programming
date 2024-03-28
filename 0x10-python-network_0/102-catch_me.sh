#!/bin/bash

# Send PUT request to 0.0.0.0:5000/catch_me with user_id set to 98 and Origin header set to HolbertonSchool
curl -s -X PUT "0.0.0.0:5000/catch_me" -d "user_id=98" -H "Origin: HolbertonSchool"
