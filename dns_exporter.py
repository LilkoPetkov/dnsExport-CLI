import re
import subprocess
import csv
import argparse
import os

from typing import List, Union


# Colors
class Colors:
    reset='\033[0m'
    bold='\033[01m'
    class fg:
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'


c, fg = Colors(), Colors.fg()
##                    Colors
## --------------------------------------------- ##


def get_data(domain_id: int = 0, all: bool = False) -> str:
    if all:
        command: str = f"site-tools-client dns list -J"
    else:
        command: str = f"site-tools-client dns list domain_id={domain_id} -J"

    result = subprocess.run(command, shell=True, capture_output=True, text=True)

    if result.stderr:
        parser.exit(1, message=f"{fg.red}{c.bold}Error{c.reset}: {result.stderr}\n")
    else:
        target: str = ""
        for res in result.stdout.split("},"):
            target += str(res)

    return target


def format_data(target: str) -> List[dict[str, Union[str, int]]]:
    pattern: str = r"(?P<data>(?P<nameSrv>\"name\":[A-z0-9\._;:\"]+,)?(?P<portSrv>\"port\":[0-9]+,)?(?P<prioSrv>\"prio\":[0-9]+,)?(?P<proto>\"proto\":[\"A-z]+,)?(?P<service>\"service\":[A-z0-9\"]+,)?(?P<priority>\"prio\":[0-9,]+)?\"ttl\":[0-9,]+,\"type\":[\"A-z]+,\"value\":[\"0-9\.A-z_\=\s\+:~\-\;]+\b)"
    records_pattern: re.Pattern = re.compile(pattern)

    data: List[dict[str, Union[str, int]]] = []

    for match in records_pattern.finditer(target):
        row = match.group(0).split(",")
        temp_dict: dict[str, Union[str, int]] = {}

        for entry in row:
            key, val = entry.split(":", 1)
            key, val = key.replace('"', ""), val.replace('"', "")
            
            temp_dict[key] = val

        data.append(temp_dict)

    return data
        

def write_data(data: List[dict[str, Union[str, int]]]) -> None:
    header: List[str] = [
        'name', 'type', 'port', 'proto', 'ttl', 'service', 'prio', 'value'
    ]

    with open('dns_records.csv', 'w', newline='') as csvfile:
        fieldnames: List[str] = header 
        writer: csv.DictWriter = csv.DictWriter(csvfile, fieldnames=fieldnames, restval="NA")

        writer.writeheader()
        writer.writerows(data)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="A small app to export DNS records from SiteGround in a csv", 
        usage=f"{fg.green}{os.path.basename(__file__)} [-h/--help] --domain_id/-id=INT | --all [--version/-v]{c.reset}"
    )
    # mutually exclusive group
    mutuallyExclusive = parser.add_mutually_exclusive_group(required=True)

    # arguments
    mutuallyExclusive.add_argument("--all", help="all domain DNS records", action="store_true")
    mutuallyExclusive.add_argument("--domain_id", "-id", type=int, help="single domain DNS records", metavar="", default=0)
    parser.add_argument("-v", "--version", action="version", version="0.1.0")

    # parsing
    args: argparse.Namespace = parser.parse_args()
    domain_id: int = args.domain_id
    domain_all: str = args.all

    # functions
    target: str = get_data(domain_id, domain_all)
    formatted_data: List[dict[str, Union[str, int]]] = format_data(target)
    write_data(formatted_data)
