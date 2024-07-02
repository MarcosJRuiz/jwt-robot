*** Settings ***
Library      OperatingSystem
Library      ../lib/jwt_verifier.py
Variables    ../resource/jwt_variables.py

*** Test Cases ***
Caso1: Valid JWT With Correct Claims
    [Tags]    Caso1
    ${result}=    Verify Jwt    ${VALID_JWT}
    Should Be True    ${result}

Caso2: Invalid JWT Missing Claim
    [Tags]    Caso2
    ${result}=    Verify Jwt    ${INVALID_JWT_MISSING_CLAIM}
    Should Not Be True    ${result}

Caso3: Invalid JWT With Extra Claim
    [Tags]    Caso3
    ${result}=    Verify Jwt    ${INVALID_JWT_EXTRA_CLAIM}
    Should Not Be True    ${result}

Caso4: Invalid JWT With Numeric Name
    [Tags]    Caso4
    ${result}=    Verify Jwt    ${INVALID_JWT_NUMERIC_NAME}
    Should Not Be True    ${result}

Caso5: Invalid JWT With Long Name
    [Tags]    Caso5
    ${result}=    Verify Jwt    ${INVALID_JWT_LONG_NAME}
    Should Not Be True    ${result}

Caso6: Invalid JWT With Non-Prime Seed
    [Tags]    Caso6
    ${result}=    Verify Jwt    ${INVALID_JWT_NON_PRIME_SEED}
    Should Not Be True    ${result}

Caso7: Invalid JWT With Invalid Role
    [Tags]    Caso7
    ${result}=    Verify Jwt    ${INVALID_JWT_INVALID_ROLE}
    Should Not Be True    ${result}
