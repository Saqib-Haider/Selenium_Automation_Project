*** Settings ***
Library     SeleniumLibrary
Resource    ../POM/Resource/Pagekeys.robot

*** Variables ***
${url}  http://demo.guru99.com/test/newtours/
${browser}  firefox



*** Test Cases ***
Login
    Opening Browser    ${url}    ${browser}
    Input Login Username    mercury
    Input Login Password    mercury
    Click Login
    Login Success
    Closing Browser