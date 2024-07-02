import jwt
from jwt.exceptions import InvalidTokenError


def decode_jwt(token):
    return jwt.decode(token, options={"verify_signature": False})


def is_valid_name(name):
    return not any(char.isdigit() for char in name) and len(name) <= 256


def is_valid_role(role):
    return role in ["Admin", "Member", "External"]


def is_prime(number):
    # Implementação para verificar se o número é primo
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def verify_jwt(jwt_token):
    try:
        decoded_jwt = decode_jwt(jwt_token)  # Função para decodificar o JWT
        print(jwt_token)
        print(decoded_jwt)
        if not isinstance(decoded_jwt, dict):
            return False

        # Verificar se o JWT possui todas as claims necessárias
        required_claims = ['Name', 'Role', 'Seed']
        
        if not all(claim in decoded_jwt for claim in required_claims):
            return False
        
        if set(decoded_jwt.keys()) != set(required_claims):
            return False
        
        if not is_valid_name(decoded_jwt['Name']):
            return False

        if not is_valid_role(decoded_jwt['Role']):
            return False

        if not is_prime(int(decoded_jwt['Seed'])):
            return False

        return True
    except (InvalidTokenError, KeyError, ValueError):
        return False


# r =  verify_jwt("eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJTZWVkIjoiNzg0MSIsIk5hbWUiOiJUb25pbmhvIEFyYXVqbyJ9.QY05sIjtrcJnP533kQNk8QXcaleJ1Q01jWY_ZzIZuAg")
# print(r)
# print()
# INVALID_JWT_MISSING_CLAIM = verify_jwt("eyJhbGciOiJIUzI1NiJ9.eyJTZWVkIjoiNzg0MSIsIk5hbWUiOiJUb25pbmhvIEFyYXVqbyJ9.GeH_kHSsRrmTY2MQI0v_NccrkBBLxwX6NJA1P2nKEeA")
# print(INVALID_JWT_MISSING_CLAIM)
# print()
# INVALID_JWT_EXTRA_CLAIM = verify_jwt("eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiTWVtYmVyIiwiT3JnIjoiQlIiLCJTZWVkIjoiMTQ2MjciLCJOYW1lIjoiVmFsZGlyIEFyYW5oYSJ9.cmrXV_Flm5mfdpfNUVopY_I2zeJUy4EZ4i3Fea98zvY")
# print(INVALID_JWT_EXTRA_CLAIM)
# print()
# INVALID_JWT_NUMERIC_NAME = verify_jwt("eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiRXh0ZXJuYWwiLCJTZWVkIjoiODgwMzciLCJOYW1lIjoiTTRyaWEgT2xpdmlhIn0.6YD73XWZYQSSMDf6H0i3-kylz1-TY_Yt6h1cV2Ku-Qs")
# print(INVALID_JWT_NUMERIC_NAME)
# print()
# INVALID_JWT_LONG_NAME = verify_jwt("eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiTWVtYmVyIiwiU2VlZCI6IjE0NjI3IiwiTmFtZSI6Ik1hcmNvcyBSdWl6IGFhYWFhYWFhYWEgYWFhYWFhYWFhYSBhYWFhYWFhYWFhYSBhYWFhYWFhYWFhIGFhYWFhYWFhYWEgYWFhYWFhYWFhYSBhYWFhYWFhYWFhIGFhYWFhYWFhYWEgYWFhYWFhYWFhYSBhYWFhYWFhYWFhIGFhYWFhYWFhYWEgYWFhYWFhYWFhYSBhYWFhYWFhYWFhIGFhYWFhYWFhYWEgYWFhYWFhYWFhYSBhYWFhYWFhYWFhIGFhYWFhYWFhYWEgYWFhYWFhYWFhYSBhYWFhYWFhYWFhIGFhYWFhYWFhYWEgYWFhYWFhYWFhYSBhYWFhYWFhYWFhIGFhYWFhYWFhYWEifQ.zClX-uOKKqLsqAqVMpnw-I0EnMe10udOMtITFc0EHUk")
# print(INVALID_JWT_LONG_NAME)
# print()
# INVALID_JWT_NON_PRIME_SEED = verify_jwt("eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW4iLCJTZWVkIjoiMTQ2MjYiLCJOYW1lIjoiTWFyY29zIFJ1aXoifQ.DEmgzTbgiW0sL1BAf2gKQTRnPtnuIZHIBq1Ejzllk7w")
# print(INVALID_JWT_NON_PRIME_SEED)
# print()
# INVALID_JWT_INVALID_ROLE = verify_jwt("eyJhbGciOiJIUzI1NiJ9.eyJSb2xlIjoiQWRtaW5pc3RyYWRvciIsIlNlZWQiOiIxNDYyNiIsIk5hbWUiOiJNYXJjb3MgUnVpeiJ9._jyQwyURKwaJQAMnnveEviN83mMXfXAcKgBopvW2rYI")
# print(INVALID_JWT_INVALID_ROLE)
# print()
