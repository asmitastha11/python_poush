
class burger:
    def bun(self):
        print('bun')
        return self
    def patty(self):
        print("Patty")
        return self
    def sause(self):
        print("Sause")
        return self
burger1 = burger()
# Normal Method
burger1.bun()
burger1.sause()
burger()
burger1.bun()
burger1.bun()
# method chain
print("\nUsing Method chain")
burger1.bun().sause().patty().sause().bun()
        