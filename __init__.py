"""
Mycroft Plasmoid Control Skill.
"""
import sys
import dbus
import requests
from traceback import print_exc
from os.path import dirname
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import getLogger
from mycroft.audio import speech
from bs4 import BeautifulSoup

__author__ = 'aix'

LOGGER = getLogger(__name__)

class MycroftPlasmoidControlSkill(MycroftSkill):
    def __init__(self):
        """
        MycroftPlasmoidControl Skill Class.
        """ 
        super(MycroftPlasmoidControlSkill, self).__init__(name="MycroftPlasmoidControlSkill")
        
    @intent_handler(IntentBuilder("MycroftPlasmoidShowKeywordIntent").require("MycroftPlasmoidShowKeyword").build())
    def handle_mycroftplasmoid_control_showmycroft_skill_intent(self, message):
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.mycroftapplet", "/mycroftapplet")
        remote_object.showMycroft(dbus_interface="org.kde.mycroftapplet")

    @intent_handler(IntentBuilder("MycroftPlasmoidShowSkillsKeywordIntent").require("MycroftPlasmoidShowSkillsKeyword").build())
    def handle_mycroftplasmoid_control_showskillsmycroft_skill_intent(self, message):
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.mycroftapplet", "/mycroftapplet")
        remote_object.showSkills(dbus_interface="org.kde.mycroftapplet")

    @intent_handler(IntentBuilder("MycroftPlasmoidShowInstallerKeywordIntent").require("MycroftPlasmoidShowInstallerKeyword").build())        
    def handle_mycroftplasmoid_control_showinstallermycroft_skill_intent(self, message):
        bus = dbus.SessionBus()
        remote_object = bus.get_object("org.kde.mycroftapplet", "/mycroftapplet")
        remote_object.showSkillsInstaller(dbus_interface="org.kde.mycroftapplet")
        
    @intent_handler(IntentBuilder("MycroftPlasmoidReadNewsIntent").require("MycroftPlasmoidReadNewsKeyword").build())
    def handle_mycroftplasmoid_control_readnews_skill_intent(self, message):
        utterance = message.data.get('utterance').lower()
        utterance = utterance.replace(message.data.get('MycroftPlasmoidReadNewsKeyword'), '')
        urlString = utterance.replace(" ", "")
        method = "GET"
        response = requests.request(method, urlString)
        soup = BeautifulSoup(response.text)
        for script in soup(["script", "style", "a"]):
            script.extract()
        
        body = soup.find('body')
        text = soup.get_text()
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        self.speak(text)

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
