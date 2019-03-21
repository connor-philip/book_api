import urllib.request as request
import urllib.parse as parse
import behave
import json
import os


@behave.given("I go to the \"{endpoint}\" endpoint")
def go_to_endpoint(context, endpoint):
    requestUrl = "{}/{}".format(context.apiUrl, parse.quote(endpoint))
    response = request.urlopen(requestUrl)

    context.endpointResponse = response
    context.responseBodyString = context.endpointResponse.read().decode("utf8")


@behave.then("I receive a JSON response")
@behave.when("I receive a JSON response")
def recieve_json_response(context):
    responseInfo = context.endpointResponse.info()

    assert responseInfo["Content-Type"] == "application/json"
    context.responseBodyJson = json.loads(context.responseBodyString)


@behave.then("the response matches the baseline file \"{baselineFile}\"")
def the_response_matches_the_baseline(context, baselineFile):
    baselineFilePath = os.path.join(context.BaselineDir, baselineFile)

    with open(baselineFilePath, "r") as jsonFile:
        baseLineJson = json.load(jsonFile)
        jsonFile.close()

    assert baseLineJson == context.responseBodyJson


@behave.then("I recieve the status code \"{statusCode}\"")
def then_i_recieve_the_status_code(context, statusCode):

    responseStatusCode = str(context.endpointResponse.code)

    assert responseStatusCode == statusCode
