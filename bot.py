import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ Güvenlik Botu aktif!\n\n"
        "/help - Komutları göster"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🛡️ GÜVENLİK BOTU\n\n"
        "/start - Botu başlat\n"
        "/help - Yardım\n"
        "/ban - Kullanıcıyı yasakla\n"
        "/mute - Kullanıcıyı sustur\n"
        "/kick - Kullanıcıyı çıkar\n"
        "/warn - Uyarı ver"
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN ayarlanmamış!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("🛡️ Güvenlik botu çalışıyor...")
    app.run_polling()

if __name__ == "__main__":
    main()
