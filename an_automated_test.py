import traceback
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest
from settings import ENVIRONMENT

MESSAGES = {}
MESSAGES['test_not_found'] = "Test with the name - {0} not found on instructor dashboard".format(ENVIRONMENT.get('test_name'))
MESSAGES['student_list_non_functional'] = "Student List page from instructor dashboard is not showing up correctly"
MESSAGES['best_practices_error'] = "Student doesnt reach on best practices page"

class Base2UTests(unittest.TestCase):

    def setup(self):
        self.driver = webdriver.Chrome(ENVIRONMENT['chromedriver'])
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.implicitly_wait(20)
        self.driver.get(ENVIRONMENT['url'])
        self.driver.implicitly_wait(10)

    def login(self, user):
        try:
            self.wait.until(EC.element_to_be_clickable((By.ID, "email"))).click()
            time.sleep(2)
            #enter email to username textfield
            self.wait.until(EC.element_to_be_clickable((By.ID, "email"))).send_keys(ENVIRONMENT['username'][user])
            self.wait.until(EC.element_to_be_clickable((By.ID, "password"))).send_keys(ENVIRONMENT['password'][user])
            time.sleep(1)
        except TimeoutException, TypeError:
           raise Exception('2U login Page has issues')
        self.wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div/div[2]/form/button"))).click()
        time.sleep(5)
        try:
            self.driver.find_element_by_xpath('//*[@id="header_profile_firstname"]')
        except:
            raise Exception('Coudnt not confirm that user is logged in')

    def tear_down(self):
        self.driver.close()

class InstructorTests(Base2UTests):

    def test_instructor_flow(self):
        #tests if test_name is there in dashboard.
        try:
            err = self.open_dashboard()
        except Exception as e:
            type_, value_, traceback_ = sys.exc_info()
            line = traceback.format_exc(traceback_)
            self.fail(line)
        try:
            test_element = self.driver.find_element_by_xpath('//*[@id="column_header_5551"]/td[1]/a')
        except NoSuchElementException as e:
            self.fail(MESSAGES['test_not_found'])
        self.assertEqual(test_element.get_attribute('innerText'), ENVIRONMENT.get('test_name'), msg=MESSAGES['test_not_found'])


        #now go to student list page and see if that has title of the same test that was clicked.
        self.open_student_list()
        try:
            test_element = self.driver.find_element_by_xpath('')
        except:
            self.fail(MESSAGES['student_list_non_functional'])
        self.assertEqual(test_element.get_attribute('innerText'), ENVIRONMENT['test_name'], msg=MESSAGES['student_list_non_functional'])
        self.tear_down()

        #can add that part to assertions as well where other things are also tested in student list page. Ideally that should be cought by other functional tests and not by 2U integration tests

    def open_dashboard(self):
        """
        Opens dashboard for instructor tests. Will return error message or false
        """
        #TODO - This directly opens proctoring url. Use clicks and reach proctoring url the way user will do. Right now 2U hasnt implemented the flow completely. - Ankit 30th May 2015
        self.setup()
        self.login('instructor')
        self.driver.get(ENVIRONMENT['url'] + '/proctoring/2u/launch')
        return False

    def open_student_list(self):
        elm_test = self.driver.find_element_by_xpath('//*[@id="column_header_5551"]/td[1]/a')
        elm_test.click()



class StudentTests(Base2UTests):

    def test_student_flow(self):
        self.setup()
        self.login('student')
        self.open_proctored_quiz()
        try:
            test_element = self.driver.find_element_by_xpath('')
        except:
            self.fail(MESSAGES['best_practices_error'])

    def open_proctored_quiz(self)
        self.driver.get('{0}/proctoring/2u/launch?custom_test_id={1}&interrupt_next_url={2}'.format(ENVIRONMENT['url'], ENVIRONMENT['test_id'], 'https://some-url-for-quiz'))

if __name__ == '__main__':
    instructor = unittest.TestSuite()
    student = unittest.TestSuite()
    instructor.addTest(InstructorTests('test_instructor_flow'))
    student.addTest(StudentTests('test_student_flow'))
    suite = eval(sys.argv[1])
    unittest.TextTestRunner().run(suite)
