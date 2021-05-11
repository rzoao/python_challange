import argparse

from controllers import LookUpController

my_parser = argparse.ArgumentParser(description="List the content of a folder")


parser = argparse.ArgumentParser()
parser.add_argument("filename")
parser.add_argument("--rdap", action="store_true")
parser.add_argument("--geo", action="store_true")
args = parser.parse_args()


results = LookUpController(args.filename, args.rdap, args.geo).query()
results.write()
# print(json.dumps(vars(results[0]), indent=3))

#r = results[1]

#rdap_url = "https://rdap.arin.net/registry/ip/{}"

#resp = requests.get(rdap_url.format(r))
#print(vars(args))
