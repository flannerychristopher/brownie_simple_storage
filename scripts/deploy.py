from brownie import accounts, config, SimpleStorage
import os


def deploy_simple_storage():
    # account = accounts.add(config["wallets"]["from_key"])
    account = accounts[0]
    print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(15, {"from": account})
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)


def main():
    deploy_simple_storage()
    print("hi")
