from classes import Record, AddressBook
from decorator import input_error
from sort_files import run_sorting
from notes import Notes
from notes_decorator import input_error_notes
from abc import abstractmethod, ABC


class IBot(ABC):

    @staticmethod
    @abstractmethod
    def get_help():
        pass

    @staticmethod
    @abstractmethod
    def exit_function():
        pass

    @staticmethod
    @abstractmethod
    def hello_function():
        pass

    @abstractmethod
    def add_record(self, data):
        pass

    @abstractmethod
    def add_phone_func(self, data):
        pass

    @abstractmethod
    def change_phone(self, data):
        pass

    @abstractmethod
    def delete_phone(self, data):
        pass

    @abstractmethod
    def search_function(self, value):
        pass

    @abstractmethod
    def show_function(self):
        pass

    @abstractmethod
    def birthday_func(self, data):
        pass

    @abstractmethod
    def next_birthday_func(self, name):
        pass

    @abstractmethod
    def search_birthday_func(self, value):
        pass

    @abstractmethod
    def address_func(self, data):
        pass

    @abstractmethod
    def email_func(self, data):
        pass

    @abstractmethod
    def del_record(self, name):
        pass

    @staticmethod
    @abstractmethod
    def folder_sorting(path_to_folder):
        pass

    @staticmethod
    @abstractmethod
    def print_note(key, value):
        pass

    @abstractmethod
    def add_note(self, data):
        pass

    @abstractmethod
    def show_notes(self):
        pass

    @abstractmethod
    def add_tags(self, data):
        pass

    @abstractmethod
    def delete_note(self, data):
        pass

    @abstractmethod
    def edit_note(self, data):
        pass

    @abstractmethod
    def search_notes(self, data):
        pass

    @abstractmethod
    def search_notes_by_tags(self, data):
        pass

    @abstractmethod
    def sort_notes(self):
        pass

    @abstractmethod
    def save_data(self):
        pass


class Bot(IBot):
    def __init__(self, address_book: AddressBook, notes: Notes):
        self.address_book = address_book
        self.notes = notes

    @staticmethod
    def get_help():
        instruction = '''
            Start: hello or hi
            Add new contact: add record /name/ /phone phone .../
            Add phone: add phone /name/ /phone/
            Add e-mail: add email /name/ /e-mail/
            Change phone: change phone /name/ /old phone/ /new phone/
            Delete phone: delete phone /name/ /phone/
            Add address: add address /name/ /address/
            Show all contacts: show all
            Search contacts: search /text for search/
            Add birthday to contact: add birthday /name/ /date yyyy-mm-dd/
            Days to next birthday: days to birthday /name/
            Shows contacts that will have birthdays in period: birthdays in range /days/
            Delete contact: delete record /name/
            Sort file in folder: sort folder /path to folder/
            Add note: add note /note text/
            Show all notes: show notes
            Add tags to note: add tags /note id/ /tag tag .../
            Edit note: edit notes /id/ /note text/
            Delete note: delete notes /id/
            Search notes by note text: search notes /text/
            Search notes by tags: search tags /tag tag .../
            Sort notes: sort notes
            Quit: stop, exit, close, good bye
        '''
        return instruction

    @staticmethod
    def exit_function():
        """Function for close program"""
        return "good bye"

    @staticmethod
    def hello_function():
        return 'How can i help you?'

    @input_error
    def add_record(self, data: str) -> str:
        name, *phones = data.strip().split(' ')
        if name in self.address_book:
            raise ValueError('This contact already exist.')
        record = Record(name)

        for phone in phones:
            record.add_phone(phone)

        self.address_book.add_record(record)
        return f'You added new contact: {name} with this {phones}.'

    @input_error
    def add_phone_func(self, data: str) -> str:
        name, phone = data.strip().split(' ', 1)
        record = self.address_book[name]
        record.add_phone(phone)
        return 'You added phone'

    @input_error
    def change_phone(self, data: str) -> str:
        name, *phones = data.strip().split(' ')
        record = self.address_book[name]
        record.change_phones(phones)
        return 'You changed phones.'

    @input_error
    def delete_phone(self, data: str) -> str:
        name, phone = data.strip().split(' ', 1)

        record = self.address_book[name]
        if record.delete_phone(phone):
            return f'Phone {phone} for {name} contact deleted.'
        return f'{name} contact does not have this number'

    @input_error
    def search_function(self, value):

        records = self.address_book.search(value)

        search_records = '\n'.join([record.get_info() for record in records])
        return search_records

    @input_error
    def show_function(self):
        contacts = ''
        page_number = 1

        for page in self.address_book.iterator():
            contacts += f'Page №{page_number}\n'

            for record in page:
                contacts += f'{record.get_info()}\n'
                page_number += 1

        return contacts

    @input_error
    def birthday_func(self, data: str) -> str:
        name, birthday_date = data.split(" ", 1)
        record = self.address_book[name]
        record.add_birthday(birthday_date)
        return f"{birthday_date} Дата дня народження створена"

    @input_error
    def next_birthday_func(self, name: str) -> str:
        name = name.strip()
        record = self.address_book[name]
        return f"Святкувати будем через {record.get_days_to_next_birthday()} днів"

    @input_error
    def search_birthday_func(self, value):
        records_info = ""
        records = self.address_book.get_birthdays_in_range(value)

        if not records:
            return 'Відсутні контакти з днем народження в данному діапазоні'

        for record in records:
            records_info += f"{record.get_info()}\n"
        return records_info

    @input_error
    def address_func(self, data: str) -> str:
        name, address_date = data.split(" ", 1)
        record = self.address_book[name]
        record.add_address(address_date)
        return f"{address_date} Тут проживає гарна людина"

    @input_error
    def email_func(self, data: str) -> str:
        name, email_date = data.split(" ", 1)
        record = self.address_book[name]
        record.add_email(email_date)
        return f"{email_date} На цю пошту ми можемо щось надіслати)"

    @input_error
    def del_record(self, name: str) -> str:
        self.address_book.remove_record(name)
        return "You deleted the contact."

    @staticmethod
    def folder_sorting(path_to_folder: str):
        return run_sorting(path_to_folder)

    @staticmethod
    def print_note(key, value):
        result = 20 * "-" + "\n"
        result += f"note id - {key}\n"
        result += f"note text - {value.note_text}\n"
        if value.note_tags:
            result += f"tags - {' '.join(sorted(tag for tag in value.note_tags))}\n"
        return result

    @input_error_notes
    def add_note(self, data):
        note_text = data
        self.notes.add_note(note_text)
        return "New note added"

    @input_error_notes
    def show_notes(self):
        result = ""
        for key, value in self.notes.get_notes():
            result += self.print_note(key, value)
        return result

    @input_error_notes
    def add_tags(self, data: str) -> str:
        note_id, *tags = data.split(" ")

        if not tags:
            return "There are no tags in your input"
        self.notes.add_tags(int(note_id), tags)
        return "Tags added"

    @input_error_notes
    def delete_note(self, data: str) -> str:
        note_id = int(data)
        self.notes.delete_note(note_id)
        return f"Note [{note_id}] deleted"

    @input_error_notes
    def edit_note(self, data: str) -> str:
        note_id, *note_text_list = data.split(" ")
        note_id = int(note_id)
        note_text = " ".join(note_text_list)

        self.notes.edit_note(note_id, note_text)
        return f"Note [{note_id}] edited"

    @input_error_notes
    def search_notes(self, data):
        result = ""
        for key, value in self.notes.search_notes(data).items():
            result += self.print_note(key, value)
        return result

    @input_error_notes
    def search_notes_by_tags(self, data: str) -> str:
        tags = data.split(" ")

        search_results = self.notes.search_notes_by_tags(tags)

        if not search_results:
            return "There are no notes with these tags"

        output = ''

        for tag in sorted(search_results):
            output += f"Tag - {tag}:\n"

            for key, note in search_results[tag].items():
                output += f"  {key}: {note.note_text}\n"
            output += "------------------------------------\n"

        return output

    def sort_notes(self) -> str:
        result = ""
        for key, value in bot.notes.sort_notes().items():
            result += self.print_note(key, value)
        return result

    def save_data(self) -> None:
        self.address_book.save_contacts_to_file()
        self.notes.save_notes_to_file()


bot = Bot(AddressBook(), Notes())
