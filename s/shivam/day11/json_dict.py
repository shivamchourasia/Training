import json
#import requests as r
#g=r.get("http://122.181.186.42:9200")
json_str={"hari":{"aliases":{},"mappings":{},"settings":{"index":{"index":"hari","creation_date":"1485316834483","number_of_shards":"5","number_of_replicas":"1","version":{"created":"1070299"},"uuid":"JiES6mbfQgWTYwtZjKBfBg"}},"warmers":{}}}
json_dict={}
json_dict=json.load(json_str)
