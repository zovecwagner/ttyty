import disnake
from disnake.ext import commands
from datetime import datetime

# Укажите префикс для команд
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)



@bot.event
async def on_ready():
    print(f"Бот {bot.user} успешно запущен!")

    activity = disnake.Game(name="Скриптинг")  # Можно указать любое текстовое сообщение
    await bot.change_presence(activity=activity)

@bot.slash_command(description="Получить партерскую программу от нас на ваш сервер.")
@commands.has_permissions(administrator=True)
async def get_partner(inter: disnake.ApplicationCommandInteraction):
    emb = disnake.Embed(
        title="Реклама:",
        description="""**Приглашение на сервер наших партнеров:** 
        https://discord.com/syAzbwPUw3""",
        color=disnake.Color.purple()
    )
    emb.set_image(url="https://cdn.discordapp.com/attachments/1338084632511647801/1339145084901527582/image.png?ex=67ada78c&is=67ac560c&hm=a70f7e1bdcc0e2dbf8fab245808dd5a78ca84cdeb60c27468325d8721f3ad260&")
    emb.set_author(name="Spofimwars", icon_url="https://cdn.discordapp.com/attachments/1338084632511647801/1339145745269395477/fav.png?ex=67ada829&is=67ac56a9&hm=d05e4eb9a128be38f0df31442db0abc304a670cabeee6bbd050d096b82d7ee40&")
    await inter.response.send_message(embed=emb)

@bot.slash_command(description="Посмотреть информацию.")
@commands.has_permissions(administrator=True)
async def information(inter: disnake.ApplicationCommandInteraction):
    emb3 = disnake.Embed(
        title="Роли:",
        description="""<:developer:1338094480338845698> ** - Главный разработчки**
        <:Moderator:1338957375004082176> ** - Модератор Дискорд сервера**
        <:Builder:1338957379537993759> ** - Строитель карты в процессе разработки**
        <:Scripter:1338957373460713563> ** - Пишет скрипты в процессе разработки**
        <:Webdev:1338957377289846983> ** - Занимается разработкой сайта**
        <:Desinger:1338957383120060529> ** - Создает дизайн для сервера или сайта**
        <:Concept:1338957381652185240> ** - Создает идеи для плейсов**
        <:QA:1338958450549456976> ** - Тестирует плейс до его выхода в открытый доступ**
        <:Staff:1338094488282861649> ** - Помогает модератору в его работе**
        <:securit:1338094486332379216> ** - Защищает сервер от Редйов и Нюкеров**
        <:bot:1338094478875168830> ** - Бот сервера**
        <:Holder:1338094482222092379> ** - Поддерживает сервер, возможно держит сервера**
        <:mail:1338094484461715538> ** - Отвечает на вопросы участников**
        """,
        color=disnake.Color.purple()
    )
    emb3.set_image(url="https://cdn.discordapp.com/attachments/1338084632511647801/1339157367584981026/image.png?ex=67adb2fc&is=67ac617c&hm=4dcc5e3b5e72fd03aae572625570ed36117bb7783b54b11106d77f6e42284223&")

    emb2 = disnake.Embed(
        description="ㅤ",
        color=disnake.Color.purple()
    )
    emb2.set_image(url="https://cdn.discordapp.com/attachments/1338084632511647801/1339160862774267924/image.png?ex=67adb63e&is=67ac64be&hm=5677c82d9c6a32d2d543461382f1a85a705be7ddc2428852461bc5c0cb50eb3d&")

    emb4 = disnake.Embed(
        description="ㅤ",
        color=disnake.Color.purple(),
    )
    emb4.set_image(url="https://cdn.discordapp.com/attachments/1338084632511647801/1339166427323830333/image.png?ex=67adbb6c&is=67ac69ec&hm=65ead8019a2f7a0df72f074732fc4d16a3622704ca2363190880deea100ff37d&")

    emb5 = disnake.Embed(
        description="""
        <#1337890832883388436> ** - Все важные каналы на сервере находятся в этой категории**
        <#1339120189337501696> ** - Здесь находится канал форума и в будующем каналы будут пополнятся**
        <#1338216421712203877> ** - Категория созданная для общения**""",
        color=disnake.Color.purple()
    )
    emb5.set_image(url="https://cdn.discordapp.com/attachments/1338084632511647801/1339157367584981026/image.png?ex=67adb2fc&is=67ac617c&hm=4dcc5e3b5e72fd03aae572625570ed36117bb7783b54b11106d77f6e42284223&")

    emb6 = disnake.Embed(
        description="""**Инормация для партенрства:
        Чтобы получить партнерскую программу с нами - вам нужно добавить бота на сервер и написать команду /get_partner, после чего отправить <@1207251344029786164> ссылку на ваш сервер.**""",
        color=disnake.Color.purple()
    )

    channel = bot.get_channel(1338156537687969915)
    await channel.send(embeds=[emb2, emb3, emb4, emb5, emb6])

bot.run("MTMzODA4MjI3MTU5MjQ1MjExNg.GRLLyf.mEA9tHjao3J1c4K6MReuj0WwWFxvmO_UMRp4ds")
