# Simple Notes Management System (Python)

notes = []

def add_note():
    title = input("Enter Note Title: ")
    content = input("Enter Note Content: ")

    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content
    }

    notes.append(note)
    print("Note Added Successfully!\n")


def view_notes():
    if len(notes) == 0:
        print("No Notes Available.\n")
    else:
        print("\n----- Notes -----")
        for note in notes:
            print(f"ID      : {note['id']}")
            print(f"Title   : {note['title']}")
            print(f"Content : {note['content']}")
            print("-----------------------")
        print()


def update_note():
    note_id = int(input("Enter Note ID to Update: "))

    for note in notes:
        if note["id"] == note_id:
            note["title"] = input("New Title: ")
            note["content"] = input("New Content: ")
            print("Note Updated Successfully!\n")
            return

    print("Note Not Found!\n")


def delete_note():
    note_id = int(input("Enter Note ID to Delete: "))

    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            print("Note Deleted Successfully!\n")
            return

    print("Note Not Found!\n")


while True:
    print("===== NOTES MANAGEMENT =====")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Update Note")
    print("4. Delete Note")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_note()

    elif choice == "2":
        view_notes()

    elif choice == "3":
        update_note()

    elif choice == "4":
        delete_note()

    elif choice == "5":
        print("Program Closed.")
        break

    else:
        print("Invalid Choice!\n")
