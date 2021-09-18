*** Settings ***
Library     SeleniumLibrary
Resource    ../POM/Resource/Registrationkeys.robot

*** Variables ***
${url}    http://demo.guru99.com/test/newtours/register.php
${browser}    firefox

*** Test Cases ***
Registration
    Opening Browser    ${url}   ${browser}
    Insert firstname    Jack
    sleep    1 second
    Insert lastname    Johnson
    sleep    1 second
    Insert phone    11189572941
    sleep    1 second
    Insert email    JJ111@testmail.com
    sleep    1 second
    Insert address    14th,Baker Street
    sleep    1 second
    Insert city    Charlotte
    sleep    1 second
    Insert state    North Carolina
    sleep    1 second
    Insert postal     28105
    sleep    1 second
    Select country    UNITED STATES
    sleep    1 second
    Insert username regis     JJ111
    sleep    1 second
    Insert password regis     JJ1111
    sleep    1 second
    Insert confirm password    JJ1111
    sleep    1 second
    Click submit
    sleep    1 second
    Register success
    sleep    1 second
    Closing Browser