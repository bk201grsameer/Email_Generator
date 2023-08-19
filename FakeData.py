from faker import Faker
import pandas as pd

fake = Faker()


def createFakeProfile(n):
    try:
        profiles = []
        print("[+] CREATING FAKE PROFILES....")
        for i in range(0, n, 1):
            profiles.append(fake.profile())
        return profiles
    except Exception as ex:
        print("[+] SOMETHING WENT WRONG WHILE CREATING FAKE PROFILE ", str(ex))


def create_Fake_PhoneNumber(n):
    try:
        fake_Numbers = []
        for i in range(0, n, 1):
            fake_Numbers.append(fake.phone_number())
        return fake_Numbers
    except Exception as ex:
        print("[-] SOMETHING WENT WRONG WHILE CREATING FAKE NUMBERS.", str(ex))


def createFakeData(n):
    try:
        profiles = createFakeProfile(n)
        numbers = create_Fake_PhoneNumber(n)
        df = pd.DataFrame(profiles)
        df["phone_number"] = numbers
        df.rename(columns={"mail": "email"}, inplace=True)
        print(df)
        df.to_csv("fake_data.csv", index=False)
    except Exception as ex:
        print("[-] SOMETHING WENT WRONG WHILE CREATING FAKE DATA..", str(ex))

def main():
    createFakeData(10)


main()
