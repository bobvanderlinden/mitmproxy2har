from setuptools import setup

setup(
    name='mitmproxy2har',
    version='0.1',
    py_modules=['mitmproxy2har'],
    install_requires=[
        'Click',
        'mitmproxy'
    ],
    entry_points='''
        [console_scripts]
        mitmproxy2har=mitmproxy2har:cli
    ''',
)
