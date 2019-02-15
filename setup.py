from distutils.core import setup

setup(name="book_api_modules",
      version="0.0.1",
      author="Connor Philip",
      author_email="connorphilip12@hotmail.com",
      package_dir={"book_api": "program"},
      packages=["book_api.modules.database"]
      )
