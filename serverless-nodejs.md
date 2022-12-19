[home](README.md)

# Using Serverless with Node.js

```bash
# Install serverless
> npm install -g serverless

# Initialize project
> sls
```

### Setup localstack
Install localstack dependency

> npm install --save-dev serverless-localstack

Add in serverless.yml -
```yml
plugins:
  - serverless-localstack

custom:
  localstack:
    stages:
      - local
```

### Deploy and invoke hello world function
```bash
> sls deploy --stage local

# Invoking functions
> sls invoke -f <function name> --stage <env>

# Invoking functions locally. Use #2. #1 doesn't work as expected
> sls invoke --function hello --stage local #1
> sls invoke local --function hello         #2

```

### 