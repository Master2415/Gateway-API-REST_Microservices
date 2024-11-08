const { Given, When, Then, Before } = require("@cucumber/cucumber");
const assert = require("assert");
const axios = require("axios");
const messageSchema = require("../../schemas/messaje-schema");
const errorSchema = require("../../schemas/error-schema");
const faker = require("@faker-js/faker");
const Ajv = require("ajv");
const ajv = new Ajv();
const addFormats = require("ajv-formats");

let response;
let URL_ADD_USER = "http://localhost:8081/api/add";
let URL_ADD = "http://localhost:8083/profile/add";
let URL_LOGIN = "http://localhost:8080/api/login";

let userData = {
    name: faker.fakerAR.internet.userName(),
    email: faker.fakerAR.internet.email(),
    password: faker.fakerAR.internet.password(),
};

let defaultData = {
    Name: userData.name,
    URL: "Empty",
    Nickname: "Empty",
    Public_Info: "Empty",
    Messaging: "Empty",
    Biography: "Empty",
    Organization: "Empty",
    Country: "Empty",
    Social_Media: "Empty",
    Email: userData.email,
};

let emptyData = {
    Name: userData.name,
    URL: "",
    Nickname: "",
    Public_Info: "",
    Messaging: "",
    Biography: "",
    Organization: "",
    Country: "",
    Social_Media: "",
    Email: userData.email,
};

Before(function () {
});

Given('un usuario quiere agregar un perfil', function () {
    return Promise.resolve();
});


Given('se proporcionan los datos del perfil', function () {
    return Promise.resolve();
});


Given('se envía una solicitud POST a \\/api\\/add_profile', function () {
    return Promise.resolve();
});


When('se envía una solicitud POST con datos de perfil válidos', async function () {
    try {
        response = await axios.post(URL_ADD_USER, userData);
        token = response.data;
        console.log('Data: ' + response.data)
        response = await axios.post(URL_ADD, defaultData, { headers: { Authorization: `Bearer ${token}` } });
    } catch (error) {
        if (error.response) {
            response = error.response;
            console.log('Data Error: ' + response)
        } else {
            throw new Error('No se recibió una respuesta válida o el mensaje de error está vacío.');
        }
    }
});

Then('se espera que el código de respuesta de \\/api\\/add_profile sea {int}', function (expectedStatusCode) {
    assert.strictEqual(response.status, expectedStatusCode);
});


Then('se espera que el mensaje de respuesta de \\/api\\/add_profile sea {string}', function (string) {
    if (response && response.data) {
        const user = response.data;
        valid = ajv.validate(messageSchema, user);
        assert.strictEqual(valid, true);
    } else {
        throw new Error('No se recibió una respuesta válida o los datos están vacíos.');
    }
});

