from behave import given, when, then
from main import TestGenerator
from ast import literal_eval


@given('the following characteristics')
def step_given_characteristics(context):
    characteristics = {}
    for row in context.table:
        characteristics[row['characteristic']] = row['values'].split(', ')
    context.generator = TestGenerator(characteristics)


@when('I generate ACoC test cases')
def step_when_generate_acoc(context):
    context.result = context.generator.ACoC()


@when('I generate ECC test cases')
def step_when_generate_ecc(context):
    context.result = context.generator.ECC()


@given('the base choice is')
def step_given_base_choice(context):
    context.base_choice = {row['characteristic']: row['value'] for row in context.table}


@when('I generate BCC test cases')
def step_when_generate_bcc(context):
    context.result = context.generator.BCC(context.base_choice)


@given('the base tests are')
def step_given_base_tests(context):
    context.base_tests = [tuple(row['base_tests'].split(', ')) for row in context.table]


@when('I generate MBCC test cases')
def step_when_generate_mbcc(context):
    context.result = context.generator.MBCC(context.base_tests)


@then('the result should be')
def step_then_result_should_be(context):
    expected = [tuple(row['result'].split(', ')) for row in context.table]
    assert set(context.result) == set(expected), f"Expected {set(expected)}, but got {set(context.result)}"
