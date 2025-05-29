from langchain_openai import ChatOpenAI
from browser_use import Agent
from dotenv import load_dotenv
load_dotenv()

import asyncio

llm = ChatOpenAI(model="gpt-4o")


async def main():
    agent = Agent(
        task="visit 'https://vahan.parivahan.gov.in/vahanservice/vahan/ui/appl_status/form_Know_Appl_Status.xhtml' and toggle to vehicle no and then Check status of application KAXXXXXX, Issue of NOC, click on 'Click here for details' and extract status",
        use_vision=True,
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())