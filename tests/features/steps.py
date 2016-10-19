from lettuce import step, world, before
from nose.tools import assert_equals
from lxml import html

from microblog.controllers import app


@before.all
def before_all():
    world.app = app.test_client()


@step(u'When I visit \'([^\']*)\' path')
def when_i_visit_group1_path(step, path):
    world.response = world.app.get('{}'.format(path))


@step(u'Then I should get a \'([^\']*)\' response')
def then_i_should_get_a_group1_response(step, expected_status_code):
    assert_equals(world.response.status_code, int(expected_status_code))


@step(u'And title set to \'([^\']*)\'')
def and_title_set_to_group1(step, expected_title):
    dom = html.fromstring(world.response.get_data(as_text=True))
    title = dom.cssselect('title')[0].text
    assert_equals(title, expected_title)
