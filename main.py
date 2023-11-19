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
/games will provide you a selection of games collected by each syndrome
/tips will provide you a selection of tips collected by each syndrome.''')


# async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await update.message.reply_text('this is a custom command')


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


async def tips_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Please, type into chat syndrome your are interested in.
For example, 'Tips for Autism'.
Now, we have a choose from:

𝐀𝐮𝐭𝐢𝐬𝐦
𝐃𝐨𝐰𝐧 𝐬𝐲𝐧𝐝𝐫𝐨𝐦𝐞
𝐖𝐢𝐥𝐥𝐢𝐚𝐦𝐬 𝐒𝐲𝐧𝐝𝐫𝐨𝐦𝐞""")


async def resources_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""Please, type into chat syndrome your are interested in.
For example, 'Resources for Autism'.
Now, we have a choose from:

𝐀𝐮𝐭𝐢𝐬𝐦
𝐃𝐨𝐰𝐧 𝐬𝐲𝐧𝐝𝐫𝐨𝐦𝐞
𝐖𝐢𝐥𝐥𝐢𝐚𝐦𝐬 𝐒𝐲𝐧𝐝𝐫𝐨𝐦𝐞""")


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
    if 'tips for autism' in processed:
        return '''𝐓𝐢𝐩 𝟏:
Create a consistent daily schedule for the child, in order to develop a useful habit in the child and calm him down mentally.

𝐓𝐢𝐩 𝟐:
Children with autism should be involved in helping around the home as early as possible. They should be involved in cooking, dishwashing, and cleaning. It is very useful for an autistic child if there are any bellies in the house: cat, dog, turtle, bird, or fish. The child should be taught to take care of them.
'''
    if 'tips for down syndrome' in processed:
        return '''𝐓𝐢𝐩 𝟏:
Do not hesitate to enroll your child in inclusive classes, because then he will be able to develop both socially and educationally much more effectively.
    
𝐓𝐢𝐩 𝟐:
Do not try to find «manifestations of the syndrome» in the behavior of the child, or his emotions. Your child can express his feelings just like any other child. 
        '''
    if 'tips for williams syndrome' in processed:
        return '''𝐓𝐢𝐩 𝟏:
Read about operant conditioning, and learn how to use positive reinforcement in order to stimulate the desired behavior in the child.

𝐓𝐢𝐩 𝟐:
Regular physical activity and specialized sports can be useful in socializing children with Williams-Campbell syndrome. Participation in sports and team activities helps to develop communication skills, strengthen self-esteem, and improve self-discipline.
        
        '''
    if 'resources for autism' in processed:
        return '''
𝐀𝐮𝐭𝐢𝐬𝐦 𝐒𝐩𝐞𝐚𝐤𝐬 - an organization offering resources for families and educational materials: https://www.autismspeaks.org/

𝐓𝐡𝐞 𝐍𝐚𝐭𝐢𝐨𝐧𝐚𝐥 𝐀𝐮𝐭𝐢𝐬𝐭𝐢𝐜 𝐒𝐨𝐜𝐢𝐞𝐭𝐲 is a British autism society offering resources and information: https://www.autism.org.uk/

𝐀𝐮𝐭𝐢𝐬𝐦 𝐄𝐝𝐮𝐜𝐚𝐭𝐨𝐫 - A website with educational materials and tips for parents and teachers: https://autismeducator.com/

𝐃𝐨𝟐𝐥𝐞𝐚𝐫𝐧 is a platform offering educational and play materials for children with autism: https://www.do2learn.com/

Understanding is a section of the website that offers resources and 𝐭𝐢𝐩𝐬 𝐨𝐧 𝐯𝐚𝐫𝐢𝐨𝐮𝐬 𝐭𝐨𝐩𝐢𝐜𝐬 𝐫𝐞𝐥𝐚𝐭𝐞𝐝 𝐭𝐨 𝐚𝐮𝐭𝐢𝐬𝐦: https://www.understood.org/en/learning-thinking-differences/child-learning-disabilities/autism/

𝐀𝐮𝐭𝐢𝐬𝐦 𝐑𝐞𝐬𝐨𝐮𝐫𝐜𝐞𝐬 - A collection of valuable resources and articles for families and educators working with children with autism: https://www.autismresources.com/

𝐒𝐭𝐚𝐫𝐟𝐚𝐥𝐥 is an interactive learning platform for children with special needs, including autism: https://www.starfall.com/

𝐀𝐮𝐭𝐢𝐬𝐦 𝐂𝐥𝐚𝐬𝐬𝐫𝐨𝐨𝐦 is a website created specifically for parents and educators of children with autism. They offer free teaching materials and tips on setting up a home classroom space and creating a productive learning environment: https://www.autismclassroom.com/

𝐃𝐚𝐲𝐂𝐚𝐩𝐞 is an app that offers children with autism visual structure in their daily routines. Parents and teachers have access to the plan and send tasks directly to the child’s app. It has a simple display with images and a visual timer and what tasks need to be done during the day. Based on research about children with ASD, the app includes visuals, color-coding, data tracking, opportunities for adaptation, and Moodshare, which helps children communicate how they feel about the activity: https://search.bridgingapps.org/apps/daycape

Build communication skills, fine motor skills, sensory play skills, and daily living skills, while helping your child or students to successfully manage any difficult behaviors, with these fun, educational, printable activities: https://speciallearninghouse.lpages.co/autism-workbook-bundle/
'''

    if 'resources for down syndrome' in processed:
        return '''
𝐃𝐨𝟐𝐥𝐞𝐚𝐫𝐧 (https://do2learn.com /) - A website with various materials and resources for educating children with special needs, including games, drawings, songs, and more.

𝐒𝐩𝐞𝐜𝐢𝐚𝐥 𝐎𝐥𝐲𝐦𝐩𝐢𝐜𝐬 (https://specialolympics.org /) is an international organization that offers sports and socialization programs for children and adults with intellectual disabilities, including Down syndrome.

𝐒𝐭𝐚𝐫𝐟𝐚𝐥𝐥 (https://www.starfall.com/h/index-grades123.php ) is an interactive educational platform offering games, books, and materials for the development of reading, mathematics, and other subjects for children up to eight years old.
resource
𝐆𝐞𝐦𝐢𝐧𝐢 (https://gemiini.org /) is a platform offering video modeling for teaching speech, social skills, and other communication skills to children with special needs.

𝐒𝐞𝐬𝐚𝐦𝐞 𝐒𝐭𝐫𝐞𝐞𝐭 𝐚𝐧𝐝 𝐀𝐮𝐭𝐢𝐬𝐦 (https://autism.sesamestreet.org /) - The Sesame Street website with materials and videos created specifically for children with autism spectrum disorders, but which can also be useful for children with Down syndrome.

𝐊𝐡𝐚𝐧 𝐀𝐜𝐚𝐝𝐞𝐦𝐲 𝐊𝐢𝐝𝐬 (https://learn.khanacademy.org/khan-academy-kids /) is an educational platform designed for children under five years old, offering interactive lessons, games, and activities in various subjects.

𝐅𝐨𝐫 𝐧𝐞𝐰 𝐩𝐚𝐫𝐞𝐧𝐭𝐬 𝐨𝐟 𝐜𝐡𝐢𝐥𝐝𝐫𝐞𝐧 𝐰𝐢𝐭𝐡 𝐃𝐨𝐰𝐧 𝐒𝐲𝐧𝐝𝐫𝐨𝐦𝐞 (https://www.wouldntchangeathing.org/product/wcat-book-by-celebrate-t21/), but many schools and organizations have requested a copy. We fund these for free for new parents, support groups, and maternity units.

𝐀𝐧 𝐢𝐧𝐜𝐥𝐮𝐬𝐢𝐯𝐞 𝐚𝐫𝐭𝐬 𝐜𝐡𝐚𝐫𝐢𝐭𝐲 (https://dancesyndrome.co.uk/) providing a range of opportunities for individuals and organizations to work with them through inspiring workshops, leadership training, and performances. Regular sessions take place across the North West of England but they also perform at events across the UK.

𝐀 𝐦𝐚𝐠𝐚𝐳𝐢𝐧𝐞 𝐟𝐨𝐫 𝐭𝐡𝐞 𝐃𝐨𝐰𝐧 𝐒𝐲𝐧𝐝𝐫𝐨𝐦𝐞 𝐜𝐨𝐦𝐦𝐮𝐧𝐢𝐭𝐲 (http://makingchromosomescount.co.uk/cgi-sys/suspendedpage.cgi) You can visit the website to subscribe and receive your copy of Down Syndrome Community News and please get in touch with them if you would like to feature in future newsletters.

𝐈𝐧𝐟𝐨𝐫𝐦𝐚𝐭𝐢𝐨𝐧, 𝐡𝐞𝐥𝐩, 𝐚𝐧𝐝 𝐚𝐝𝐯𝐢𝐜𝐞 𝐟𝐨𝐫 𝐩𝐚𝐫𝐞𝐧𝐭𝐬 𝐚𝐧𝐝 𝐟𝐚𝐦𝐢𝐥𝐢𝐞𝐬 𝐨𝐟 𝐩𝐫𝐢𝐦𝐚𝐫𝐲 𝐬𝐜𝐡𝐨𝐨𝐥 𝐜𝐡𝐢𝐥𝐝𝐫𝐞𝐧 (https://downsyndrome.ie/support-detail/primary-school/)
        '''
    if 'resources for williams syndrome' in processed:
        return '''
𝐓𝐡𝐞 𝐖𝐢𝐥𝐥𝐢𝐚𝐦𝐬 𝐒𝐲𝐧𝐝𝐫𝐨𝐦𝐞 𝐀𝐬𝐬𝐨𝐜𝐢𝐚𝐭𝐢𝐨𝐧 (𝐖𝐒𝐀): The official website of The Williams Syndrome Association offers information about the syndrome, training resources, support groups, and much more. Link: https://williams-syndrome.org/

𝐊𝐡𝐚𝐧 𝐀𝐜𝐚𝐝𝐞𝐦𝐲 𝐋𝐞𝐚𝐫𝐧𝐢𝐧𝐠 𝐑𝐞𝐬𝐨𝐮𝐫𝐜𝐞𝐬: Khan Academy offers free educational videos and lessons in various subjects, including mathematics, science, and art. This is a great resource for children with various special needs. Link: https://www.khanacademy.org/

𝐒𝐞𝐬𝐚𝐦𝐞 𝐒𝐭𝐫𝐞𝐞𝐭 𝐚𝐧𝐝 𝐀𝐮𝐭𝐢𝐬𝐦: The Sesame Street program offers special resources for children with autism that may also be useful for children with Williams syndrome. Link: https://autism.sesamestreet.org/

𝐒𝐩𝐞𝐜𝐢𝐚𝐥 𝐎𝐥𝐲𝐦𝐩𝐢𝐜𝐬: Special Olympics offers sports and educational programs for children with various special needs, including children with Williams syndrome. Link: https://www.specialolympics.org/

𝐈𝐧𝐜𝐥𝐮𝐬𝐢𝐯𝐞 𝐓𝐞𝐜𝐡𝐧𝐨𝐥𝐨𝐠𝐲: Inclusive Technology offers educational resources and programs for children with special educational needs. Resources are available in several languages. Link: https://www.inclusive.co.uk/

𝐂𝐡𝐢𝐥𝐝𝐫𝐞𝐧'𝐬 𝐋𝐢𝐛𝐫𝐚𝐫𝐲 𝐒𝐭𝐨𝐫𝐲𝐥𝐢𝐧𝐞 𝐎𝐧𝐥𝐢𝐧𝐞: Storyline Online is a collection of videos of famous actors reading children's books. This resource can be useful for developing reading and language skills in children with Williams syndrome. Link: https://www.storylineonline.net/

𝐖𝐡𝐚𝐭 𝐢𝐭 𝐦𝐞𝐚𝐧𝐬 𝐭𝐨 𝐥𝐢𝐯𝐞 𝐰𝐢𝐭𝐡 𝐖𝐢𝐥𝐥𝐢𝐚𝐦𝐬 𝐬𝐲𝐧𝐝𝐫𝐨𝐦𝐞 𝐚𝐧𝐝 𝐡𝐨𝐰 𝐭𝐨 𝐟𝐢𝐧𝐝 𝐭𝐡𝐞 𝐫𝐢𝐠𝐡𝐭 𝐬𝐮𝐩𝐩𝐨𝐫𝐭 𝐟𝐨𝐫 𝐲𝐨𝐮𝐫 𝐟𝐚𝐦𝐢𝐥𝐲: https://www.mencap.org.uk/learning-disability-explained/conditions-linked-learning-disability/williams-syndrome#:~:text=With the right support%2C people, develop as they grow up

𝐖𝐢𝐥𝐥𝐢𝐚𝐦𝐬 𝐒𝐲𝐧𝐝𝐫𝐨𝐦𝐞 𝐌𝐮𝐬𝐢𝐜 𝐚𝐧𝐝 𝐀𝐫𝐭: A website that provides resources for the use of music and art in the education and development of children with Williams syndrome. Here you can find free tasks, games, and activities: http://williamssyndrometoolbox.com/arts/music-art/

𝐖𝐢𝐥𝐥𝐢𝐚𝐦𝐬 𝐒𝐲𝐧𝐝𝐫𝐨𝐦𝐞 𝐒𝐨𝐮𝐧𝐝𝐬-𝐅𝐞𝐞𝐝𝐬 𝐌𝐢𝐧𝐝𝐬: A website that provides resources for the development of speech and communication skills of children with Williams Syndrome. It contains free audio files with instructions for pronunciation training and language development: https://www.williams-syndrome.org/sound-feed-minds

𝐖𝐢𝐥𝐥𝐢𝐚𝐦𝐬 𝐒𝐲𝐧𝐝𝐫𝐨𝐦𝐞 𝐅𝐨𝐮𝐧𝐝𝐚𝐭𝐢𝐨𝐧: This foundation offers a variety of free resources for children with Williams Syndrome, their families, and specialists. They provide information, assistance, and guidance on education and medicine: https://williams-syndrome.org.uk/
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
    # app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('books', books_command))
    app.add_handler(CommandHandler('games', games_command))
    app.add_handler(CommandHandler('tips', tips_command))
    app.add_handler(CommandHandler('resources', resources_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('Polling...')
    app.run_polling(poll_interval=3)
