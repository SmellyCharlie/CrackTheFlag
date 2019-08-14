from distutils.core import setup

setup(
    name="CrackTheFlag",
    version="0.1dev",
    author=["Soul", "SinisterMatrix"],
    author_email=["", "sinistermatrix663@gmail.com"],
    packages=["ctf", "ctflib", "ctflib.test"],
    url="https://github.com/soulctf/CrackTheFlag",
    license="LICENSE",
    description="A module based framework, meant to automate capture the flag solving",
    long_description=open("README.md").read(),
    install_requires=[
        # Install Dependencies
    ]
)