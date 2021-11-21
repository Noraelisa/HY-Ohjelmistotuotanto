*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  pekka  password6543
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password 
    Input Credentials  user  moikkakalle123
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password 
    Input Credentials  un  password123
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  ville  lyhyt
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  maija  passwordlongenough
    Output Should Contain  Password contains only letters    

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  user  password1234