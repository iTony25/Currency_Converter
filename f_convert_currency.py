import requests
import tkinter as tk
from tkinter import ttk
import logging



logging.basicConfig(filename='currency_converter.log', level=logging.DEBUG)

def convert_currency(api_key, from_currency, to_currency, amount, result_label):
    base_url = "https://open.er-api.com/v6/latest"
    params = {
        'apikey': api_key,
        'from': from_currency,
        'to': to_currency
    }

    response = requests.get(base_url, params=params)

    # Logare 
    logging.info(f"Requested conversion from {from_currency} to {to_currency} for amount {amount}")

    if response.status_code == 200:
        exchange_rates = response.json()['rates']
        if from_currency in exchange_rates and to_currency in exchange_rates:
            converted_amount = amount * exchange_rates[to_currency] / exchange_rates[from_currency]
            result_label.config(text=f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}", fg="green")
            logging.info(f"Conversion successful. Result: {amount} {from_currency} to {converted_amount:.2f} {to_currency}")
        else:
            result_label.config(text="Unable to perform currency conversion. Please check the currencies and try again.", fg="red")
            logging.error("Invalid currencies selected for conversion.")
    else:
        result_label.config(text="Unable to perform currency conversion. Please check the currencies and try again.", fg="red")
        logging.error(f"Failed to retrieve exchange rates. Status code: {response.status_code}")

def on_convert_button_click():
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()
    api_key = "API"

    
    try:
        amount = float(amount_entry.get())
    except ValueError:
        result_label.config(text="Invalid input for amount. Please enter a valid numeric value.", fg="red")
        logging.error("Invalid input for amount.")
        return

    convert_currency(api_key, from_currency, to_currency, amount, result_label)


    try:
        amount = float(amount_entry.get())
    except ValueError:
        result_label.config(text="Invalid input for amount. Please enter a valid numeric value.", fg="red")
        return

    convert_currency(api_key, from_currency, to_currency, amount, result_label)


#Interfata grafica

root = tk.Tk()
root.title("Currency Converter")
root.configure(bg='#ececec')  



tk.Label(root, text="From Currency:", bg='#ececec').grid(row=0, column=0, padx=10, pady=10)
from_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"], style='TCombobox')  # Stil pentru combobox
from_currency_combobox.grid(row=0, column=1, padx=10, pady=10)
from_currency_combobox.set("USD")

tk.Label(root, text="To Currency:", bg='#ececec').grid(row=1, column=0, padx=10, pady=10)
to_currency_combobox = ttk.Combobox(root, values=["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"], style='TCombobox')  # Stil pentru combobox
to_currency_combobox.grid(row=1, column=1, padx=10, pady=10)
to_currency_combobox.set("EUR")

tk.Label(root, text="Amount:", bg='#ececec').grid(row=2, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert", command=on_convert_button_click, bg='#4caf50', fg='white')  # Stil pentru buton
convert_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="", bg='#ececec')
result_label.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()
