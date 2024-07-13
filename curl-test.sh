#!/bin/bash

URL="http://127.0.0.1:5000/api/timeline_post"

NAME="TestUser$(date +%s)"
EMAIL="testuser$(date +%s)@example.com"
CONTENT="This is a test post created at $(date)."

create_post() {
  RESPONSE=$(curl -s -X POST $URL \
      -d "name=$NAME" \
      -d "email=$EMAIL" \
      -d "content=$CONTENT")
  echo "Response created: $RESPONSE"
  ID=$(echo $RESPONSE | jq -r '.id')
}

get_posts() {
  RESPONSE=$(curl $URL)
  echo "Get Response: $RESPONSE"
}

delete_post() {
  RESPONSE=$(curl -s -X DELETE $URL/$ID)
  echo "Deleted post ID: $ID"
}

if ! command -v jq &> /dev/null
then
    echo "jq could not be found. Please install jq to run this script."
    exit
fi

create_post

get_posts

delete_post