import pytest


@pytest.mark.css_selectors_page
def test_page_content(css):
    css.check_main_page_content()
    css.check_b1_content()
    css.check_b2_content()
    css.check_b3_content()
    css.check_b4_content()
    css.check_b5_content()
    css.check_b6_content()
    css.check_b7_content()
    css.b7_check_status()


@pytest.mark.css_selectors_page
def test_b1_button(css):
    css.b1_click_on_btn()


@pytest.mark.css_selectors_page
def test_b2_buttons(css):
    css.b2_click_on_btn1()
    css.b2_click_on_btn2()
    css.b2_click_on_btn3()


@pytest.mark.css_selectors_page
def test_b3(css):
    name = 'Name'
    email = 'Email'

    css.b3_fill_fields(name, email)
    css.b3_check_fields_data(name, email)

    css.b3_check_chip_status(1, True)
    css.b3_check_chip_status(2, False)

    css.b3_click_on_link()


@pytest.mark.css_selectors_page
def test_b6(css):
    css.check_is_btn1_visible()
    css.check_is_bnt2_not_displayed()
    css.check_is_bnt3_not_visible()
    css.check_is_bnt4_not_visible()
    css.check_is_bnt5_to_be_hidden()
    css.check_is_bnt6_to_be_offscreen()


@pytest.mark.css_selectors_page
@pytest.mark.parametrize(
    'dom_level',
    [1, 2, 3],
)
def test_b7(css, dom_level):
    data = 'Some input 123'

    css.b7_click_on_btn(dom_level)

    css.b7_fill_field(dom_level, data)
    css.b7_check_field(dom_level, data)
