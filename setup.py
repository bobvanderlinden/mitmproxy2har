from setuptools import setup

setup(
    name='mitmjson',
    version='0.1',
    py_modules=['mitmjson'],
    install_requires=[
        'Click',
        'mitmproxy'
    ],
    entry_points='''
        [console_scripts]
        mitmjson=mitmjson:cli
    ''',
)
