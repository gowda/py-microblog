from lettuce import step, world, before
from nose.tools import assert_equals

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
