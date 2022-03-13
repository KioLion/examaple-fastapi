from app.calculations import *
import pytest

@pytest.fixture
def zero_bank_account():
    return BankAccount()

@pytest.fixture
def bank_account():
    return BankAccount(50)

@pytest.mark.parametrize("num1,num2,expected", [(3,2,5),(7,1,8),(6,5,11)])
def test_add(num1,num2, expected):
    assert add(num1,num2) == expected


def test_divide():
    assert divide(6,3) == 2

def test_substract():
    assert subtract(6,3) == 3

def test_multiplay():
    assert multiply(2,3) == 6



def test_bank_set_initial_amount(bank_account):
    assert bank_account.balance == 50

def test_bank_set_default_amount(zero_bank_account):
    assert zero_bank_account.balance == 0

def test_withdraw(bank_account):
    bank_account.withdraw(20)
    assert bank_account.balance== 30

def test_deposit(bank_account):
    bank_account.deposit(20)
    assert bank_account.balance== 70

def test_collect_intrest(bank_account):
    bank_account.collect_interest()
    assert round(bank_account.balance,5)== 55

@pytest.mark.parametrize("deposited,withdrew,expected", [
    (100,25,125),
    (12,37,25),
    (75,75,50)
    ])
def test_bank_transaction(bank_account, deposited, withdrew, expected):
    bank_account.deposit(deposited)
    bank_account.withdraw(withdrew)
    assert bank_account.balance == expected


def test_withdraw_insufficient_fund(zero_bank_account):
    with pytest.raises(InsufficientFunds):
        zero_bank_account.withdraw(25)