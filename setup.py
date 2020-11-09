from setuptools import setup, find_packages
import os

from xpcspy.__init__ import __version__


here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'requirements.txt'), 'r') as f:
    requirements = f.readlines()

print("hey hey")
print(f"REQ {requirements}")

setup(
    name='xpcspy',
    description="XPC message interception and more",
    license='Apache-2.0',
    author='hot3eed',
    author_email='hot3eed@gmail.com',
    url='https://github.com/hot3eed/xpcspy',
    keyword=['macos', 'ios', 'xnu', 'xpc', 'frida'],
    version=__version__,
    packages=find_packages(),
    install_requires=requirements,
    entry_points={
        'console_scripts': [
                'xpcspy=xpcspy.console.cli:main'
            ]
        }
)
