# mitmjson

A command-line tool to convert mitmproxy recordings to JSON format.

## Usage

First record requests and responses using mitmproxy. For instance:

```sh
mitmdump --save-stream-file recording &
http_proxy=http://127.0.0.1:8080 curl http://google.com/
```

Then use `mitmjson` to convert the recording to JSON:

```sh
mitmjson recording > recording.json
```

## Installation

```sh
pip install mitmjson
```


## Development

Use the following to install mitmjson while being able to make changes to `mitmjson.py`:

```sh
python3 -m venv venv
pip install --editable .
```
