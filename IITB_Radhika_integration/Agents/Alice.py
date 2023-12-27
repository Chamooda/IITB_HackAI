from uagents.setup import fund_agent_if_low
from uagents import Agent, Bureau, Context, Model
from Messages.List_Modal import Message
import os

Converter_ka_address = "agent1qtwpmxqn2mq7u6c66qvllq03m9ztymyvfh8p3swrncky57aj0t9wysqft29"
list_of_resumes = []


RECIPIENT_ADDRESS = Converter_ka_address

alice = Agent(
    name="alice",
    port=8000,
    seed="Asad_Hadi",
    endpoint=["http://127.0.0.1:8000/a"],
)


fund_agent_if_low(alice.wallet.address())



def get_file_names(folder_path):
    try:
        files = os.listdir(folder_path)
        
        file_names = ["Resumes/" + file for file in files if os.path.isfile(os.path.join(folder_path, file))]
        
        return file_names
    except Exception as e:
        print(f"Error: {e}")
        return None





@alice.on_interval(period=15.0)
async def send_message(ctx: Context):
        
        list_of_resumes = get_file_names("Resumes/")
        await ctx.send(RECIPIENT_ADDRESS, Message(message=list_of_resumes))

