class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f'Email: {self.email}')
        print(f"Age: {self.age}")
        print(f"Rewards member: {self.is_rewards_member}")
        print(f"Gold card points: {self.gold_card_points}")
        print("")
        return self

    def enroll(self):
        if self.is_rewards_member == True:
            print(f"{self.first_name} is already a member")
            print("")
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
        return self

    def spend_points(self,amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
            print(f"{self.first_name} has {self.gold_card_points} points left")
            print("")
        else:
            print("Not enough points")
            print("")
        return self

user1 = User("Kalvin", "Tang", "kt@gmail.com", 29)
user2 = User("Sheryl", "Crispo", "CrispySher@gmail.com", 26)
user3 = User("Leeroy", "Jenkins", "WOW@blizzard.com", 55)

user1.display_info().enroll().display_info().enroll().spend_points(50).display_info()

user2.enroll().spend_points(80).display_info()

user3.spend_points(100).display_info()

