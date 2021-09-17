*** Settings ***
Library    SeleniumLibrary
Resource     ../RobotAutomation/keys.robot
Library    DataDriver    ../RobotAutomation/Excel/Login.xlsx

Suite Setup    Opening Browser
Suite Teardown    Closing Browser
Test Template    Invalid Login

*** Test Cases ***
Data Driven Negative Testing using ${username} and ${password}



*** Keywords ***
Invalid Login
    [Arguments]    ${username}   ${password}
    Input username    ${username}
    Input passwd    ${password}
    Login button
    Error message
    Logging into the page