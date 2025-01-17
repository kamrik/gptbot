from aiogram import Router, types
from aiogram.filters import CommandStart, Command
from .actions import change_assistant, handle_response
from .client import get_thread, get_assistant, asst_filter
from .logger import create_logger
from .translate import _t
from .helpers import escape_markdown
from .users import access_middleware

logger = create_logger(__name__)
router = Router()
router.message.middleware(access_middleware)


@router.message(CommandStart())
async def on_start(message: types.Message) -> None:
  logger.info(f"on_start:{message.from_user.username}:{message.from_user.id}")
  await message.answer(_t("bot.welcome", name=escape_markdown(message.from_user.full_name), id=message.from_user.id))


@router.message(Command("new"))
async def on_new(message: types.Message) -> None:
  await message.answer(_t("bot.new_chat"))
  thread = await get_thread(message.from_user.id, new_thread=True)
  logger.debug(f"on_new:{thread}")
  

@router.message(Command("help"))
async def on_new(message: types.Message) -> None:
  await message.answer('\n'.join([
    "Bot commands:",
    "/new - start a new chat",
    "/tutor - change the Agent (tutor) to talk to",
  ]))

@router.message(Command("tutor"))
async def on_tutor(message: types.Message) -> None:
  tutors = await get_assistant()
  logger.info(f"on_tutor:{[id for id, _ in tutors.items()]}")
  await message.answer(
      _t("bot.new_tutor", tutors="\n".join([f"`{id}`: {info['desc']}" for id, info in tutors.items()])),
      reply_markup=types.ReplyKeyboardMarkup(
          keyboard=[[types.KeyboardButton(text=id) for id, _ in tutors.items()]],
          resize_keyboard=True
      )
  )


@router.message(asst_filter)
async def on_change(message: types.Message) -> None:
  await change_assistant(message)


@router.message()
async def on_message(message: types.Message) -> None:
  try:
    await handle_response(message)
  except TypeError as error:
    logger.error(f"on_message:{error}")
    await message.answer(_t("bot.error_in_the_code"))
