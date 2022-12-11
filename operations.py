from commands import bot


OPERATIONS = {
    'help': bot.get_help,
    'stop': bot.exit_function,
    'exit': bot.exit_function,
    'close': bot.exit_function,
    'good bye': bot.exit_function,
    'hello': bot.hello_function,
    'hi': bot.hello_function,
    'add email': bot.email_func,
    'add phone': bot.add_phone_func,
    'add birthday': bot.birthday_func,
    'add address': bot.address_func,
    'add note': bot.add_note,
    'add tags': bot.add_tags,
    'search notes': bot.search_notes,
    'search tags': bot.search_notes_by_tags,
    'sort notes': bot.sort_notes,
    'search by tags': bot.search_notes_by_tags,
    'add record': bot.add_record,
    'days to birthday': bot.next_birthday_func,
    'birthdays in range': bot.search_birthday_func,
    'change phone': bot.change_phone,
    'show all': bot.show_function,
    'search': bot.search_function,
    'delete phone': bot.delete_phone,
    'delete record': bot.del_record,
    'delete notes': bot.delete_note,
    'edit notes': bot.edit_note,
    'show notes': bot.show_notes,
    'sort folder': bot.folder_sorting
}
