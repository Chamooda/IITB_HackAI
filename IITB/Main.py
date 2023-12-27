from uagents.setup import fund_agent_if_low
from uagents import Agent, Bureau, Context, Model

from Agents.Alice import alice
from Agents.Converter import Converter

bureau = Bureau()
bureau.add(alice)
bureau.add(Converter)

bureau.run()