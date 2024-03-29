from setuptools import setup, find_packages

setup(
    name='your_package_name',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'aiohttp==3.8.4',
        'aiosignal==1.3.1',
        'async-timeout==4.0.2',
        'attrs==22.2.0',
        'certifi==2022.12.7',
        'charset-normalizer==3.1.0',
        'frozenlist==1.3.3',
        'idna==3.4',
        'multidict==6.0.4',
        'openai==1.12.0',
        'python-dotenv==1.0.0',
        'requests==2.28.2',
        'tqdm==4.65.0',
        'urllib3==1.26.15',
        'yarl==1.8.2',
    ],
    entry_points={
        'console_scripts': [
            'askgpt=askgpt:main',
        ],
    },
)
