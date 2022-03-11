from mycroft import MycroftSkill, intent_file_handler


class FirstSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('skill.first.intent')
    def handle_skill_first(self, message):
        self.speak_dialog('skill.first')


def create_skill():
    return FirstSkill()

