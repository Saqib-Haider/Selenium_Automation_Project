*** Settings ***
Library     SeleniumLibrary
Variables    ../POM/Locators/locator.py

*** Keywords ***
Opening Browser
    [Arguments]    ${url}   ${browser}
    open browser     ${url}    ${browser}
    maximize browser window
    set selenium speed    0.4 seconds

Input Login Username
    [Arguments]    ${username}
    input text    ${username_login}    ${username}

Input Login Password
    [Arguments]    ${password}
    input text    ${password_login}    ${password}


Click Login
    click button     ${button_login}


Login Success
    page should contain    Login Successfully

Closing Browser
    close browser