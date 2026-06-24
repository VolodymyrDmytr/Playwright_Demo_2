import pytest
import allure


@pytest.mark.animated_button_page
def test_page_content(animated):
    allure.dynamic.title('Test page content')
    animated.check_page_content()


@pytest.mark.animated_button_page
def test_status_text(animated):
    allure.dynamic.title('Test status text')
    animated.check_status_text('Default')

    animated.click_on_target_btn()
    animated.check_status_text('Clicked Static')

    animated.click_on_start_btn()
    animated.check_status_text('Moving')

    animated.click_on_target_btn()
    animated.check_status_text('Clicked Move')

    animated.check_status_text('Done')
