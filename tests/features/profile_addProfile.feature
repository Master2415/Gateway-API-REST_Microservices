Feature: Crear Perfil

  Background:
    Given un usuario quiere agregar un perfil
    And se proporcionan los datos del perfil
    And se envía una solicitud POST a /api/add_profile

  Scenario: Agregar perfil exitosamente
    When se envía una solicitud POST con datos de perfil válidos
    Then se espera que el código de respuesta de /api/add_profile sea 200
    And se espera que el mensaje de respuesta de /api/add_profile sea "Perfil creado exitosamente"

    Scenario: Error debido a campos faltantes
    When se envía una solicitud POST con datos de perfil faltantes
    Then se espera que el código de respuesta de /api/add_profile sea 400
    And se espera que el mensaje de respuesta de /api/add_profile contenga un mensaje de "Error"

  Scenario: Error debido a tipo de datos inválido
    When se envía una solicitud POST con datos de perfil con tipos de datos inválidos
    Then se espera que el código de respuesta de /api/add_profile sea 400
    And se espera que el mensaje de respuesta de /api/add_profile contenga un mensaje de "Error"

  Scenario: Error debido a token inválido
    When se envía una solicitud POST con un token inválido
    Then se espera que el código de respuesta de /api/add_profile sea 404
    And se espera que el mensaje de respuesta de /api/add_profile contenga un mensaje de "Error"

  Scenario: Error debido a email ya registrado
    When se envía una solicitud POST con un email que ya está registrado
    Then se espera que el código de respuesta de /api/add_profile sea 400
    And se espera que el mensaje de respuesta de /api/add_profile contenga un mensaje de "Error"