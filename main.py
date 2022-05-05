import sentry_sdk
sentry_sdk.init(
    "https://9a0299d9fdad42f08a39354c2bd271d8@o1233801.ingest.sentry.io/6382827",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    environment="development",
    release="myapp@1.0.0",
    debug=False
)

if __name__ == "__main__":
    division_by_zero = 3 / 0
