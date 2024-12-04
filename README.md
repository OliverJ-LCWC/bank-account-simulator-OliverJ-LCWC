[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17429882)
# Bank Account Simulator
Create a class called Bank_account to simulate bank account operations. The class will have the following attributes:

* `balance` - default value of zero (but can start as any other non-negative value)
* `owner`

You __must__ ensure that both of these attributes are _private_

This means you also need to create suitable `get` method for both of these attribtues, but only create a `set` method for the owner attribute, as the `deposit` and `withdraw` methods below will take the place of `set_balance`

You will also have three methods that can be carried out:

* deposit
* withdraw

The withdraw method should prevent withdrawing an amount greater than the account balance

## Examples
```
account = Bank_account("Alice")
print(account.get_owner())          # ➞ "Alice"
print(account.get_balance())        # ➞ 0

account.deposit(100)
print(account.get_balance())        # ➞ 100

account.withdraw(50)
print(account.get_balance())        # ➞ 50

account.withdraw(100)               # ➞ "Insufficient funds"
print(account.get_balance())        # ➞ 50
```

### Note:
You will __need__ to make use of a default parameter value here to allow the balance to default to zero, refer to this <a href="https://www.w3schools.com/python/python_functions.asp" target="_blank">W3Schools</a> page for more information
