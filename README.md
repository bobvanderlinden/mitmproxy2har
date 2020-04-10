# mitmproxy2har

A command-line tool to convert mitmproxy recordings to [HAR format](https://en.wikipedia.org/wiki/HAR_%28file_format%29).

## Usage

First record requests and responses using mitmproxy. For instance:

```sh
mitmdump --save-stream-file recording &
http_proxy=http://127.0.0.1:8080 curl http://google.com/
```

Then use `mitmproxy2har` to convert the recording to JSON:

```sh
mitmproxy2har recording > recording.har
```

## Installation

```sh
pip install mitmproxy2har
```

## Development

Use the following to install mitmproxy2har while being able to make changes to `mitmproxy2har.py`:

```sh
python3 -m venv venv
pip install --editable .
```
