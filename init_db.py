from tinydb import TinyDB


def init():
    with open("db.json", "w") as f:
        db = TinyDB("db.json")

        data = [
            {
                "name": "Contact Information",
                "full_name": "text",
                "email": "email",
                "phone_number": "phone",
            },
            {
                "name": "Event Registration",
                "event_name": "text",
                "event_date": "date",
                "participant_email": "email",
            },
            {
                "name": "Feedback Form",
                "feedback_text": "text",
                "rating": "text",
                "feedback_date": "date",
            },
        ]

        db.insert_multiple(data)
