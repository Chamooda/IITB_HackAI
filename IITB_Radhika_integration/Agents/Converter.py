from uagents.setup import fund_agent_if_low
from uagents import Agent, Bureau, Context, Model
from Messages.List_Modal import Message
import time

Converter = Agent(
    name = "Converter",
    port = 8000,
    seed = "Pushpak_Agrawal",
    endpoint=["http://127.0.0.1:8000/b"],
)

fund_agent_if_low(Converter.wallet.address())


@Converter.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    import os
    from langchain.document_loaders import PyPDFLoader
    import re
    for resume in msg.message:

        os.environ["OPENAI_API_KEY"] = "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"

        pdf_loader = PyPDFLoader(resume)
        documents = pdf_loader.load()

        from langchain.llms import OpenAI
        from langchain.chains.question_answering import load_qa_chain

        # we are specifying that OpenAI is the LLM that we want to use in our chain
        chain = load_qa_chain(llm=OpenAI())
        query = """
        Rate this person's compatability for a job
        Make sure that the person meets the minimum educational qualifications for the job and is highly skilled.
        Rate strictlty according to educational qualifications 
        Be Extremely Critical and try to give as less of a score as possible consider worst case scenario
        See the resume from a recruiters point of view
        from 0 to 1000

        Make sure it matches the following job description:
        Job Title: Senior Software Engineer (ML for Backend)
        1) holds a college degree in Computer Science or related field
        2) has 5+ years of experience in software development
        3) has 3+ years of experience in Python
        4) has worked on projects related to web programming in the past
        5) has worked on projects related to machine learning in the past
        6) has worked with blockchain
        7) has a Phd in Computer Science


        If cannot accurately tell the answer just guess but make sure that the response should be a number between 0 and 1000
        """
        score = None
        response = chain.run(input_documents=documents, question=query)
        score = [ word for word in response.split(" ") if word.isdigit() and int(word) < 1000]

        if score:
            resume = resume[8:]
            resume = resume[:-4]

            ctx.logger.info(f"Resume {resume} got: {score}")

        time.sleep(20)
