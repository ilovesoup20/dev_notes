
# Serverless Notes


## Setup
```bash
$ npm install -g serverless
```
---
## Commands
```bash
# Deploy all functions
$ sls deploy --stage local --config serverless-image-service.yml

# Deploy single function
$ sls deploy function -f <function name> --stage <stage name>

# Invoke functions
$ sls invoke local -f <function name>
$ sls invoke --stage <stage name> -f <function name>
```
---
## Links

### 12/19/2022
[AWS Lambda Runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html)
### 12/16/2022
[Image Resize Lambda@Edge Function](https://github.com/hoony9x/aws-lambda-edge-img-resize-function)

### - 12/14/2022
[Deploy Serverless to multiple aws accounts](https://seed.run/blog/how-to-deploy-your-serverless-app-into-multiple-aws-accounts.html)

[Deploy Python Lambda functions with .zip file archives](https://docs.aws.amazon.com/lambda/latest/dg/python-package.html)

[ImportError: cannot import name _imaging](https://stackoverflow.com/questions/25340698/importerror-cannot-import-name-imaging)

[Getting PIL/Pillow 4.2.1 to upload properly to AWS Lambda Py3.6](https://stackoverflow.com/questions/45473501/getting-pil-pillow-4-2-1-to-upload-properly-to-aws-lambda-py3-6)

[Creating and sharing Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html)

[Creating New AWS Lambda Layer For Python Pandas Library](https://medium.com/@qtangs/creating-new-aws-lambda-layer-for-python-pandas-library-348b126e9f3e)

[Serverless AWS Lambda Layers](https://www.serverless.com/framework/docs/providers/aws/guide/layers)

[Serverless — AWS Lamda@Edge basic auth](https://medium.com/@dorian599/serverless-aws-lamda-edge-basic-auth-f01a88fe047a)

[Reducing pythons serverless deploy size](https://stackoverflow.com/questions/66038142/serverless-python-requirements-slimtrue-does-nothing-for-dependency-size)

[Lambda@Edge support now available](https://www.serverless.com/blog/lambda-at-edge-support-added)

[Serverless Cloudfront](https://www.serverless.com/framework/docs/providers/aws/events/cloudfront/)

[Serverless Plugin Cloudfront Lambda Edge](https://www.serverless.com/plugins/serverless-plugin-cloudfront-lambda-edge)

[Lambda execution role](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html)

[]

## Notes

Lambda@Edge functions requires CloudFront distribution during deployment.
- Removing lambda functions (`sls remove`) fails if the functions are associated with CloudFront distribution. The functions need to be removed from the distribution or the delete the distribution to successfully run `sls remove`.
  - Too many hurdles to remove functions.
  - Uncertain if `sls` or any plugins have the ability to remove old versioned functions that's not used in a distribution or unassociate functions from distribution for removal.
  - What then?
    - Perhaps Lambda@Edge functions should always deploy new version. A separate process would be needed to delete old versions that's not used in distributions.

- If I deploy (`sls deploy ...`), does it always create new version?

Hardcoding CloudFront distribution in serverless.yml or have serverless generate a distribution during build?

---

# Errors

> **Error:**
> 
> The maximum compressed size of your Lambda function cannot exceed 1 MB for viewer events.
> 
> **Solution**: 
>```
>custom:
>  pythonRequirements:
>    layer: true
>```
> This will separately package the lambda functions and python requirements. Python requirements are packaged as a layer
> ```
> functions:
>  func1: gbike-python-serverless-functions-dev-func1 (30 kB)
>  func2: gbike-python-serverless-functions-dev-func2 (30 kB)
>layers:
>  pythonRequirements: arn:aws:lambda:us-east-1:038417966468:layer:gbike-python-serverless-functions-dev-python-requirements:1
>```

---
> **Error**
>
> The function cannot have a layer. 
>
> **Solution**
> 
> Lambda functions with layers are not supported in Lambda@Edge. [[Link](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/edge-functions-restrictions.html#lambda-requirements-lambda-function-configuration)]
---
> **Error** 
> 
> Your function's execution role must be assumable by the edgelambda.amazonaws.com service principal.
>
> **Solution**
>
> Add this in serverless.yml 
>```
>resources:
>  Resources:
>    IamRoleLambdaExecution:
>      Type: "AWS::IAM::Role"
>      Properties:
>        AssumeRolePolicyDocument:
>          Statement:
>            - Effect: Allow
>              Principal:
>                Service:
>                  - lambda.amazonaws.com
>                  - edgelambda.amazonaws.com
>              Action: sts:AssumeRole
>```
---

![abad](/images/meme.jpeg)