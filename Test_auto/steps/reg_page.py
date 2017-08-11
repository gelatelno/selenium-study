from behave import given, when, then
from common import reg_page_url, start_page_url


@given('Ticketscloud new partner registration page')
def step_impl(context):
	context.url = start_page_url


@when('Select registration')
def step_impl(context):
	pass


@then('Registration page opens')
def step_impl(context):
	context.driver.get(context.url)
