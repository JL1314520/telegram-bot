from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import os

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 欢迎使用机器人！\n\n"
        "发送：\n"
        "/calc 1+2\n"
        "例如：/calc 100*25"
    )

async def calc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) == 0:
        await update.message.reply_text("请输入算式，例如：/calc 10+20")
        return

    expression = " ".join(context.args)

    try:
        result = eval(expression)
        await update.message.reply_text(f"结果：{result}")
    except:
        await update.message.reply_text("算式错误！")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("calc", calc))

print("机器人启动成功...")
app.run_polling()
