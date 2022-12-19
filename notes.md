# Links
[AWS - Deploy Python Lambda functions with .zip file archives](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html)
# Commands
```sh
# Update AWS Lambda Function
> aws lambda update-function-code --function-name coffeebean-python1 --zip-file fileb://lambda-func.zip

# Invoke AWS Lambda Function
> aws lambda invoke --function-name coffeebean-python1 out 

# Install pillow for AWS Lambda Runtime Environment
> pip install --target . --platform manylinux1_x86_64 --only-binary=:all: pillow

# Create AWS Lambda Function
>

# Create AWS Role
>

```
## Issues and fixes
### Conflicting boto versions when installing localstack, awscli and awscli-local
https://stackoverflow.com/a/65799965/20306193
```sh
> pip3 uninstall botocore, s3transfer, boto3
> pip3 install botocore, s3transfer, boto3
```
---

### ImportError: cannot import name _imaging
https://stackoverflow.com/a/65799965/20306193
```sh
> pip3 install --platform manylinux1_x86_64 --only-binary=:all: pillow
```
---

### Your function's execution role must be assumable by the edgelambda.amazonaws.com service principal.
---

### Inaccessible host: `localhost' at port `4566'. This service may not be available in the `us-east-1' region.
https://github.com/localstack/serverless-localstack/issues/125#issuecomment-975875765
```sh
#Fixed by running docker to start localstack
> docker run --rm -it -p 4566:4566 -p 4571:4571 localstack/localstack
```
---

### Creating and activating virtual environment in Python
https://stackoverflow.com/questions/32390291/pip-freeze-for-only-project-requirements
```sh
> python3 -m venv ./venv source myvenv/bin/activate
```
