import os


def before_feature(context, feature):
    # Add env variable to context
    context.apiIpAddress = os.environ["testServerIP"]

    # Add target environment variables not added from env variables
    context.protocol = "http"
    context.apiUrl = "{}://{}".format(context.protocol, context.apiIpAddress)

    # Add some common file paths to the context
    context.featuresDir = os.path.dirname(os.path.abspath(__file__))
    context.featureTestsDir = os.path.abspath(os.path.join(context.featuresDir, ".."))
    context.testDataDir = os.path.join(context.featureTestsDir, "test_data")
    context.BaselineDir = os.path.join(context.testDataDir, "baselines")


# --no-capture mode still seems to suppress the last print.
# This adds an empty print after each step so you don't need to add one.
def after_step(context, step):
    print()
