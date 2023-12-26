import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from binance.error import ClientError as ClientErrorBinance
from utils.prepare_env import get_api_key_binance
import tkinter as tk

config_logging(logging, logging.DEBUG)

api_key, api_secret = get_api_key_binance()
spot_client = Client(api_key, api_secret)
current_whitelist = []

def button1_function():
    try:
        available_assets = spot_client.funding_wallet()
    except ClientErrorBinance as error:
        logging.error(
            "Error with the payment methods. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )
        return

    assets = []
    for asset in available_assets:
        item = list(asset.items())[:2]
        assets.extend(item)

    result = "assets:\n"
    for asset in assets:
        result += f"{asset[0]}: {asset[1]}\n"

    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, result)


def button2_function():
    try:
        available_assets = spot_client.funding_wallet()
        print(available_assets)
    except ClientErrorBinance as error:
        logging.error(
            "Error with the payment methods. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )
        return

    for asset in available_assets:
        if asset["asset"] == "USDT":
            continue

        try:
            spot_client.user_universal_transfer(asset=asset["asset"], amount=asset["free"], type="FUNDING_MAIN")
        except ClientErrorBinance as error:
            logging.error(
                "Error with the payment methods. status: {}, error code: {}, error message: {}".format(
                    error.status_code, error.error_code, error.error_message
                )
            )
            continue
        current_whitelist.append(asset["asset"])
    print(current_whitelist)
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, "successful transfer to spot wallet")

def button3_function():
    try:
        spot_assets = spot_client.user_asset()
    except ClientErrorBinance as error:
        logging.error(
            "Error with the payment methods. status: {}, error code: {}, error message: {}".format(
                error.status_code, error.error_code, error.error_message
            )
        )
        return

    for asset in spot_assets:
        if asset["asset"] not in current_whitelist:
            continue
        else:
            symbol = asset["asset"] + "USDT"
            try:
                trade_info = spot_client.exchange_info(symbols=[symbol])
                filters = trade_info.get("filters", [])
                for filt in filters:
                    if filt.get("filterType") == "LOT_SIZE":
                        print(filt)
                        step_size = float(filt.get("stepSize"))
                        print(filt.get("stepSize"))
                        break
            except ClientErrorBinance as error:
                logging.error(
                    "Error with the payment methods. status: {}, error code: {}, error message: {}".format(
                        error.status_code, error.error_code, error.error_message
                    )
                )
                continue
            print(step_size)
            quantity = asset["free"]
            print(quantity)
            if quantity % step_size != 0:
                quantity = int(quantity / step_size) * step_size

            params = {
                "symbol": symbol,
                "side": "SELL",
                "type": "MARKET",
                "quantity": quantity,
            }
            print(params)
            try:
                spot_client.new_order(**params)
            except ClientErrorBinance as error:
                logging.error(
                    "Error with the payment methods. status: {}, error code: {}, error message: {}".format(
                        error.status_code, error.error_code, error.error_message
                    )
                )
                continue


    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, "assets traded to USDT and send to funding wallet")

def change_color_button(button):
    button.config(background="red")

# Initialize Tkinter Window
window = tk.Tk()
window.title("swapper alpha 0.01")

# Create the frame for the buttons
button_frame = tk.Frame(window)
button_frame.pack(pady=20)

# Create buttons
button1 = tk.Button(button_frame, text="See available assets", background="green", command=button1_function, height=2, width=20)
button1.pack(side=tk.TOP, padx=10, pady=5)
button1.bind("<Button-1>", lambda event, button=button1: change_color_button(button))

button2 = tk.Button(button_frame, text="Send the assets to spot wallet", background="green", command=button2_function, height=2, width=20)
button2.pack(side=tk.TOP, padx=10, pady=5)
button2.bind("<Button-1>", lambda event, button=button2: change_color_button(button))

button3 = tk.Button(button_frame, text="sent USDT to funds", background="green", command=button3_function, height=2, width=20)
button3.pack(side=tk.TOP, padx=10, pady=5)
button3.bind("<Button-1>", lambda event, button=button3: change_color_button(button))

# Square Text area to display the results
text_result = tk.Text(window, height=20, width=50)  # Adjust the height and width to get a square shape
text_result.pack(pady=10)

window.geometry("500x600") # Adjust the size of the window to fit the square display and buttons

window.mainloop()

