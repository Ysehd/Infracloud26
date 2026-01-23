#!/usr/bin/env bash

BASE_URL="https://httpbin.org"

while true; do
    echo "=============================="
    echo "AP6 – REST API met curl (Forms)"
    echo "1) GET request testen"
    echo "2) POST formulier sturen"
    echo "q) Stoppen"
    echo "=============================="
    read -p "Kies optie: " choice

    case "$choice" in
        1)
            echo "GET $BASE_URL/get"
            curl -s "$BASE_URL/get"
            ;;
        2)
            read -p "Voornaam: " fname
            read -p "Achternaam: " lname
            read -p "Email: " email
            read -p "Bericht: " msg

            echo "POST formulier naar $BASE_URL/post"
            curl -s -X POST "$BASE_URL/post" \
              -F "first_name=$fname" \
              -F "last_name=$lname" \
              -F "email=$email" \
              -F "message=$msg"
            ;;
        q|Q)
            echo "Programma afgesloten."
            exit 0
            ;;
        *)
            echo "Ongeldige keuze."
            ;;
    esac

    echo ""
done
