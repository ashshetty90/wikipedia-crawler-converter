from currency_converter import CurrencyConverter

class Converter:

    def convert(self,usd_value, response_values):
        try:
            ccy_conv = CurrencyConverter()
            # converting from USD to DKK  and rounding off to 3 decimal places
            danish_kron_value = round(ccy_conv.convert(float(usd_value), 'USD', 'DKK'), 3)
            return response_values.replace('US$', 'DKK').replace(usd_value, str(danish_kron_value))
        except Exception as e:
            print("Invalid Currency Conversion")