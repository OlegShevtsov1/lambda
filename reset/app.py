from exchangelib import Account, Credentials, Configuration
from config import EMAIL, PASSWORD, HOST


def reset():
    credentials = Credentials(EMAIL, PASSWORD)
    config = Configuration(server=HOST, credentials=credentials)
    account = Account(EMAIL, credentials=credentials, config=config, autodiscover=False)

    resets = []
    sent = account.sent.all()
    if sent.count():
        resets.append(f'Reset is {sent.count()}')
        # sent.delete()
        breakpoint()

    else:
        resets.append('No resets')

    trash = account.trash.all()
    if trash.count():
        resets.append(f'Reset is {trash.count()}')
        # trash.delete()
    else:
        resets.append('No Resets')
        breakpoint()
    return resets


def lambda_handler(event, context):
    try:
        return {
            "statusCode": 200,
            "body": reset()
        }
    except Exception as e:
        return {
            "statusCode": 401,
            "body": str(e)
        }
