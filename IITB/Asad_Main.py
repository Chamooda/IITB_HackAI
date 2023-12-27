from uagents.setup import fund_agent_if_low
from uagents import Agent, Bureau, Context, Model



class Message(Model):
    message: list


Converter_ka_address = "agent1qtwpmxqn2mq7u6c66qvllq03m9ztymyvfh8p3swrncky57aj0t9wysqft29"
list_of_resumes = []





RECIPIENT_ADDRESS = Converter_ka_address

alice = Agent(
    name="alice",
    port=8000,
    seed="Asad_Hadi",
    endpoint=["http://127.0.0.1:8000/a"],
)


Converter = Agent(
    name = "Converter",
    port = 8000,
    seed = "Pushpak_Agrawal",
    endpoint=["http://127.0.0.1:8000/b"],
)


fund_agent_if_low(alice.wallet.address())
fund_agent_if_low(Converter.wallet.address())

@alice.on_interval(period=5.0)
async def send_message(ctx: Context):
    resume = input("Enter new Resume name else enter: XXX\n")
    if(resume != "XXX"):
        list_of_resumes.append(resume)
        await ctx.send(RECIPIENT_ADDRESS, Message(message=list_of_resumes))


@Converter.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")

bureau = Bureau()
bureau.add(alice)
bureau.add(Converter)


if __name__ == "__main__":
    bureau.run()
