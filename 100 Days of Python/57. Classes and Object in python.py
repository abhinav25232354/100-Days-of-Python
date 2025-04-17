class Company:
    name = "XYZ Company"
    net_turnover = 10000000000000000000
    def info(self):
        print(f"Company Name: {self.name}")
        print(f"Company Turnover: {self.net_turnover}")

obj = Company()
obj.info()