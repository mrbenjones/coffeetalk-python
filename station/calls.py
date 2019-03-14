from station.models import *
from station import db
import random
from sqlalchemy import or_

def callers_for_code(code):
    """
    Return all users matching the code.
    :param code:
    :return:
    """
    return db.session.query(Caller).filter(Caller.code==code).all()

def call_data_for_code(code):
    """
    Return callee, question, and call for the code of the caller.

    :param code:
    :return: A dictionary with keys pointing to the caller object being called, and the question asked.
    """

    return [rq for c in callers_for_code(code) for rq in recipient_question_coroutine(c)]

def recipient_question_coroutine(caller):
    """

    :param caller:
    :return:
    """
    calls = db.session.query(Call).filter(Call.caller==caller.caller).all()
    for call in calls:
        question = db.session.query(Question).get(call.question)
        callee = db.session.query(Caller).get(call.callee)
        yield {'question': question.text,
               'callee' : callee.full_name,
               'email' : callee.email}


def prior_links(caller):
    """
    Return a list of the caller pkids linked to a given caller from dead calls.
    :param caller:
    :return: a list of ids from the caller table.
    """
    outgoing = set(db.session.query(Call).filter(Call.caller==caller.caller).all())
    incoming = set(db.session.query(Call).filter(Call.callee==caller.caller).all())
    return list(outgoing.union(incoming))

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
    """

    :return: a list of all callers.
    """
    return db.session.query(Caller).all()

def available_callers():
    """
    Give the list of callers not in an active call.
    :return: a list of callers without active calls.
    """
    return [c for c in all_callers() if not(caller_active(c))]


def previously_assigned(caller):
    """
    Return true if there is an inactive call between caller and callee
    :param caller:
    :param callee:
    :return: true if there has been a call between caller and callee.  False otherwise.
    """


def create_call_list(caller_pool = None):
    """
    Return a list of calls assigned from the list of potential callers.
    Generate the list, shuffle them to create order, and then link each person to
    the first person they haven't been linked to before
    :return:
    """
    if (caller_pool is not None):
        pool_of_callers = caller_pool
    else:
        pool_of_callers = available_callers()

    random.shuffle(pool_of_callers)
    new_calls = []
    N = len(pool_of_callers)
    for (i,c) in enumerate(pool_of_callers):
        links = prior_links(c)
        j=0
        while(j<N):
            d = pool_of_callers[(i+j) % N]
            if (d not in links):
                new_calls.append(create_call(c,d))
                break
            j+=1
    return new_calls


