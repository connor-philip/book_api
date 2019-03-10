import os


def before_feature(context, feature):
    # Add some common filepaths to the context
    context.featuresDir = os.path.dirname(os.path.abspath(__file__))
    context.featureTestsDir = os.path.abspath(os.path.join(context.featuresDir, ".."))
    context.testDataDir = os.path.join(context.featureTestsDir, "test_data")
    context.BaselineDir = os.path.join(context.testDataDir, "baselines")


# --no-capture mode still seems to supress the last print.
# This adds an empty print after each step so you don't need to add one.
def after_step(context, step):
    print()
