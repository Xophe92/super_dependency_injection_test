"""
ok, now let's try something with multiple inheritance
"""

class MarketData():
    def get_yield_curve(self):
        return ("I am a flat Yield Curve")

class Instrument():
    def get_pay_off(self):
        return "je suis un zero coupon"

class Pricer(MarketData, Instrument):
    def describe_intent(self):
        """
        This function shows that if there is no overlapping in the name of methods that we call with super().XX()
        the multiple inheritance can be used to perform dependency injection

        :return: None
        """
        print(super().get_pay_off())
        print(super().get_yield_curve())


class Cap(Instrument):
    def __init(self):
        print("Cap.__init() has been called !!")

    def get_pay_off(self):
        return "I am a cap"

class PricerCap(Pricer, Cap):
    pass

mon_pricer = Pricer()
mon_pricer.describe_intent()

mon_pricer = PricerCap()
mon_pricer.describe_intent()

help(PricerCap)