"""
Plasma Mycroft Plasmoid Skill. 
"""

import sys
import dbus
from traceback import print_exc
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger

__author__ = 'aix'

LOGGER = getLogger(__name__)


class MycroftPlasmoidControlSkill(MycroftSkill):
    """
    Mycroft Plasmoid Skill Class.
    """

    def __init__(self):
        """
        Initialization
        """
        super(MycroftPlasmoidControlSkill, self).__init__(name="MycroftPlasmoidControlSkill")

    @intent_handler(IntentBuilder("MycroftPlasmoidShowKeywordIntent").
            require("MycroftPlasmoidShowKeyword").build())
    def handle_mycroftplasmoid_plasma_show_intent(self, message):
        """
        Show Mycroft Plasmoid
        """
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.mycroftapplet", "/mycroftapplet")
        remote_object.showMycroft(dbus_interface="org.kde.mycroftapplet")

    @intent_handler(IntentBuilder("MycroftPlasmoidShowSkillsKeywordIntent").
            require("MycroftPlasmoidShowSkillsKeyword").build())
    def handle_mycroftplasmoid_plasma_showskills_intent(self, message):
        """
        Show Mycroft Plasmoid Skills Page
        """
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.mycroftapplet", "/mycroftapplet")
        remote_object.showSkills(dbus_interface="org.kde.mycroftapplet")

    def stop(self):
        """
        Mycroft Stop Function
        """
        pass


def create_skill():
    """
    Mycroft Create Skill Function
    """
    return MycroftPlasmoidControlSkill()
