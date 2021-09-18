*** Settings ***
Library     SeleniumLibrary
Variables    ../POM/Locators/locator.py

*** Keywords ***
Opening Browser
    [Arguments]    ${url}    ${browser}
    open browser    ${url}    ${browser}
    maximize browser window

Insert firstname
    [Arguments]    ${firstname}
    input text    ${firstname_regis}     ${firstname}

Insert lastname
    [Arguments]    ${lastname}
    input text    ${lastname_regis}    ${lastname}

Insert phone
    [Arguments]    ${phone}
    input text    ${phone_regis}     ${phone}

Insert email
    [Arguments]    ${email}
    input text    ${email_regis}     ${email}

Insert address
    [Arguments]    ${address}
    input text    ${address_regis }     ${address}


Insert city
    [Arguments]    ${city}
    input text    ${city_regis}     ${city}


Insert state
    [Arguments]    ${state}
    input text    ${state_regis}     ${state}

Insert postal
    [Arguments]    ${postal}
    input text    ${postal_regis}     ${postal}

Select country
    [Arguments]    ${country}
    select from list by value    ${country_regis}     ${country}

Insert username regis
    [Arguments]    ${username}
    input text    ${username_regis}     ${username}

Insert password regis
    [Arguments]    ${password}
    input text    ${password_regis}     ${password}

Insert confirm password
    [Arguments]    ${c_password}
    input text    ${confirm_password}     ${c_password}

Click submit
    click button    ${button_regis}

Register success
    page should contain    Thank you for registering

Closing Browser
    close browser