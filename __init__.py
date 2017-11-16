import sys
import dbus
from traceback import print_exc
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger

__author__ = 'aix'

LOGGER = getLogger(__name__)


class MycroftPlasmoidControlSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(MycroftPlasmoidControlSkill, self).__init__(name="MycroftPlasmoidControlSkill")

    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))

        mycroftplasmoid_plasma_show_intent = IntentBuilder("MycroftPlasmoidShowKeywordIntent").\
            require("MycroftPlasmoidShowKeyword").build()
        self.register_intent(mycroftplasmoid_plasma_show_intent, self.handle_mycroftplasmoid_plasma_show_intent)

        mycroftplasmoid_plasma_showskills_intent = IntentBuilder("MycroftPlasmoidShowSkillsKeywordIntent").\
            require("MycroftPlasmoidShowSkillsKeyword").build()
        self.register_intent(mycroftplasmoid_plasma_showskills_intent, self.handle_mycroftplasmoid_plasma_showskills_intent)

    def handle_mycroftplasmoid_plasma_show_intent(self, message):

        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.mycroftapplet", "/mycroftapplet")
        remote_object.showMycroft(dbus_interface="org.kde.mycroftapplet")

    def handle_mycroftplasmoid_plasma_showskills_intent(self, message):

        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.mycroftapplet", "/mycroftapplet")
        remote_object.showSkills(dbus_interface="org.kde.mycroftapplet")

    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
        return MycroftPlasmoidControlSkill()
