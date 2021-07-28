from behave import given, then, when

from bdd.modules.auxiliar import cast_table_to_dict


@given(u'que acesse a home')
def access_index_given(context):
    ...


@when(u'acesso a home')
def access_index(context):
    ...


@when(u'clico no botão de "{button_name}"')
def step_impl(context, button_name):
    ...


@then(u'deverá ser enviado o seguinte evento')
def step_impl(context):
    ...


@then(u'deverá ser enviado um evento de Pageview')
def step_impl(context):
    ...
