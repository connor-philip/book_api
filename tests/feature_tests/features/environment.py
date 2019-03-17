import subprocess
import os


def before_feature(context, feature):
    # Add env variable to context
    context.apiIpAddress = os.environ["testServerIP"]
    context.dbIpAddress = os.environ["testDatabaseIP"]

    # Add target environment variables not added from env variables
    context.protocol = "http"
    context.apiUrl = "{}://{}".format(context.protocol, context.apiIpAddress)

    # Add some common file paths to the context
    context.featuresDir = os.path.dirname(os.path.abspath(__file__))
    context.featureTestsDir = os.path.abspath(os.path.join(context.featuresDir, ".."))
    context.testDataDir = os.path.join(context.featureTestsDir, "test_data")
    context.BaselineDir = os.path.join(context.testDataDir, "baselines")
    context.dbBson = os.path.join(context.testDataDir, "feature_tests_db",
                                  "bookdb", "books.bson")


def before_scenario(context, step):
    # Ensure the DB is in a clean state
    subprocess.run(["mongo", "--quiet", "bookdb", "--host", context.dbIpAddress, "--port", "27017",
                   "--eval", "db.dropDatabase()"], stdout=subprocess.DEVNULL)
    subprocess.run(["mongorestore", "--quiet", "--host", context.dbIpAddress, "--port", "27017",
                   "--db", "bookdb", "--collection", "books", context.dbBson])


def after_step(context, step):
    # --no-capture mode still seems to suppress the last print.
    # This adds an empty print after each step so you don't need to add one.
    print()
