import pytest


@pytest.mark.progress_bar_page
def test_page_content(progress):
    progress.check_page_content()


@pytest.mark.progress_bar_page
@pytest.mark.parametrize('percent', [75, 80, 90])
def test_progress_bar(progress, percent):
    progress.progress_bar_actions(percent)
