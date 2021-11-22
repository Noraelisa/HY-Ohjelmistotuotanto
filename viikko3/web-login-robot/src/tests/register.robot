*** Settings ***
Resource  resource.robot
Resource  login.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  nora
    Set Password  noranora123
    Set Password Comfirmation  noranora123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password    
    Set Username  mu
    Set Password  nora123
    Set Password Comfirmation  nora123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  maija
    Set Password  nora
    Set Password Comfirmation  nora
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation   
    Set Username  pirjo
    Set Password  maija1234
    Set Password Comfirmation  maija12345
    Submit Credentials
    Register Should Fail With Message  Password and Password confirmation does not match

Login After Successful Registration
    Set Username  risto
    Set Password  noranora123
    Set Password Comfirmation  noranora123
    Submit Credentials
    Register Should Succeed
    Go To Login Page    
    Set Username  risto
    Set Password  noranora123
    Submit Login Credentials
    Login Should Succeed 

Login After Failed Registration
    Set Username  maija
    Set Password  nora
    Set Password Comfirmation  nora
    Submit Credentials
    Register Should Fail With Message  Password too short
    Go To Login Page    
    Set Username  maija
    Set Password  nora
    Submit Login Credentials
    Login Should Fail     

*** Keywords ***
Login Should Succeed
    Main Page Should Be Open

Login Should Fail
    Login Page Should Be Open

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Submit Login Credentials
    Click Button  Login    

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Comfirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}

Create User And Go To Register Page 
    Create User  nora  nora123
    Go To Register Page
    Register Page Should Be Open

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open