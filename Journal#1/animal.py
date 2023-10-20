class Cat:
    def __init__(self, arm_length, leg_length,num_eyes, has_tail,is_furry):
        self.arm_length=float(arm_length)
        self.leg_length=float(leg_length)
        self.num_eyes=int(num_eyes)
        self.has_tail=bool(has_tail)
        self.is_furry=bool(is_furry)

    def describe(self):
        print(f"Cat's arm length is:", self.arm_length)
        print(f"Cat's leg length is:", self.leg_length)
        print(f"Cat's number of eyes is:", self.num_eyes)
        if self.has_tail==True:
            print("Cat has a tail")
        else:
            print("Cat doesn't have a tail")
        if self.is_furry==True:
            print("Cat is furry")
        else:
            print("Cat is not furry")

def main():
    c=Cat(arm_length=18.111,leg_length=18.111,num_eyes=2,has_tail=True,is_furry=True)
    return c.describe()

if __name__=="__main__":
    main()
