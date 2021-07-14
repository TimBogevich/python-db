from db import DB

def main():
  users = DB("data/users.json")
  accounts = DB("data/accounts.json")

  join = users.join_left_hash(accounts, "id")
  result = join.filter("iban", "==", "AD26 4494 9767 SP2E BCOY EZKB")

  # print joined values
  print(result.data)


if __name__ == "__main__":
  main()