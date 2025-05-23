from behave import given, when, then
from utils.excel_util import ExcelUtil
from pages.login_page import LoginPage
from selenium import webdriver

@given("the Excel file is loaded")
def step_load_excel(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.saucedemo.com/")
    context.driver.maximize_window()
    context.excel = ExcelUtil("D:\\Automation\\PAT-EB-6\\Behave_Excel_Demo\\data\\test_data.xlsx", "Sheet1")
    context.login_page = LoginPage(context.driver)

@when("I try to login with all data sets")
def step_login_all_sets(context):
    for i in range(2, context.excel.get_row_count() + 1):
        username = context.excel.read_data(i, 1)
        password = context.excel.read_data(i, 2)
        context.login_page.login(username, password)

        if context.login_page.is_login_successful():
            context.excel.write_data(i, 3, "Pass")
            context.driver.back()
        else:
            context.excel.write_data(i, 3, "Fail")
            context.driver.refresh()

@then("the login results should be written back to Excel")
def step_close(context):
    context.driver.quit()
