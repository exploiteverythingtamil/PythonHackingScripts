import requests
import argparse
import json

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("-i","--ipaddress",help="Enter IP Address TO Track")
    args=parser.parse_args()
    ip=args.ipaddress

    url="http://ip-api.com/json/"+str(ip)
    res=requests.get(url)
    data=json.loads(res.content)
    print("\t[+]IP \t\t ",data['query'])
    print("\t[+]CITY \t\t ",data['city'])
    print("\t[+]ISP \t\t ",data['isp'])
    print("\t[+]COUNTRY \t\t ",data['countryCode'])
    print("\t[+]REG NAME \t\t ",data['regionName'])
    print("\t[+]TIME ZONE \t\t ",data['timezone'])
    print("\t[+]ZIP \t\t ",data['zip'])
    print("\t[+]LAT \t\t ",data['lat'])
    print("\t[+]LON \t\t ",data['lon'])