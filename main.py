from typing import Final
from telegram import Update
from telegram.ext import CommandHandler, MessageHandler, filters, ContextTypes, Application

TOKEN: Final = ''
BOT_USERNAME = '@thegencup_bot'


# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''Dear parents and guests of our bot!

We are thrilled to welcome you to our project. We would like to note that the bot was created exclusively with non-commercial and positive purposes. As The Gencup team, we strive to provide the best possible support for special children and their parents, worldwide.

We also want to note that, the advice and information provided is general and not tailored to the individual needs of a minor child. If you have any questions or concerns, feel free to contact us. We are ready to help you at any time!

Type /help to find commands that can help you!

Sincerely, The Gencup team.''')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''Here is the list of existing commands:

/books will provide you a selection of books collected by each syndrome.
/games will provide you a selection of games collected by each syndrome.''')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('this is a custom command')


async def books_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Please, type into chat syndrome your are interested in.
For example, 'Books for Autism'.
Now, we have a choose from:

𝐀𝐮𝐭𝐢𝐬𝐦
𝐃𝐨𝐰𝐧 𝐬𝐲𝐧𝐝𝐫𝐨𝐦𝐞
𝐂𝐨𝐧𝐠𝐞𝐧𝐢𝐭𝐚𝐥 𝐇𝐲𝐩𝐨𝐭𝐡𝐲𝐫𝐨𝐢𝐝𝐢𝐬𝐦
𝐖𝐢𝐥𝐥𝐢𝐚𝐦𝐬 𝐒𝐲𝐧𝐝𝐫𝐨𝐦𝐞
𝐇𝐮𝐧𝐭𝐢𝐧𝐠𝐭𝐨𝐧'𝐬 𝐃𝐢𝐬𝐞𝐚𝐬𝐞""")


async def games_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Please, type into chat syndrome your are interested in.
For example, 'Games for Autism'.
Now, we have a choose from:

𝐀𝐮𝐭𝐢𝐬𝐦
𝐃𝐨𝐰𝐧 𝐬𝐲𝐧𝐝𝐫𝐨𝐦𝐞
𝐂𝐨𝐧𝐠𝐞𝐧𝐢𝐭𝐚𝐥 𝐇𝐲𝐩𝐨𝐭𝐡𝐲𝐫𝐨𝐢𝐝𝐢𝐬𝐦
𝐖𝐢𝐥𝐥𝐢𝐚𝐦𝐬 𝐒𝐲𝐧𝐝𝐫𝐨𝐦𝐞
𝐇𝐮𝐧𝐭𝐢𝐧𝐠𝐭𝐨𝐧'𝐬 𝐃𝐢𝐬𝐞𝐚𝐬𝐞""")



# Handle Responses

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'books for autism' in processed:
        return '''Here is the link to Google Drive with books for kids with Autsim:
https://drive.google.com/drive/folders/13xnRHzCInjEC509jUQ6X2gYaXPFwCJNB?usp=drive_link'''

    if 'books for congenital hypothyroidism' in processed:
        return '''Here is the link to Google Drive with books for kids with Congenital Hypothyroidism:
https://drive.google.com/drive/folders/1qhavM35tyjLYUXPLRDdX-nMdFZg9GVjJ?usp=drive_link'''

    if 'books for down syndrome' in processed:
        return '''Here is the link to Google Drive with books for kids with Down syndrome:
https://drive.google.com/drive/folders/1ccrWUS0kFFggsY7BnTqgqs1fg9baAH5c?usp=drive_link'''

    if "books for huntington's disease" in processed:
        return '''Here is the link to Google Drive with books for kids with Huntington's Disease:
https://drive.google.com/drive/folders/1IPsGOzQ_UUu8hrKFhz8RVCnU1bhg1x_o?usp=drive_link'''

    if 'books for williams syndrome' in processed:
        return '''Here is the link to Google Drive with books for kids with Williams Syndrome:
https://drive.google.com/drive/folders/1ImAhoy-AUcq2DPVYZ1Wjzwkn3B_9KNfY?usp=drive_link'''

    if 'games for down syndrome' in processed:
        return '''Game 1: 𝐎𝐛𝐬𝐭𝐚𝐜𝐥𝐞𝐬 𝐂𝐨𝐮𝐫𝐬𝐞

Use furniture to make your course. Let them come up with new obstacles as it will work their imagination.
You could have themes on different days - e.g. Pirates, Beach, Jungle, Castles.

Here is the example on Youtube:
https://www.youtube.com/watch?v=LpZti52tjNs

Game 2: 𝐌𝐞𝐦𝐨𝐫𝐲 𝐠𝐚𝐦𝐞𝐬

𝟏.Hiding game
Pull different items on the table, name them and after hide one item and ask your child what is hidden or what is missing.
 
𝟐.Pictures game
Line up pictures face down. You can start with a few pictures and increase their number.
Turn over the first and name it and then turn it back to face down. Ask your child to remember what was in the picture.
When the child can do that, turn over two pictures and name them. 
Turn the pictures back to face down position, point to each one and ask "What is it?".

𝟑.Grouping items
Pull a few items from different categories on the table. Name them and ask your child to sort them. 
Alternatively, lay down many items from one category on the table, with one item that does not belong to the same category and ask your child, "Which one does not belong to the group?

'''

    if 'games for williams syndrome' in processed:
        return '''Game 1: 𝐆𝐫𝐨𝐬𝐬 𝐚𝐧𝐝 𝐅𝐢𝐧𝐞 𝐌𝐨𝐭𝐨𝐫 𝐒𝐤𝐢𝐥𝐥𝐬 𝐃𝐞𝐯𝐞𝐥𝐨𝐩𝐦𝐞𝐧𝐭 𝐠𝐚𝐦𝐞

Materials: painter’s tape, toys.
Lay down painter’s tape on the floor in a ladder format in a rectangle shape.
The child can assist with this activity. The child can remove in the path in different ways.
Try walking through without stepping on the lines or vice versa, only on the line.
Try jumping over small toys inside the rectangle. Throw toys into rectangles.

Here is the example on Youtube:
https://youtu.be/Js62IcXgYcI

Game 2: 𝐇𝐚𝐧𝐝-𝐞𝐲𝐞 𝐜𝐨𝐨𝐫𝐝𝐢𝐧𝐚𝐭𝐢𝐨𝐧 𝐠𝐚𝐦𝐞: 𝐁𝐚𝐥𝐥𝐨𝐨𝐧 𝐓𝐞𝐧𝐧𝐢𝐬

Use a spatula or a paper plate taped to a paint stirrer as a racquet.
Children should hit the ball back and forth without letting it hit the floor.

Here is the example on YouTube:
https://www.youtube.com/watch?v=yuVkkhpiHTA

Game 3: 𝐅𝐢𝐧𝐠𝐞𝐫 𝐅𝐢𝐭𝐧𝐞𝐬𝐬 𝐄𝐱𝐞𝐫𝐜𝐢𝐬𝐞 𝐃𝐚𝐧𝐜𝐞𝐬 𝐟𝐨𝐫 𝐊𝐢𝐝𝐬

Here is the example on YouTube:
https://www.youtube.com/watch?v=r2tBH_XyeJc
'''
    if 'games for autism' in processed:
        return '''Game 1: 𝐒𝐦𝐞𝐥𝐥𝐬 𝐫𝐞𝐜𝐨𝐠𝐧𝐢𝐭𝐢𝐨𝐧

Bag items that have concrete smells (apples, lemons, geranium etc.).
It is necessary to exclude any other possibility of perceiving these objects(for example tactile).

Game 2: 𝐒𝐞𝐧𝐬𝐨𝐫𝐲 𝐩𝐥𝐚𝐲

𝟏.Assemble the toy
Make toy figures (animal toys or dolls) from plywood, foam or cardboard, cut out toy’s details (mouth, eyes, hair etc.).
Children should find the right place for the cut details by themselves. Gradually add more details.

𝟐.Playdough
Provide the child with various colors of playdough and simple tools like cookie cutters, rolling pins, and plastic utensils.
Encourage them to explore different textures, shapes, and creative ideas using the playdough.
'''

    return "I am not sure what you meant. Check your message's spelling, please."


async def handle_message(update: Update, contex: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id} in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('books', books_command))
    app.add_handler(CommandHandler('games', games_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
