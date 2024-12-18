# kyfromabove-on-aws-examples
This repo contains examples of how to access KyFromAbove hosted on AWS's open data registry.  You can find the sample notebooks in the [example folder](examples).

## Resources

[KyFromAbove Open Data Registry on AWS](https://registry.opendata.aws/kyfromabove/)<br>
KyFomAbove AWS [Open Data Docs](https://github.com/awslabs/open-data-docs/tree/main/docs/kyfromabove)<br>
[KyFromAbove AWS Data Explorer](https://kyfromabove.s3.us-west-2.amazonaws.com/index.html)

Installing the AWS Command Line Interface, or [AWSCLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).  This will assist with the use of the AWS Python SDK.<br>
**You do not need an AWS Account to install/use the CLI**

## Set up your environment

1. Clone this repo:
```bash
git clone https://github.com/ianhorn/kyfromabove-on-aws-examples.git
cd kyfromabove-on-aws-examples
```

Create a python environment and activate it. Make sure to use the correct commands for mac/linux or windows.

On Mac/Linux
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
On Windows
```cmd
python3 -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

### Samples

1. Clip a tile index layer to an area of interest [notebook](examples/clip_tiles_to_boundary.ipynb).


