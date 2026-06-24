import pytest
import allure


@pytest.mark.progress_bar_page
def test_page_content(progress):
    allure.dynamic.title('Test page content')
    progress.check_page_content()


@pytest.mark.progress_bar_page
@pytest.mark.parametrize('percent', [75, 80, 90])
def test_progress_bar(progress, percent):
    allure.dynamic.title(f'Test progress bar. expected - {percent}')
    progress.progress_bar_actions(percent)
