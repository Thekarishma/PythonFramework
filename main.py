import unittest
import HtmlTestRunner
import browseractivity
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
from config import  Fusion_URL, IMPLICIT_WAIT_TIME,RESULTS_FOLDER,PASSWORD

import browseractivity
class TestWebBrowser(unittest.TestCase) :

    def setUp(self):
        self.driver = browseractivity.open_url_in_chrome('https://login-exqh-dev8.fa.ocs.oraclecloud.com/')

    def test_login_to_Fusion1(self):
        try:
            #driver=browseractivity.open_url_in_chrome(Fusion_URL)

            browseractivity.click("//button[@id='ssoBtn']",self.driver);
            browseractivity.input("//input[@autocomplete='username']","karishma.patidar@cloud.com",self.driver);
            browseractivity.click("//input[@value='Next']",self.driver);
            browseractivity.input("//input[@name='credentials.passcode']",PASSWORD ,self.driver);
            #browseractivity.click("//input[@value='Verify']");
            #browseractivity.click("//a[@aria-label='Select to get a push notification to the Okta Verify app.']");
            print("Logged in to Fusion")
        except Exception as e:
            raise Exception('Failed to open URL in Chrome. Error: ',e.MESSAGE)



def load_and_run_test(test_name):
    suite = unittest.TestLoader().loadTestsFromName(test_name, TestWebBrowser)
    unittest.TextTestRunner().run(suite)


def tearDown(self):
    browseractivity.quit_chrome(self.driver)


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestWebBrowser))
    runner = HtmlTestRunner.HTMLTestRunner(output=RESULTS_FOLDER)
    runner.run(suite)
    #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=RESULTS_FOLDER))