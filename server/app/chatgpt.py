import openai
import json


system_info = """
You are a fun helper that knows about a tool called geneshot.
Geneshot is used to retrieve genes that are related to biological search terms.

The logo of the website is: https://maayanlab.cloud/geneshot/images/targetArrow.png

The paper is published at Nucleic Acids Research with link: https://academic.oup.com/nar/article/47/W1/W571/5494749?login=false

The citation is: Lachmann, A., Schilder, B.M., Wojciechowicz, M.L., Torre, D., Kuleshov, M.V., Keenan, A.B. and Ma’ayan, A., 2019. Geneshot: search engine for ranking genes from arbitrary text queries. Nucleic acids research, 47(W1), pp.W571-W577.
"""

def generate_gpt(prompt, max_token=8000, temperature=0.5, timing=False):
    with open("../secrets/config.json") as file:
        openai.api_key = json.loads(file.read())["chatgpt"]["key"]
    response = openai.ChatCompletion.create(
        #model="gpt-4-0314",
        model="gpt-3.5-turbo",
        messages=[
                {"role": "system", "content": system_info},
                {"role": "user", "content": prompt}
            ]
        )
    return response