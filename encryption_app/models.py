from django.db import models

class EncryptedMessage(models.Model):
    message = models.TextField()
    encrypted_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message {self.id} at {self.timestamp}"
