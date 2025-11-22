#!/bin/bash

echo "Refreshing all card sets..."
for FILE in card_set_lookup/*.json; do
    SET_ID=$(basename "$FILE" .json)
    echo "Refreshing card set with ID: $SET_ID"
    curl -s "https://api.pokemontcg.io/v2/cards?q=set.id:$SET_ID" > "$FILE"
    echo "Data written to $FILE"
done
echo "All card sets have been refreshed."