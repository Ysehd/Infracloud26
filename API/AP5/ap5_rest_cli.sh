#!/usr/bin/env bash

BASE_URL="https://jsonplaceholder.typicode.com"

while true; do
    echo "=============================="
    echo "AP5 – REST API met curl"
    echo "1) GET alle users"
    echo "2) GET user via ID"
    echo "3) POST nieuwe post"
    echo "4) DELETE post"
    echo "q) Stoppen"
    echo "=============================="
    read -p "Kies optie: " choice

    case "$choice" in
        1)
            echo "GET alle users"
            curl -s "$BASE_URL/users"
            ;;
        2)
            read -p "Geef user ID: " id
            curl -s "$BASE_URL/users/$id"
            ;;
        3)
            read -p "Titel: " title
            read -p "Body: " body
            read -p "User ID: " userId

            curl -s -X POST "$BASE_URL/posts" \
                -H "Content-Type: application/json" \
                -d "{\"title\":\"$title\",\"body\":\"$body\",\"userId\":$userId}"
            ;;
        4)
            read -p "Geef post ID om te verwijderen: " id
            curl -s -X DELETE "$BASE_URL/posts/$id"
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














set -euo pipefail
#!/usr/bin/env bash

