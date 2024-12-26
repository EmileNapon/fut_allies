from django.db import models
from users.models import CustomUser



class Domaine(models.Model):
    nom_domaine = models.CharField(max_length=800) 
    def __str__(self):
        return self.nom_domaine

class Module(models.Model):
    domaine = models.ForeignKey(Domaine, on_delete=models.CASCADE, default=1) 
    nom_module = models.CharField(max_length=800, default='')
   # formateur = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom_module

class Cours(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, default=1)  # Relation vers Module
    nom_cours = models.CharField(max_length=800, default='')

    def __str__(self):
        return self.nom_cours

class Chapitre(models.Model):
    cours = models.ForeignKey(Cours, on_delete=models.CASCADE, default=1)  # Relation vers Cours
    titre = models.CharField(max_length=800, default='')

    def __str__(self):
        return self.titre




class Section(models.Model):
    chapitre = models.ForeignKey(Chapitre, on_delete=models.CASCADE, default=1)  # Relation vers Chapitre
    nom_section = models.TextField()
    def __str__(self):
        return self.nom_section  # Retourne les premiers 50 caractères



class Contenu(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, default=1)  # Relation vers Chapitre
    description = models.TextField(max_length=800, default='')
    def __str__(self):
        return self.description  # Retourne les premiers 50 caractères

    
class Video(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, default=1)  # Relation vers Chapitre
    nom_video = models.TextField(max_length=800)
    def __str__(self):
        return self.nom_video  # Retourne les premiers 50 caractères


class Audio(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, default=1)  # Relation vers Chapitre
    nom_audio = models.TextField(max_length=800, default='')
    def __str__(self):
        return self.nom_audio  # Retourne les premiers 50 caractères

########################################################################################################
    ############################################################################################
from django.db import models

class Webinar(models.Model):
    FUTUR_ALLIES = 'FuturAllies'
    CAFE_DES_ALLIES = 'Café des allies'
    WEBINAR_TYPES = [
        (FUTUR_ALLIES, 'FuturAllies'),
        (CAFE_DES_ALLIES, 'Café des allies'),
    ]
    WEBINAR_FORMAT = [
        (FUTUR_ALLIES, 'Gratuit'),
        (CAFE_DES_ALLIES, 'Payant'),
    ]

    _id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    startDateTime=models.DateTimeField()
    duree = models.CharField(max_length=20)
    webinarUrl = models.URLField(blank=True)
    description = models.TextField(null=True, blank=True)
    maxParticipants = models.IntegerField()
    registrationDeadline = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    isPaid = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    format = models.CharField(max_length=20, choices=WEBINAR_FORMAT, default='Payant')
    type = models.CharField(max_length=20, choices=WEBINAR_TYPES)

    def __str__(self):
        return self.title

class WebinarEnrollment(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('free', 'Free')
    ]

    PAYMENT_METHOD_CHOICES = [
        ('creditCard', 'Credit Card'),
        ('orangeMoney', 'Orange Money'),
        ('moovMoney', 'Moov Money'),
        ('sankMoney', 'Sank Money')
    ]
    webinarId = models.ForeignKey(Webinar, on_delete=models.CASCADE, related_name="enrollments")
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE, null=True)
    whatsapp = models.CharField(max_length=10, null=True)
    registrationDate = models.DateTimeField(auto_now_add=True)
    hasAcceptedTerms = models.BooleanField(default=False)
    paymentStatus = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, null=True, blank=True)
    paymentMethod = models.CharField(max_length=15, choices=PAYMENT_METHOD_CHOICES, null=True, blank=True)
    isConfirmed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('webinarId', 'user')  # Assure qu'un utilisateur ne peut s'inscrire qu'une seule fois à une formation
    def __str__(self):
        return f"{self.user} inscrit à {self.webinarId}"
    






