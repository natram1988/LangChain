from langchain.chat_models import ChatOpenAI
import openai
from langchain.prompts import ChatPromptTemplate

openai.api_key  = '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'

chat = ChatOpenAI()

chat = ChatOpenAI(temperature=0.0)

template_string = """Translate the text \
that is delimited by triple backticks \
into a style that is {style}. \
text: ```{text}```
"""

customer_style = """American English \
in a calm and respectful tone
"""

customer_email = """
Arrr, I be fuming that me blender lid \
flew off and splattered me kitchen walls \
with smoothie! And to make matters worse, \
the warranty don't cover the cost of \
cleaning up me kitchen. I need yer help \
right now, matey!
"""

prompt_template = ChatPromptTemplate.from_template(template_string)



customer_messages = prompt_template.format_messages(
                    style=customer_style,
                    text=customer_email)

customer_response = chat(customer_messages)
print(customer_response.content)

service_reply = """Hey there customer, \
the warranty does not cover \
cleaning expenses for your kitchen \
because it's your fault that \
you misused your blender \
by forgetting to put the lid on before \
starting the blender. \
Tough luck! See ya!
"""

service_style_pirate = """\
a polite tone \
that speaks in American Pirate English\
"""

service_messages = prompt_template.format_messages(
    style=service_style_pirate,
    text=service_reply)

service_response = chat(service_messages)
print(service_response.content)
