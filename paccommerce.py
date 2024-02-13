from tabulate import tabulate
from math import sqrt

class Membership:    
    # inisialisai attribute
    def __init__(self, data):
        self.data = data
    
    @staticmethod
    def ecludian_distance(monthly_expense, req_expense, mothly_income, req_income):
        return sqrt((monthly_expense - req_expense)**2 + (mothly_income - req_income)**2)
    
    @staticmethod
    def count_discount(list_harga, discount):
        discount = int(discount[:-1]) / 100
        return sum(list_harga) - (discount * sum(list_harga))
    
    def _get_requirement_table(self):
        # Membership, Monthly Expense (juta), Monthly Income (juta)
        tables = [
            ["Platinum", 8_000_000, 15_000_000],
            ["Gold", 6_000_000, 10_000_000],
            ["Silver", 5_000_000, 7_000_000],
        ]
        
        return tables
    
    def _get_benefit_table(self):
        tables = [
            ["Platinum", "15%", "Benefit Silver + Gold + Voucher Liburan + Cashback max. 30%"],
            ["Gold", "10%", "Benefit Silver + Voucher Ojek Online"],
            ["Silver", "8%", "Voucher Makanan"],
        ]
        
        return tables
    
    def set_data_register(self, username, monthly_expense, monthly_income):
        self.data[username] = self.get_membership_prediction(
            monthly_expense, 
            monthly_income
        )
    
    # method untuk menampilkan benefit membership
    def get_membership_benefit(self):
        tables = self._get_benefit_table()
        
        header = ["Membership", "Discount", "Another Benefit"]
        
        print("PacCommerce Membership Benefits\n")
        print(tabulate(tables, header))
                  
        
    # method untuk menampilkan requirements membership
    def get_requirements(self):
        tables = self._get_requirement_table()
        header = ["Membership", "Monthly Expense (juta)", "Monthly Income (juta)"]
        
        print("PacCommerce Membership Requirements\n")
        print(tabulate(tables, header))
        
    # method untuk melakukan prediksi membership
    # menggunakan euclidean distance
    def get_membership_prediction(self, monthly_expense, mothly_income):
        requirements = self._get_requirement_table()
        result = {
            "platinum": None,
            "gold": None,
            "silver": None
        }
        
        req_expense = []
        req_income = []
        
        for requirement in requirements:
            req_expense.append(requirement[1])
            req_income.append(requirement[2])
        
        if len(req_expense) == len(req_income) and len(req_expense) == len(result):
            for i in range(len(req_expense)):
                if i == 0:
                    result['platinum'] = self.ecludian_distance(
                        monthly_expense, 
                        req_expense[i], 
                        mothly_income, 
                        req_income[i]
                    )
                elif i == 1:
                    result['gold'] = self.ecludian_distance(
                        monthly_expense, 
                        req_expense[i], 
                        mothly_income, 
                        req_income[i]
                    )
                if i == 2:
                    result['silver'] = self.ecludian_distance(
                        monthly_expense, 
                        req_expense[i], 
                        mothly_income, 
                        req_income[i]
                    )
        else:
            print('Requirement Data Invalid!')
        
        result_index = [
            result['platinum'], 
            result['gold'], 
            result['silver']
        ]

        # Using index() method
        member_index = result_index.index(min(result_index))
        member = None
        
        if member_index == 0:
            member = list(result.keys())[0]
        elif member_index == 1:
            member = list(result.keys())[1]
        elif member_index == 2:
            member = list(result.keys())[2]
            
        return member.capitalize()
    
    # method untuk menampilkan membership yang dimiliki
    # dari database yang dimiliki
    def get_membership_status(self, username):
        for key, value in self.data.items():
            if key == username and value == 'Platinum':
                tables = [self._get_benefit_table()[0]]

                header = ["Membership", "Discount", "Another Benefit"]

                print(f"Halo {key}, berikut status membership kamu: \n")
                print(tabulate(tables, header))
            elif key == username and value == 'Gold':
                tables = [self._get_benefit_table()[1]]

                header = ["Membership", "Discount", "Another Benefit"]

                print(f"Halo {key}, berikut status membership kamu: \n")
                print(tabulate(tables, header))
            elif key == username and value == 'Silver':
                tables = [self._get_benefit_table()[2]]

                header = ["Membership", "Discount", "Another Benefit"]

                print(f"Halo {key}, berikut status membership kamu: \n")
                print(tabulate(tables, header))
    
    # method untuk menghitung final price berdasarkan membership
    def calculate_price(self, username, list_harga):
        membership = None
        for key, value in self.data.items():
            if key == username:
                membership = value
        if membership:
            benefits = self._get_benefit_table()
            discount = {
                "platinum": None,
                "gold": None,
                "silver": None
            }

            for benefit in benefits:
                if benefit[0].lower() == 'platinum':
                    discount['platinum'] = benefit[1]
                elif benefit[0].lower() == 'gold':
                    discount['gold'] = benefit[1]
                elif benefit[0].lower() == 'silver':
                    discount['silver'] = benefit[1]
            
            total_harga = 0
            
            if membership.lower() == 'platinum':
                total_harga = self.count_discount(list_harga, discount['platinum'])
            elif membership.lower() == 'gold':
                total_harga = self.count_discount(list_harga, discount['gold'])
            elif membership.lower() == 'silver':
                total_harga = self.count_discount(list_harga, discount['silver'])

            return total_harga
        else:
            print('Username tidak ditemukan!')
            
if __name__ == "__main__":
    data = {
        'Sumbul': 'Platinum', 
        'Ana': 'Gold', 
        'Cahya': 'Platinum'
    }
    
    admin = Membership(data)
    
    print("\nCheck data users.")
    print(admin.data)
    
    print("\n-------------- Test Case 1 --------------")
    cahya = Membership(data)
    
    print("\nCahya check membership benefits.")
    cahya.get_membership_benefit()
    
    print("\n-------------- Test Case 2 --------------")
    
    print("\nShandy check membership requirement.")
    shandy = Membership(data)
    shandy.get_requirements()
    
    print("\n-------------- Test Case 3 --------------")
    
    print("\nCahya check membership prediction.")
    print(cahya.get_membership_prediction(9_000_000, 12_000_000))
    
    print("\nShandy sign-up.")
    shandy.set_data_register("Shandy", 9000_000, 12_000_000)
    
    print("\nCheck data users.")
    print(admin.data)
    
    print("\nShandy check registration status.")
    shandy.get_membership_status("Shandy")
    
    print("\n-------------- Test Case 4 --------------")
    
    print("\nShandy shopping.")
    list_harga = [150_000, 200_000, 400_000]
    print(shandy.calculate_price("Shandy", list_harga))
    
    print("\n----------- Another Test Case -----------")
    
    print("\nAna check registration status.")
    shandy.get_membership_status("Ana")
    
    print("\nCheck data users.")
    print(admin.data)
    
    print("\nAna shopping.")
    list_harga = [150_000, 200_000, 400_000, 500_000]
    print(shandy.calculate_price("Ana", list_harga))
    
    print("\n-------------- Other User --------------")
    
    print("\nBambang check member requirements.")
    bambang = Membership(data)
    bambang.get_requirements()
    
    print("\nBambang sign-up.")
    bambang.set_data_register("Bambang", 3_000_000, 4_000_000)
    
    print("\nCheck data users.")
    print(admin.data)
    
    print("\nBambang check registration status.")
    bambang.get_membership_status("Bambang")
    
    print("\nBambang shopping.")
    list_harga = [300_000, 150_000, 1_250_000, 15_000]
    print(bambang.calculate_price("Ana", list_harga))