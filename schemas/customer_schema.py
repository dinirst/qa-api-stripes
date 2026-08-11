customer_schema = {
    "type": "object",
    "required": [
        "id",
        "object",
        "email",
        "livemode"
    ],
    "properties": {
        "id": {
            "type": "string"
        },
        "object": {
            "type": "string",
            "const": "customer"
        },
        "email": {
            "type": "string"
        },
        "livemode": {
            "type": "boolean"
        }
    }
}