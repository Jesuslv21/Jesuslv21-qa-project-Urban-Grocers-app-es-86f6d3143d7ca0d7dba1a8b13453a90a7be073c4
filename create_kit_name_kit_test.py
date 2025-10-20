import data
import sender_stand_request

# Funcion para crear el kit
def get_kit_body(kit_name):
    current_body = data.kit_body.copy()
    current_body["name"] = kit_name
    return current_body

#Funcion para crear AuthToken
def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

# Función común para crear kit con nombre y validar respuesta esperada
def positive_assert(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Función común para verificar códigos 400 en casos inválidos
def negative_assert_code_400(kit_body):
    response = sender_stand_request.post_new_client_kit(kit_body, get_new_user_token())
    assert response.status_code == 400

#prueba ejemplo 1
def test_crear_1_kit_con_nombre_de_5_letras():
    new_kit_body = get_kit_body("Jesus")
    positive_assert(new_kit_body)



#prueba 1
def test_crear_un_kit_con_nombre_de_1_letra():
    new_kit_body = get_kit_body("a")
    positive_assert(new_kit_body)

#prueba 2
def test_crear_un_kit_con_nombre_de_511_letras():
    new_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(new_kit_body)

#prueba 3
def test_crear_un_kit_con_letras_menor_que_la_cantidad_permitida():
    new_kit_body = get_kit_body("")
    negative_assert_code_400(new_kit_body)

#prueba 4
def test_crear_1_kit_con_nombre_tipo_carateres_especiales():
    new_kit_body = get_kit_body("∞%&$&/$%¬")
    positive_assert(new_kit_body)

#prueba 5
def test_crear_un_kit_con_nombre_de_512_letras():
    new_kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcDpip3")
    negative_assert_code_400(new_kit_body)

#prueba 6
def test_crear_un_kit_con_nombre_con_espacios():
    new_kit_body = get_kit_body("Jesus Lopez")
    positive_assert(new_kit_body)

#Prueba 7
def test_crear_un_kit_con_nombre_tipo_numero():
    new_kit_body = get_kit_body(345)
    positive_assert(new_kit_body)

#Prueba 8
def test_crear_un_kit_con_el_paramtro_no_se_pasa_de_la_solicitud():
    kit_body = data.user_body.copy()
    kit_body.pop('firstName')
    negative_assert_code_400(kit_body)

#Prueba 9
def test_crear_un_kit_con_paramtro_diferente_numero():
    new_kit_body = get_kit_body(223)
    negative_assert_code_400(new_kit_body)


