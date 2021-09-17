*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}    https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F
${browser}    firefox
*** Keywords ***
Opening Browser
    open browser    ${url}    ${browser}
    set selenium speed    0.4 seconds
    maximize browser window

Logging into the page
    go to    ${url}

Input username
    [Arguments]    ${username}
    input text    id:Email    ${username}

Input passwd
    [Arguments]    ${password}
    input text    id:Password    ${password}


Login button
    click element    xpath:/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button


Error message
    page should contain    Login was unsuccessfu

Closing Browser
    close browser
