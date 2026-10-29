import pandas as pd
import requests

# The API this brick reads: change it to yours. In the browser, the API must let pages from other
# sites read its answers (CORS). Don't write a key into the code, which goes into what you share.
BASE_URL = 'https://api.frankfurter.dev/v1'
TIMEOUT_SECONDS = 10


def handle(base: str = 'AUD') -> pd.DataFrame:
    #ABCD
    print("helloxxx")
    '''The latest reference rates for one unit of the base currency, one row per currency'''
    try:
        response = requests.get(f'{BASE_URL}/latest', params={'base': base}, timeout=TIMEOUT_SECONDS)
    except requests.RequestException as err:
        # In the browser, a host that doesn't let other sites read its answers (CORS) fails here too
        raise RuntimeError(f'The API could not be reached: {err}. In the browser, the API must also allow '
                           'other sites to read its answers (CORS); without that, the brick runs only in multi-user.') from err
    if response.status_code != 200:
        raise RuntimeError(f'The API returned HTTP {response.status_code}: {response.text[:300]}')
    rates = response.json().get('rates', {})
    return pd.DataFrame({'rate': rates}).rename_axis('currency')


brick_kind = 'link'
