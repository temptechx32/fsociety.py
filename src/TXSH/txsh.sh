#!/usr/bin/env bash

clear

# Farben
CYAN='\033[1;36m'
GREEN='\033[1;32m'
RED='\033[1;31m'
RESET='\033[0m'

# Logo
echo -e "${CYAN}████████╗██╗  ██╗███████╗██╗  ██╗"
echo -e "╚══██╔══╝╚██╗██╔╝██╔════╝██║  ██║"
echo -e "   ██║    ╚███╔╝ ███████╗███████║"
echo -e "   ██║    ██╔██╗ ╚════██║██╔══██║"
echo -e "   ██║   ██╔╝ ██╗███████║██║  ██║"
echo -e "   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝${RESET}"

echo -e "${GREEN}          TECHX SHELL${RESET}"
echo

# Shell Loop
while true; do

    # CMD BAR
    echo -ne "${CYAN}TXSH${RESET}> "

    # Eingabe
    read -r cmd args

    # Built-in Commands
    case "$cmd" in

        exit)
            echo -e "${RED}TXSH closed.${RESET}"
            break
            ;;

        help)
            echo "Commands:"
            echo "  techxfetch"
            echo "  hello"
            echo "  fbsh"
            echo "  help"
            ;;
        
        clear)
            clear
            ;;

        *)
            # BIN COMMANDS
            if [ -x "./bin/$cmd" ]; then
                "./bin/$cmd" $args
            else
                echo -e "${RED}Command not found:${RESET} $cmd"
            fi
            ;;
    esac

done