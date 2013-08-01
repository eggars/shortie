from django.db import models
import base64

class Record(models.Model):
      url = models.CharField(max_length=400)
      
      def __unicode__(self):
          return self.url

      def to_base64(self):
          return base64.urlsafe_b64encode(str(self.id))

      @staticmethod
      def id_from_base64(base64_str):
          return int(base64.urlsafe_b64decode(base64_str))
