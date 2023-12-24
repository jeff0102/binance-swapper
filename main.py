import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from utils.prepare_env import get_api_key_binance
import tkinter as tk

def button1_function():
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, "assets show")

def button2_function():
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, "successful transfer to spot wallet")

def button3_function():
    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, "assets traded to USDT and sended to funding wallet")

def change_color_button(button):
    button.config(background="red")

# Initialize Tkinter Window
window = tk.Tk()
window.title("Tkinter GUI Example")

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
"""
config_logging(logging, logging.DEBUG)

api_key, api_secret = get_api_key_binance()

spot_client = Client(api_key, api_secret)
logging.info(
#    spot_client.user_universal_transfer(asset="USDT", amount=1, type="FUNDING_MAIN")
) """