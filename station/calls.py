from station.models import *
from station import db
import random
def callers_for_code(code):
    """
    Return all users matching the code.
    :param code:
    :return:
    """
    return db.session.query(Caller).filter(Caller.code==code).all()


def calls_for_callers(caller):
    """
    Returns a list of call objects for the caller chose, 
    :return: 
    """
    return db.session.query(Call).filter(Call.caller == caller.caller).all()

def caller_active(caller):
    """
    Return True if the caller has an active call.
    :param caller:
    :return:True if caller has an call marked active, false otherwise.
    """
    calls = db.session.query(Call).filter(Call.caller==caller.caller).filter(Call.active).all()
    return (bool(calls))

def draw_random_question():
    """
    Draw a question shuffled at random from the whole list.
    :return:
    """
    question_list = Question.query.all()
    return random.choice(question_list)

def create_call(caller,callee,question=None):
    """

    :param caller:
    :param callee:
    :return:
    """
    new_call = Call()
    new_call.active=True
    new_call.caller=caller.caller
    new_call.callee=callee.caller
    if (question is None):
        question = draw_random_question()
    new_call.question = question.question
    db.session.add(new_call)
    db.session.commit()
    return new_call

def all_callers():
    return db.session.query(Caller).all()

def available_callers():
    """
    Give the list of callers not in an active call.
    :return: a list of callers without active calls.
    """
    return [c for c in all_callers() if not(caller_active(c))]

def create_call_list():
    """
    Return a list of calls assigned from the list of potential callers.
    Generate the list, shuffle them to create order, and then link each person to
    the first person they haven't been linked to before
    :return:
    """
    pool_of_callers = available_callers()
    random.shuffle(pool_of_callers)
    return []