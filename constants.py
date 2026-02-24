from flask import Flask


class CustomApp(Flask):
    def __init__(self, *args, **kwargs):
        super(CustomApp, self).__init__(*args, **kwargs)
        self.logger.setLevel("DEBUG")
        self.logger.debug("initializing app")
        self.secret_key = "TESTING-GENERATE-LATER╚"


app = CustomApp("app")
