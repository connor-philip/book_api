

def before_feature(context, feature):
    pass
    # Make sure required environments are up


# --no-capture mode still seems to supress the last print.
# This adds an empty print after each step so you don't need to add one.
def after_step(context, step):
    print()
