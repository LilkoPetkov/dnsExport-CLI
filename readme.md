# DNS Exporter CLI

Simple python CLI app for DNS zone export from SiteGround to a .csv file. 

# Table of contents
* [Problem](#Problem)
* [Solution](#Solution)
* [Technologies](#Technologies)
* [Usage](#Usage)
* [Result](#Result)
* [License](#License)

## Problem

At the moment there is no tool in SiteGround with which users can export the DNS zones of their domain names. It is needed for each user to copy the records 1 by 1 in a txt file and then manually add them in their new host. 

## Solution

Using the internal site-tools-client API, regex for formatting and python for the CLI, the DNS records can be exported either for a specific domain ID, or for the whole DNS zone, depending on the user's needs.

## Technologies
 - Python 3.8 / 3.11
 - No external libraries or dependencies required

## Usage

- Help:

```
python3 dns_exporter.py -h
```

- Export all DNS records:

```
python3 dns_exporter.py --all
```

- Export DNS records for single domain ID:

```
python3 dns_exporter.py --domain_id=1
```


## Result

A file "dns_records.csv" will be created in the current working directory. An example from my hosting is uploaded in the repository:

[Example CSV]([https://github.com/LilkoPetkov/dnsExport-CLI/blob/main/dns_records.csv])

## License

[MIT](https://choosealicense.com/licenses/mit/)
