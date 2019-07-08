from django.apps import AppConfig


class JcboseConfig(AppConfig):
    name = 'jcbose'

    def ready(self):
    	import jcbose.signals	