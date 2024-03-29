# DNS Exporter CLI

Python CLI app for DNS zone export from SiteGround into a .csv file. 

# Table of contents
* [Problem](#Problem)
* [Solution](#Solution)
* [Technologies](#Technologies)
* [Usage](#Usage)
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

 - Result - A file "dns_records.csv" will be created in the current working directory:

> name,type,port,proto,ttl,service,prio,value
> staging60.test,A,NA,NA,86400,NA,NA,34.90.154.249 
> staging60.test,TXT,NA,NA,14400,NA,NA,v=spf1 +a +mx +ip4:35.204.243.180 include:_spf.mailspamprotection.com ~all


## License

[MIT](https://choosealicense.com/licenses/mit/)
