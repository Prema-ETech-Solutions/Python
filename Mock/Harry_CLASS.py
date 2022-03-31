class A:
    id = 100
    def Data(self):
        print(f"Hello {self.id} and {self.name}")
    @staticmethod
    def Hello():
        print("HELLO")
b = A()
b.name = "PREM"
A.Data(b)
A.Hello()