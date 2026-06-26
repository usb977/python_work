class Employee:
    def __init__(self, first, last, payment):
        self.first_ = first
        self.last_ = last
        self.payment_ = payment
    
    def give_raise(self, rise=5000):
        self.payment_ += rise
        return self.payment_