from behave import when


@when(u'preencho o campo "{field}"')
def step_impl(context, field):
    ...


@when(u'clico no botão submit')
def step_impl(context):
    ...
