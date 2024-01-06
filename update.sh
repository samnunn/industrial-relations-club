#!/bin/bash

new_date=$(date +"<span id=\"last-updated\">%Y-%m-%d</span>")
sed -i '' "s|<span id=\"last-updated\">[^<]*</span>|$new_date|g" _site/index.html