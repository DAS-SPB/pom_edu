class Links:

    def __init__(self, host):
        self.HOST = host
        self.LOGIN_PAGE = f"{self.HOST}"
        self.INVENTORY_PAGE = f"{self.HOST}/inventory.html"
        self.CART_PAGE = f"{self.HOST}/cart.html"
