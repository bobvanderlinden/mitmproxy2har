import click
import mitmproxy
from mitmproxy import io
from mitmproxy.exceptions import FlowReadException
import sys
import json

class IteratorAsList(list):
    def __init__(self, it):
        self.it = it
    def __iter__(self):
        return self.it
    def __len__(self):
        return 1

def from_header(pair):
    key, value = pair
    return {
        "key": key,
        "value": value
    }

def from_headers(headers):
    return IteratorAsList(map(from_header, headers.items()))

def from_flow(flow):
    return {
        "request": {
            "http_version": flow.request.http_version,
            "scheme": flow.request.scheme,
            "host": flow.request.host,
            "port": flow.request.port,
            "method": flow.request.method,
            "path": flow.request.path,
            "headers": from_headers(flow.request.headers),
            "text": flow.request.text,
            "timestamp_end": flow.request.timestamp_end,
            "timestamp_start": flow.request.timestamp_start
        },
        "response": flow.response and {
            "status_code": flow.response.status_code,
            "reason": flow.response.reason,
            "headers": from_headers(flow.response.headers),
            "text": flow.response.text,
            "timestamp_end": flow.response.timestamp_end,
            "timestamp_start": flow.response.timestamp_start
        },
        "error": flow.error and str(flow.error)
    }

@click.command()
@click.argument('file')
def cli(file):
    """Converts a mitmproxy file to JSON"""
    with open(file, "rb") as logfile:
        freader = io.FlowReader(logfile)
        try:
            json.dump(IteratorAsList(map(from_flow, freader.stream())), sys.stdout, indent = 4)
            sys.stdout.write("\n")
        except FlowReadException as e:
            print("Flow file corrupted: {}".format(e))
