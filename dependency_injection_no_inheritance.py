"""
ok, now let's try something with standard use of __init__(selgf)
"""

class MarketData():
    def get_yield_curve(self):
        return ("I am a flat Yield Curve")

class Instrument():
    def get_pay_off(self):
        return "je suis un zero coupon"

class Pricer():

    def __init__(self, market_data, intrument):
        self.market_data = market_data
        self.intrument = intrument

    def describe_intent(self):
        """
        This function shows that if there is no overlapping in the name of methods that we call with super().XX()
        the multiple inheritance can be used to perform dependency injection

        :return: None
        """
        print(self.intrument.get_pay_off())
        print(self.market_data.get_yield_curve())


mes_market_data = MarketData()
mon_instrument = Instrument()
mon_pricer = Pricer(mes_market_data, mon_instrument)
mon_pricer.describe_intent()


class Cap(Instrument):
    def get_pay_off(self):
        return "I am a cap"

mon_cap = Cap()

mon_pricer = Pricer(mes_market_data, mon_cap)
mon_pricer.describe_intent()
