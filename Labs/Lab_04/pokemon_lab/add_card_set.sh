#!/usr/bin/env bash

read -r -p "Enter the TCG Card Set ID: " SET_ID

if [ -z "$SET_ID" ]; then
    echo "Error: Set ID cannot be empty." >&2
    exit 1
fi

echo "Fetching card set with ID: $SET_ID"
curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID&page=1&pageSize=250" > card_set_lookup/"$SET_ID".json

echo "Card set data saved to card_set_lookup/$SET_ID.json"