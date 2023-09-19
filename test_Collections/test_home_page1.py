import pytest
from PageFactories.home_page import TestHomePageVerification


@pytest.mark.usefixtures("setup_one")
@pytest.mark.smoke
class TestHomePage:

    def test_HomePageVerification(self):
        self.hp = TestHomePageVerification(self.driver)
        self.hp.Home_Page_Search_Functionality()
