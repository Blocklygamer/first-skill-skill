from mycroft import MycroftSkill, intent_file_handler
from mycroft.skills.audioservice import AudioService


class FirstSkill(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
        
    def initialize(self):
        self.audioservice = AudioService(self.bus)
        

    @intent_file_handler('skill.first.intent')
    def handle_skill_first(self, message):
        self.speak_dialog('skill.first')
        self.audio_service.play(join(dirname(__file__), "magic.mp3"))


def create_skill():
    return FirstSkill()

