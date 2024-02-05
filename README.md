# Binance Swapper

Binance Swapper is a Python application designed to support peer-to-peer (P2P) trading on the Binance platform. Its main functionality is to convert any asset other than USDT into USDT and release it to the user's funding wallet. This feature enables users to easily exchange various assets for USDT.

## Target

The target of this project is to provide users with a convenient way to manage their assets and liquidity. By automating the process of converting assets into USDT and transferring them to the funding wallet, users can streamline their trading activities and access trading capital more efficiently.

## How It Works

1. **Connection to Binance Account:** Users can connect their Binance account using their API key and secret.
2. **Retrieve Available Assets:** The application retrieves a list of available assets from the funding wallet from Binance platform.
3. **Execution of Trades:** The application executes trades to convert selected assets into USDT at MARKET price.
4. **Transfer to Funding Wallet:** The converted USDT is then transferred to the user's funding wallet on Binance, where it can be used for further trading or withdrawn.

By automating this process, Binance Swapper aims to provide users with a seamless experience for managing their assets and participating in P2P trading activities.

## Installation

1. Clone the repository to your local machine.

2. (Optional) Set up a virtual environment to keep dependencies isolated:

3. Install the required packages using pip:

```bash
pip install -r requirements.txt 
```

## Usage

1. Make a copy of the file `example.config.ini` and save it as `config.ini`.
2. Insert your API and Secret keys in the `config.ini` file. For example:
   ```ini
   [keys]
   api_key=YourAPIKeyHere
   api_secret=YourSecretKeyHere
   ```

Run the script:

``` python
python main.py
```

For more detailed information about the Binance Spot API, please visit the [official API documentation](https://binance-docs.github.io/apidocs/spot/en).

