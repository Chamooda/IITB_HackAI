from uagents.setup import fund_agent_if_low
from uagents import Agent, Bureau, Context, Model
from Messages.List_Modal import Message

Converter = Agent(
    name = "Converter",
    port = 8000,
    seed = "Pushpak_Agrawal",
    endpoint=["http://127.0.0.1:8000/b"],
)

fund_agent_if_low(Converter.wallet.address())


@Converter.on_message(model=Message)
async def message_handler(ctx: Context, sender: str, msg: Message):
    ctx.logger.info(f"Received message from {sender}: {msg.message}")
