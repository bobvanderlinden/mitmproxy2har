from setuptools import setup

setup(
    name='mitmjson2har',
    version='0.1',
    py_modules=['mitmjson2har'],
    install_requires=[
        'Click',
        'mitmproxy'
    ],
    entry_points='''
        [console_scripts]
        mitmjson2har=mitmjson2har:cli
    ''',
)
