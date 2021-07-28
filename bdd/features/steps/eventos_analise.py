from behave import when


@when(u'clico no botão para a próxima página')
def step_impl(context):
    ...


@when(u'clico no botão "{button}"')
def step_impl(context, button):
   ...
