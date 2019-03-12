from station.models import *
import pytest
from station import db
import hashlib
from station.calls import  *
import json
def test_user_roundtrip():
    onetime = User()
    onetime.set_password("test")
    onetime.email = "test@test.net"
    onetime.username = "testtest"
    assert(onetime.check_password("test"))
    db.session.add(onetime)
    db.session.commit()
    assert(onetime.id>0)
    # now load, delete, and assert
    tobedeleted = db.session.query(User).filter(User.email=="test@test.net").all()[0]
    assert(tobedeleted.id==onetime.id)
    db.session.delete(tobedeleted)
    db.session.commit()

    remaining_list = db.session.query(User).filter(User.email=="test@test.net").all()
    assert(not(remaining_list))

def code_for_caller(caller):
    return hashlib.md5(caller.full_name.encode('utf-16',"ignore")).hexdigest()

def test_code_roundtrip():
    """

    :return:
    """
    call_list = Caller.query.all()
    for caller in call_list:
        corresponding_list = callers_for_code(caller.code)
        assert(caller in corresponding_list)
        assert(len(corresponding_list)>0)
        assert(len(corresponding_list)<2)

def sample_user_for_name(name):
    sample = Caller()
    sample.full_name = "{} YYYYY".format(name.upper())
    sample.email = "{}@xxx.x".format(name)
    sample.apply_code()
    return sample

@pytest.fixture()
def two_test_callers():
    """
    Create two test callers and save them to the database.
    :return:
    """
    test_caller_pool = db.session.query(Caller).filter(Caller.email.endswith("xxx.x"))
    for c in test_caller_pool:
        # delete test caller
        db.session.delete(c)
    db.session.commit()
    test_caller_a = Caller()
    test_caller_b = Caller()
    test_caller_a.full_name = "XXXXX YYYYYY"
    test_caller_b.full_name = "ZZZZZ YYYYYY"
    test_caller_a.email = "xxx@xxx.x"
    test_caller_b.email = "yyy@xxx.x"
    test_caller_a.apply_code()
    test_caller_b.apply_code()
    db.session.add(test_caller_a)
    db.session.add(test_caller_b)
    db.session.commit()
    return([test_caller_a, test_caller_b])

def test_call_linking():
    """
    Test whether call assignment is possible.
    :return:
    """
    test_caller_pool = db.session.query(Caller).filter(Caller.full_name == "XXXXX YYYYYY").all()
    if (test_caller_pool):
        test_caller = test_caller_pool[0]
    else:
        test_caller = Caller()
        test_caller.full_name = "XXXXX YYYYYY"
        test_caller.email = "xxx@xxx.x"
        test_caller.apply_code()
        db.session.add(test_caller)
        db.session.commit()


    call_list = available_callers()
    master_list = Caller.query.all()
    assert(len(call_list)>0)
    assert(len(master_list)>=len(call_list))
    db.session.delete(test_caller)
    db.session.commit()
    test_caller_pool = db.session.query(Caller).filter(Caller.full_name == "XXXXX YYYYYY").all()
    assert(not(test_caller_pool))

def test_create_call(two_test_callers):
    """

    :return:
    """
    (caller_a,caller_b) = two_test_callers
    try:
        call_out = create_call(caller_a,caller_b)
        call_list = available_callers()
        assert(caller_a not in call_list)
        db.session.delete(call_out)
        db.session.commit()
 #       assert(caller_b not in call_list)
    except:
        assert(False)

    remaining_calls = db.session.query(Call).filter(Call.caller==caller_a.caller).all()
    assert(not(remaining_calls))
    db.session.delete(caller_a)
    db.session.delete(caller_b)
    db.session.commit()

@pytest.fixture
def ten_user_list():
    """

    :return:
    """
    namestrings = ["aaaaaa","bbbbbb","cccccc","dddddd","eeeeee","ffffff",
                   "gggggg","hhhhhh","iiiiii","jjjjjj"]

    users = [sample_user_for_name(u) for u in namestrings]
    for u in users:
        db.session.add(u)
    db.session.commit()
    return users


def test_circle_of_links(ten_user_list):
    call_list = create_call_list(ten_user_list)
    for c in call_list:
        db.session.add(c)
    db.session.commit()
    for c in ten_user_list:
        contacts = call_data_for_code(c.code)
        assert(json.dumps(contacts).startswith("["))
        assert("{" in json.dumps(contacts))
    avc = available_callers()
    intersect = [u for u in ten_user_list if u in avc]
    assert(not(intersect))
    for c in call_list:
        db.session.delete(c)
    db.session.commit()
    avc = available_callers()
    intersect = [u for u in ten_user_list if u in avc]
    assert(intersect)
    for u in ten_user_list:
        db.session.delete(u)
    db.session.commit()
    sample_users = db.session.query(Caller).filter(Caller.email.endswith("xxx.x")).all()

    assert(not(sample_users))

