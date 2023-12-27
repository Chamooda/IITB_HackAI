from uagents.setup import fund_agent_if_low
from uagents import Agent, Bureau, Context, Model
from Messages.List_Modal import Message
import json

bob = Agent(
    name = "Bob",
    port = 8000,
    seed = "Radhika_Desai",
    endpoint=["http://127.0.0.1:8000/c"],
)

fund_agent_if_low(bob.wallet.address())

@bob.on_interval(period = 10.0)
async def Check_and_print(ctx:Context):
    

    # file_path = 'Jobs.json'
    # with open(file_path, 'r') as file:
    #     data = json.load(file)

    # # Iterate through jobs
    # for job_title, job_details in data["jobs"].items():
    #     print(f"Job Title: {job_title}")
    #     print(f"Total Experience Required: {job_details['total_experience_required']}")
    #     print(f"Primary Skills Required: {', '.join(job_details['primary_skills_required'])}")
    #     print(f"Degree Required: {job_details['degree_required']}")
    #     print("\n" + "="*30 + "\n")


