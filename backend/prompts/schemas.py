from langchain.output_parsers import ResponseSchema

EMAIL_SCHEMAS = [
    ResponseSchema(name="email_content", description="The main body of the email"),
    ResponseSchema(name="subject", description="The email subject line"),
    ResponseSchema(name="to_email", description="The recipient's email address")
] 