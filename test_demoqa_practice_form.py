import os
from selene import browser, have, be


def test_fill_form(browser_config):
    browser.open('/automation-practice-form')
    browser.element('#firstName').click().should(be.blank).type('Ivan')
    browser.element('#lastName').click().should(be.blank).type('Ivanov')
    browser.element('#userEmail').click().should(be.blank).type('name@example.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').click().should(be.blank).type('8999999999')
    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="1996"]').click()
    browser.element('[class*=month-select]').click()
    browser.element('[class*=month-select] [value="1"]').click()
    browser.element('[class*=day--022]').click()
    browser.element('#subjectsInput').click().type('Eng').press_tab()
    browser.element('[for=hobbies-checkbox-1]').click()
    browser.element('[for=hobbies-checkbox-2]').click()
    browser.element('[for=hobbies-checkbox-3]').click()
    browser.element('[type=file]').send_keys(os.path.abspath('res/img.png'))
    browser.element('#currentAddress').click().should(be.blank).type('Baker Street')
    browser.element('#react-select-3-input').type('Haryana').press_enter()
    browser.element('#react-select-4-input').type('Panipat').press_enter()
    browser.element('#submit').press_enter()
    browser.all('tbody tr td')[1::2].should(
        have.texts('Ivan Ivanov', 'name@example.com', 'Male', '8999999999', '22 February,1996', 'English',
                   'Sports, Reading, Music', 'img.png', 'Baker Street', 'Haryana Panipat'))
